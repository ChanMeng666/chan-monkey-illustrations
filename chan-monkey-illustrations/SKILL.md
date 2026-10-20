---
name: chan-monkey-illustrations
description: Generate Chan Meng–branded inline illustrations for articles, blog posts, newsletters, LinkedIn posts, docs and talks, starring Chan's brand monkey (the solid-ink monkey head from the chanmeng.org logo). Use whenever the user asks for article illustrations, blog images, inline figures, a shot list, "配图", "正文配图", "文章插图", "猴子配图", "Chan monkey illustration", or wants a judgement, workflow, structure, state or metaphor from their writing drawn as a picture; also for editing or regenerating one of these images (remove text, fix a label, make the monkey more central). English or Chinese articles.
---

# Chan Monkey Illustrations

Turn the one idea in a paragraph that most deserves a picture into a 16:9 hand-drawn
figure: white page, ink line art, a few brand-colour notes — and the **Chan monkey** doing
the work that explains the idea.

Not commercial illustration, not a slide, not a mascot sticker. The test of every image:
the reader smiles at what the monkey is doing, then understands the structure in one second.

## Read before generating

Load only what the step needs:

- `references/monkey-ip.md` — the character: what is frozen from the logo, the body, the
  tail, the expression set, the ink-on-ink rule. **Always read before the first prompt.**
- `references/style-dna.md` — page, line, palette, type, what is banned.
- `references/composition-patterns.md` — structure types and how to invent a fresh metaphor.
- `references/prompt-template.md` — the generation and edit prompts.
- `references/qa-checklist.md` — pass/fail checks and iteration moves.
- `assets/monkey/monkey-reference.png` — the identity reference passed to the image model
  on every generation. Never redraw the head from words alone.
- `assets/examples/` — style calibration only. Do not copy their compositions.

## Workflow

### 1. Digest the text

Read what the user gave (file, URL, pasted text, `content/*.mdx` in the portfolio). Find
the cognitive anchors: the core claim, the turning points, a before/after, a loop, a fork,
a pitfall, a role change. Skip paragraphs a picture would only decorate.

Detect the article language. Labels in the image follow it: English article → English
labels; Chinese article → Chinese labels. Do not mix unless the user asks.

### 2. Shot list first

If the user asks what to illustrate, or the article is long and the count is unclear, give
a shot list before generating. Per image:

- after which paragraph / heading
- slug (`02-tail-as-a-hook`)
- core idea (one sentence)
- structure type
- what the monkey is doing (the action that carries the idea) and its mood
- 3–6 label words

Default 3–6 images. Short post: 1–2. Never more than 8 — this is a blog, not a picture book.

### 3. Generate, one image per call

If the user said generate / make / draw, do not stop to confirm the shot list. Generate
each image separately with the bundled script (never several images stitched into one):

```bash
python scripts/generate_image.py \
  --prompt-file <scratch>/03-prompt.txt \
  --out <workspace>/assets/<article-slug>-illustrations/03-topic.png
```

The script sends `assets/monkey/monkey-reference.png` as a reference image through the
OpenAI Images edit endpoint with high input fidelity, so the monkey stays on-model. Write
each prompt from `references/prompt-template.md` into a file first; keep the prompt files —
they are the recipe for regenerating.

Sizes: `--size article` (default, 1536×864), `--size linkedin` (1080×1350), `--size x`
(1600×900). Page colour: `--ground white` (default) or `--ground basalt` for social posts —
see "Social post profile" in `references/style-dna.md`.

Environment: `OPENAI_API_KEY` (required), optional `OPENAI_BASE_URL`, `OPENAI_IMAGE_MODEL`
(default `gpt-image-2`). The script reads a `.env` in the current directory or the skill
folder. If no key is available and the host has its own image tool (e.g. Codex `image_gen`),
use that tool with the same prompt **and attach the reference PNG**; never generate the
monkey without the reference.

Invent a new metaphor for every image from *this* article. The examples show density and
how the monkey participates; they are not templates.

### 4. Check and iterate

Look at every image (open the PNG) against `references/qa-checklist.md`. Regenerate, or
edit with `--edit <image>`, when:

- the head is off-model (curl missing or sweeping the wrong way, eyes not round, face not white,
  ears without inner knockout)
- the monkey is decoration, not the actor
- it reads as a slide, flowchart or corporate infographic
- too many labels, misspelt labels, or a title in a corner
- the background is not clean white

Two failed attempts at the same image → simplify the scene (fewer objects, fewer labels)
rather than retrying the same prompt.

### 5. Save and report

Save into the user's workspace:

```text
assets/<article-slug>-illustrations/01-topic-name.png
assets/<article-slug>-illustrations/prompts/01-topic-name.txt
```

For the 2d-portfolio blog, use `public/blog/<post-slug>/` (the existing per-post folder
convention) and reference images from the MDX with alt text written from the core idea.

Never overwrite an existing image unless asked; write `-v2` alongside instead.

Report: how many images, what each one is for and where it goes in the text, the paths,
and which ones are strongest vs optional. Keep it short; let the pictures talk.
