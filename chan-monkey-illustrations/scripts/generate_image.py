#!/usr/bin/env python3
"""
Generate (or edit) one Chan monkey illustration.

Calls the OpenAI Images edit endpoint with the brand monkey reference attached, so the head
stays on-model. Works with the official API or an OpenAI-compatible endpoint via
OPENAI_BASE_URL.

  python generate_image.py --prompt-file 01.txt --out assets/post-illustrations/01-x.png
  python generate_image.py --edit 01-x.png --prompt "Remove the text ..." --out 01-x-v2.png
"""

import argparse
import base64
import os
import shutil
import sys
from pathlib import Path

SKILL_DIR = Path(__file__).resolve().parent.parent
REFERENCE = SKILL_DIR / "assets" / "monkey" / "monkey-reference.png"

try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None

try:
    from openai import OpenAI, BadRequestError
except ImportError:
    sys.exit("Error: openai package not installed. Run: pip install -r requirements.txt")


def load_env() -> None:
    if load_dotenv is None:
        return
    # The working directory wins over the skill folder.
    load_dotenv(Path.cwd() / ".env")
    load_dotenv(SKILL_DIR / ".env")


def build_client() -> OpenAI:
    # An empty OPENAI_BASE_URL= line would be picked up by the SDK as a scheme-less base
    # URL, so only pass one when it is actually set.
    base_url = os.environ.get("OPENAI_BASE_URL", "").strip()
    if not base_url:
        os.environ.pop("OPENAI_BASE_URL", None)
    kwargs = {"api_key": os.environ["OPENAI_API_KEY"]}
    if base_url:
        kwargs["base_url"] = base_url
    return OpenAI(**kwargs)


def free_path(path: Path) -> Path:
    """Never overwrite: 01-x.png -> 01-x-v2.png -> 01-x-v3.png ..."""
    if not path.exists():
        return path
    n = 2
    while True:
        candidate = path.with_name(f"{path.stem}-v{n}{path.suffix}")
        if not candidate.exists():
            return candidate
        n += 1


# Final pixel sizes. Requests are rounded up to multiples of 16 (an API constraint), then
# cropped and resized to these.
SIZES = {
    "article": (1536, 864),   # 16:9 inline figure
    "linkedin": (1080, 1350), # 4:5 portrait, the most feed space on LinkedIn
    "x": (1600, 900),         # 16:9, shows uncropped on X
}

# The page colour. Generation is always on white; a non-white ground is swapped in after.
GROUNDS = {
    "white": None,
    "basalt": (0xE2, 0xE2, 0xDF),  # social post visuals (linkedin-post-skill)
    "ash": (0xF7, 0xF6, 0xF2),
}


def parse_size(value: str) -> tuple[int, int]:
    if value in SIZES:
        return SIZES[value]
    w, h = (int(v) for v in value.lower().split("x"))
    return w, h


def request_size(width: int, height: int) -> str:
    def up16(v: int) -> int:
        return -(-v // 16) * 16
    return f"{up16(width)}x{up16(height)}"


def fallback_size(width: int, height: int) -> str:
    ratio = width / height
    if ratio > 1.1:
        return "1536x1024"
    if ratio < 0.9:
        return "1024x1536"
    return "1024x1024"


def finish(data: bytes, width: int, height: int, ground) -> bytes:
    """Centre-crop to the target aspect, resize to the exact size, swap in the ground."""
    from io import BytesIO
    from PIL import Image

    img = Image.open(BytesIO(data)).convert("RGB")
    w, h = img.size
    target = width / height
    if abs(w / h - target) > 0.005:
        if w / h > target:
            new_w = round(h * target)
            img = img.crop(((w - new_w) // 2, 0, (w - new_w) // 2 + new_w, h))
        else:
            new_h = round(w / target)
            img = img.crop((0, (h - new_h) // 2, w, (h - new_h) // 2 + new_h))
    if img.size != (width, height):
        img = img.resize((width, height), Image.LANCZOS)
    if ground is not None:
        img = swap_ground(img, ground)
    out = BytesIO()
    img.save(out, format="PNG")
    return out.getvalue()


def swap_ground(img, ground):
    """Replace white paper with the ground colour, leaving ink and brand colours alone.

    Each pixel moves toward the ground by (its darkest channel / 255) ** 4: paper white moves
    all the way, anti-aliased edges part way, and saturated orange / violet (darkest channel
    near 0) and ink stay put. The monkey's face knockout becomes the ground too, as it is
    on the real logo.
    """
    import numpy as np
    from PIL import Image

    px = np.asarray(img, dtype=np.float32)
    weight = (px.min(axis=2, keepdims=True) / 255.0) ** 4
    out = px * (1 - weight) + np.array(ground, dtype=np.float32) * weight
    return Image.fromarray(out.round().clip(0, 255).astype(np.uint8))


def main() -> int:
    load_env()
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    src = p.add_mutually_exclusive_group(required=True)
    src.add_argument("--prompt", help="prompt text")
    src.add_argument("--prompt-file", type=Path, help="file holding the prompt")
    p.add_argument("--out", type=Path, required=True, help="output PNG path")
    p.add_argument("--edit", type=Path, help="image to edit (sent first, before the monkey reference)")
    p.add_argument("--ref", type=Path, action="append", default=[], help="extra reference image (repeatable)")
    p.add_argument("--size", default=os.getenv("OPENAI_IMAGE_SIZE", "article"),
                   help="article (1536x864, default) | linkedin (1080x1350) | x (1600x900) | WIDTHxHEIGHT")
    p.add_argument("--ground", choices=sorted(GROUNDS), default="white",
                   help="page colour: white (default), basalt (social posts), ash")
    p.add_argument("--overwrite", action="store_true", help="replace --out instead of writing -v2")
    p.add_argument("--quality", default=os.getenv("OPENAI_IMAGE_QUALITY", "high"))
    p.add_argument("--model", default=os.getenv("OPENAI_IMAGE_MODEL", "gpt-image-2"))
    args = p.parse_args()

    if not os.environ.get("OPENAI_API_KEY"):
        print("Error: OPENAI_API_KEY is not set (environment or .env).", file=sys.stderr)
        return 2

    prompt = args.prompt if args.prompt is not None else args.prompt_file.read_text(encoding="utf-8")
    images = ([args.edit] if args.edit else []) + [REFERENCE] + args.ref
    for img in images:
        if not img.is_file():
            print(f"Error: image not found: {img}", file=sys.stderr)
            return 2

    width, height = parse_size(args.size)
    size = request_size(width, height)
    client = build_client()
    files = [open(img, "rb") for img in images]
    request = dict(
        model=args.model,
        image=files,
        prompt=prompt,
        n=1,
        quality=args.quality,
    )
    # gpt-image-2 always reads input images at high fidelity and rejects the parameter;
    # gpt-image-1.x needs it to keep the monkey's head on-model.
    if args.model.startswith("gpt-image-1"):
        request["input_fidelity"] = "high"
    try:
        print(f"Generating with {args.model} at {size} ({len(images)} input image(s))...")
        try:
            result = client.images.edit(size=size, **request)
        except BadRequestError as e:
            # Endpoints without custom sizes: fall back to 3:2 and crop.
            fallback = fallback_size(width, height)
            if size == fallback or "size" not in str(e.body or e.message).lower():
                raise
            print(f"Size {size} rejected; retrying at {fallback} and cropping.")
            for f in files:
                f.seek(0)
            result = client.images.edit(size=fallback, **request)
    finally:
        for f in files:
            f.close()

    data = base64.b64decode(result.data[0].b64_json)
    data = finish(data, width, height, GROUNDS[args.ground])

    out = args.out if args.overwrite else free_path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_bytes(data)

    # Keep the recipe next to the image so it can be regenerated.
    prompts_dir = out.parent / "prompts"
    prompts_dir.mkdir(exist_ok=True)
    if args.prompt_file and args.prompt_file.resolve() != (prompts_dir / f"{out.stem}.txt").resolve():
        shutil.copyfile(args.prompt_file, prompts_dir / f"{out.stem}.txt")
    elif args.prompt is not None:
        (prompts_dir / f"{out.stem}.txt").write_text(prompt, encoding="utf-8")

    print(f"Saved {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
