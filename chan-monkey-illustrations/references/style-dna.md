# Style DNA

## In one line

White page, ink line art, lots of air, three brand colours used sparingly — a builder's
sketchbook where the logo monkey is stamped in clean and everything else is drawn by hand.

## Page

- 16:9 landscape (generated at 1536×1024 or wider, then used as a 16:9 figure).
- **Pure white** background. No paper texture, cream, grey wash, gradient, shadow, vignette,
  noise or border.
- The subject occupies roughly 40–60% of the canvas; keep at least a third of the page
  empty, ideally one whole quiet area.

## Line

- Black ink (`#070607`), thin, slightly wobbly, confident — a felt-tip on paper, not vector.
- Objects are simple line drawings: outlines, few interior details, no hatching for shading.
- The monkey's head and body are the only large solid ink areas on the page.

## Palette (chanmeng.org brand)

| colour | hex | job |
|---|---|---|
| ink | `#070607` | line art, the monkey, most label text |
| orange | `#FC5000` | the main path: flow arrows, motion lines, the one thing that moves from A to B; key emphasis |
| violet | `#524AE9` | AI / system / automation, secondary notes, feedback loops, the monkey's emote marks |
| glare | `#F5F28E` | a highlighter swipe behind **one** key label or object, max one per image |

No other colours. No red, green or blue-grey. Colour covers well under 10% of the page.
Violet is optional; use it only when there is a second layer (system state, AI, feedback).

## Labels

- Handwritten-looking, short: 1–4 words in English, 2–8 characters in Chinese.
- At most 5–7 labels. Fewer is better; image models misspell long text.
- Labels in the article's language. Ink for names of things, orange for the action or the
  result, violet for side notes.
- No title, no heading, no caption block, no structure-type name ("Workflow", "Architecture"),
  no logo wordmark ("CHAN") unless asked.

## Mood of the page

Clever, playful, clean, a little absurd — an idea you'd sketch to explain something to a
friend at a whiteboard, with a wink.

## Banned

- Commercial or corporate illustration, flat vector "tech people" scenes.
- Slides, infographics, formal flowcharts, architecture diagrams, course material.
- Realistic UI, screenshots, glowing tech, 3D, isometric.
- Children's book style, kawaii, sticker sheets, emoji style.
- Dense scenes: many nodes, many arrows, every step explained.

## Social post profile (LinkedIn / X)

Used when the image goes in a feed — `linkedin-post-skill` calls this skill with it. The
feed has stricter brand rules than the blog, and the image is seen at phone width for a
second while scrolling:

- `--ground basalt` (`#E2E2DF`): post visuals are never pure white. Prompt on white as usual;
  the script swaps the ground after generation.
- `--size linkedin` (1080×1350, 4:5) and `--size x` (1600×900, 16:9). Compose for the shape:
  portrait stacks vertically (monkey low, the thing it works on above, or the reverse);
  landscape reads left to right.
- **One orange accent**: the single element the post is about (the path, the thing being
  moved, the result). Not every arrow.
- **Violet is never text**: violet marks only (emotes, bubbles, a feedback loop). Labels are
  ink.
- Glare at most once, as a highlighter swipe.
- **0–3 labels**, 1–3 words each. The post carries the words; the image carries the idea.
- Bigger and simpler than an article figure: one object, the monkey at least a quarter of
  the frame's height, subject filling ~60%.
