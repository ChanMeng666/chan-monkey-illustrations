# QA checklist

Open every generated PNG and check it. Do not report an image you have not looked at.

## Must pass

**Character**
- [ ] Head is on-model: solid ink, white heart-shaped face, round eyes, two nostril dots,
      smile, inner-ear crescents.
- [ ] The two-strand curl is there, rising from the crown, sweeping up to the right.
- [ ] Body small, limbs thin, tail present when the scene uses it.
- [ ] No ink-on-ink detail; anything over the head is orange or violet.
- [ ] The monkey performs the core action (delete-the-monkey test fails).

**Page**
- [ ] 16:9 landscape, clean pure white background.
- [ ] Subject ≤ ~60% of canvas; a quiet empty area exists.
- [ ] One idea, one structure.
- [ ] Only ink, orange, violet, glare. Orange = flow/emphasis; violet = system/side notes.

**Text**
- [ ] ≤ 7 labels, all short, spelled exactly as in the prompt, in the article's language.
- [ ] No title, caption, structure name, watermark, or stray gibberish text.

**Taste**
- [ ] First reaction "ha, clever", then the structure is clear within a second.
- [ ] Not a slide, flowchart, corporate vector or kids' book.
- [ ] Not a copy of an example image or of another image in the same article.

## Failure → fix

| failure | fix |
|---|---|
| head redrawn / curl wrong / face grey | edit with the "fix an off-model head" prompt; if the whole style drifted, regenerate |
| monkey is decoration | rewrite the scene so the monkey's verb is the idea; consider the tail |
| too busy | drop to one object and 3–4 labels |
| slide / diagram look | remove boxes, grids and extra arrows; one physical scene |
| too cute | "warm but not babyish; no blush, no sparkle; builder at work" |
| misspelt labels | edit to fix one label; if several, regenerate with fewer, shorter labels |
| colour creep | restate "no other colours"; drop violet if not needed |
| looks like an old example | keep the idea, change the main object and the action |

## Delivery bar

If the first impression is "tutorial page" rather than "a clever sketch with Chan's monkey
in it", it doesn't ship.
