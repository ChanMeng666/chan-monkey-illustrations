#!/usr/bin/env node
// Re-render assets/monkey/monkey-reference.png from the logo SVG: the head at 760 px, centred on
// a 1024 px white square. Run it whenever the logo changes.
//
//   node tools/render-reference.cjs <chan-meng-monkey-black-on-white.svg> [path/to/sharp]
//
// sharp is not a dependency of this repo; pass the path of any installed copy if it can't be
// required from here (e.g. ../2d-portfolio/node_modules/sharp).
const path = require('path');
const [svg, sharpPath = 'sharp'] = process.argv.slice(2);
if (!svg) {
  console.error('Usage: node tools/render-reference.cjs <monkey-black-on-white.svg> [path/to/sharp]');
  process.exit(1);
}
const sharp = require(sharpPath);
const out = path.join(__dirname, '..', 'chan-monkey-illustrations', 'assets', 'monkey', 'monkey-reference.png');

(async () => {
  const head = await sharp(svg, { density: 600 })
    .resize(760, 760, { fit: 'contain', background: '#ffffff' })
    .flatten({ background: '#ffffff' })
    .png()
    .toBuffer();
  await sharp({ create: { width: 1024, height: 1024, channels: 3, background: '#ffffff' } })
    .composite([{ input: head, left: 132, top: 132 }])
    .png()
    .toFile(out);
  console.log(`Saved ${out}`);
})();
