# Chan Monkey Illustrations

> Hand-drawn inline illustrations for articles, starring Chan Meng's brand monkey.
>
> 16:9 · white page · ink line art · brand orange / violet / glare · English or Chinese labels · Agent Skill

![Walk your tech, don't let it walk you](examples/images/01-tech-on-a-leash.png)

An agent skill that reads an article, finds the few ideas worth drawing, invents a fresh
physical metaphor for each, and generates one figure per idea — with the monkey from the
[chanmeng.org](https://chanmeng.org) logo doing the work that explains it.

The head is never redrawn from words: every generation sends the logo as a reference image,
so the monkey stays on-model across articles.

## What it makes

- a shot list: where each figure goes, its idea, structure, the monkey's action and mood, labels
- one PNG per figure, 1536×864 (16:9)
- the prompt behind every image, saved next to it so it can be regenerated

Not slides, infographics, architecture diagrams, posters or mascot stickers.

## The character

| frozen (the logo) | free (added for illustrations) |
|---|---|
| solid ink head, round ears with white inner crescents | small rounded ink body |
| white heart-shaped face, round eyes, two nostril dots, smile | thin line arms and legs |
| the two-strand curl sweeping up to the right | a long curly tail — its third hand |
| | ten expressions from the portfolio's mood set |

Props over the head are drawn in brand colour, never ink on ink. Full spec:
[`references/monkey-ip.md`](chan-monkey-illustrations/references/monkey-ip.md).

## Palette

| ink `#070607` | orange `#FC5000` | violet `#524AE9` | glare `#F5F28E` |
|---|---|---|---|
| line art, the monkey | main flow, arrows, emphasis | AI / system / side notes | one highlighter swipe |

![最小闭环](examples/images/02-minimum-loop-zh.png)

## Install

The skill is the inner folder `chan-monkey-illustrations/`.

**Claude Code**

```bash
cp -r chan-monkey-illustrations ~/.claude/skills/
pip install -r ~/.claude/skills/chan-monkey-illustrations/requirements.txt
```

**Codex**

```bash
cp -r chan-monkey-illustrations "${CODEX_HOME:-$HOME/.codex}/skills/"
```

Set `OPENAI_API_KEY` in the environment or in a `.env` (see
[`.env.example`](chan-monkey-illustrations/.env.example)); `OPENAI_BASE_URL` is supported for
compatible endpoints.

## Use

```text
Use chan-monkey-illustrations: plan the figures for content/digital-minimalism.mdx — shot list only.
```

```text
Use chan-monkey-illustrations to generate 4 illustrations for this article and save them in public/blog/<slug>/.
```

```text
用 chan-monkey-illustrations 给这篇文章生成 3 张猴子正文配图。
```

```text
Edit 03-handoff.png: the curl is on the wrong side, fix only the head.
```

The script can also be called directly:

```bash
python chan-monkey-illustrations/scripts/generate_image.py --prompt-file prompt.txt --out out/01-idea.png
python chan-monkey-illustrations/scripts/generate_image.py --edit out/01-idea.png --prompt "Remove the text ..." --out out/01-idea.png
```

It never overwrites: an existing `01-idea.png` makes it write `01-idea-v2.png`.

## Layout

```text
chan-monkey-illustrations/          # the skill
├── SKILL.md
├── agents/openai.yaml
├── references/
│   ├── monkey-ip.md                # the character
│   ├── style-dna.md                # page, line, palette, labels
│   ├── composition-patterns.md     # structures + metaphor method
│   ├── prompt-template.md          # generation and edit prompts
│   └── qa-checklist.md
├── scripts/generate_image.py       # OpenAI Images edit + monkey reference
├── assets/monkey/                  # monkey-reference.png (1024², black on white) + source SVG
└── assets/examples/                # calibration images
examples/                           # README images and their prompts
```

`monkey-reference.png` is rendered from `chan-meng-logo/assets/monkey/chan-meng-monkey-black-on-white.svg`
at 760 px on a 1024 px white square. If the logo changes, re-render it.

## Credits

Workflow adapted from [Ian Xiaohei Illustrations](https://github.com/helloianneo/ian-xiaohei-illustrations)
by Ian (MIT). See [NOTICE.md](NOTICE.md).

## License

Code and docs: MIT. The monkey mark is Chan Meng's personal brand — see [NOTICE.md](NOTICE.md).
