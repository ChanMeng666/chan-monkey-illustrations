# Prompt templates

One prompt per image, written to a file and passed to `scripts/generate_image.py`. The
script attaches `assets/monkey/monkey-reference.png`; the prompt must refer to it as
"the reference image".

## Generation

```text
Create one standalone 16:9 landscape illustration for a blog article.

CHARACTER — keep exactly on-model:
The reference image is the brand mark of the recurring character, the Chan monkey. Reproduce
its head exactly: one flat solid near-black (#070607) head with round ears, a white crescent
knockout in each ear, a large white heart/peanut-shaped face knockout, two big solid round
eyes, two small nostril dots, one wide shallow smile, and the signature two-strand hair curl
rising from the top of the crown and sweeping up to the right. Clean smooth curves, no outline, no texture,
no shading. Give it a small rounded solid ink body, thin line arms and legs, simple round
hands, and a long thin curly tail. The head stays the dominant part of the character.
Expression: {mood — e.g. "neutral: the logo's own eyes and smile" | "focused: eyes glancing right, small flat mouth"}.
The monkey must perform the core action of the idea, not decorate the scene.

STYLE:
Pure white background. Minimal hand-drawn black ink line art, thin slightly wobbly
felt-tip lines, generous empty space. The monkey is the only large solid black shape.
Sparse brand colour: orange (#FC5000) for the main flow, arrows and motion lines;
{violet (#524AE9) for secondary notes / AI / system state — or: "no violet"};
{one pale yellow (#F5F28E) highlighter swipe behind "<label>" — or: "no highlighter"}.
No other colours. No gradients, shadows, paper texture, 3D, realistic UI, corporate vector
style, slide or infographic look, children's-book or kawaii style.

IDEA:
{core idea in one sentence}

SCENE:
{structure type in plain words, e.g. "a single strange machine"}. {What the monkey is doing,
where, with what; how the thing flows from where to where; what the tail does if used.}

Objects: {object 1}, {object 2}{, object 3}.

LABELS — handwritten, short, spelled exactly as given, nothing else written:
"{label 1}", "{label 2}", "{label 3}"{, "{label 4}"}{, "{label 5}"}
{Language: English | Simplified Chinese}. Ink for names of things, orange for the action or
result, violet for side notes.

CONSTRAINTS:
One idea only. Subject fills about half the canvas, at least a third stays empty white.
No title, heading, caption, signature, watermark or logo wordmark. Do not write the
structure type. Not a formal diagram. Clever and playful, clean, a little absurd.
```

Keep the CHARACTER block word-for-word across every image of an article — it's the
consistency anchor. Change only the expression line.

## Edits (`--edit <image>`)

The script sends the image being edited first and the monkey reference second.

Remove text:

```text
Edit the first image. Remove only the text "{text}" (and its underline if any). Fill the
area with the same clean white background. Keep everything else exactly as it is:
character, labels, lines, colours, composition. Add nothing.
```

Fix an off-model head:

```text
Edit the first image. Redraw only the monkey's head so it matches the second image (the
brand mark) exactly: solid ink head, white face knockout, round eyes, two nostril dots,
smile, inner-ear crescents, and the two-strand curl rising from the crown and sweeping up to the right. Keep the
body pose, expression intent, everything else in the image and the composition unchanged.
```

Make the monkey the actor:

```text
Regenerate this illustration with the same idea and the same sparse layout, but make the
monkey do the core action: {new action}. Keep the white page, line style, labels and colours.
```

Fix a label:

```text
Edit the first image. Replace the handwritten label "{wrong}" with "{right}" in the same
hand-lettered style, colour, size and position. Change nothing else.
```

## Notes from calibration

- The head comes back on-model reliably when the reference is attached; spend the prompt's
  words on the scene, not on re-describing the face beyond the CHARACTER block.
- If the tail must do the action, say "with its tail (not its hands)" — otherwise the model
  often uses the hands and leaves the tail as decoration.
- Dense textures (tangles, crowds, piles) come out busier than asked; say "a loose tangle of
  a few loops" rather than "a huge tangled heap".
