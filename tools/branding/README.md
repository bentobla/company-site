# Website app artwork

The PNG `pictures/loern-icon-7d9d53a.png` is copied byte-for-byte from lœrn's
`assets/brand/icon.png`. Its new filename avoids retaining a cached old icon.
The earlier PNG remains available for existing external references.

The three `pictures/brand/*-splash.svg` files reuse the original SVG artwork and
port the native 3.3-second splash timelines. They play once when an existing app
icon becomes visible, at its existing size. They do not block page navigation.
No app runtime, remote fonts, third-party scripts or animation libraries load.
The static PNG stays visible until the animation image loads successfully.
Reduced motion (including a preference change mid-animation), unavailable
IntersectionObserver, JavaScript disabled, or a failed SVG request retain the PNG.
The SVGs themselves also default to their final state with reduced motion.

## Sources

| App | Source revision | Artwork | Animation reference |
| --- | --- | --- | --- |
| lœrn | `560f0856be78d388af34fa876286f15aaae78b36` | `assets/brand/icon.svg`, `icon.png`, `brand.json` | `lib/branding/brand_animation.dart`, `brand_artwork.dart` |
| sudøku | `014925f162a8d08ad01efa63fd3afbfb587960df` | `assets/brand/icon.svg` | `lib/branding/brand_animation.dart` |
| tøwer | `e7daf19d67acb45329611ae454fce59aa4120cd3` | `assets/icon.svg` | `ui/splash.gd` |

`sources/` contains the original SVG files. `FONT_LICENSE.txt` preserves the font
license supplied with the outlined lœrn/sudøku wordmarks. The animation generator
uses sampled native equations, at 20ms intervals; it removes redundant frames.
The geometry is normalized to the app icon square for the website rather than
the native full-screen splash viewport. It is a web port, not a device capture.

To update, replace the original artwork, check the source animation equations
and timing, update the source revisions above, then run:

```sh
python tools/branding/generate.py
node scripts/check_brand_motion.cjs
```

Keep image dimensions and the static fallback. Review the first, intermediate
and final artwork and reduced-motion behavior when changing the timeline.
