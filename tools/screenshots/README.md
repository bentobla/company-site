# App website captures

These are real app widgets / Godot views rendered from the source revisions in
`manifest.json`, with illustrative sample data. The PNGs are 1080×2160 pixels at
432×864 logical pixels. Website images are **lossless** WebP conversions; no UI
was painted over or generated with AI. Store listings may lag these main-branch
revisions. These are UI captures, without native phone status/navigation bars.

Use disposable app checkouts at the recorded revisions. No production accounts,
purchases, ad requests or user databases are needed. Keep capture-only changes
out of app release branches.

## Flutter (lœrn and sudøku)

Set `CAPTURE_FLUTTER_ROOT` to the Flutter SDK directory and `CI=true`. Flutter's
normal bot detector then skips cloud metadata discovery entirely. On Linux with
no writable system temp/cache, also set `TMPDIR` and `PUB_CACHE` to user-owned
directories. Run `flutter pub get` in each app checkout.

Copy `loern_capture_test.dart` or `sudoku_capture_test.dart` into that checkout's
`test/website_capture_test.dart`, then run:

```sh
flutter test --no-pub --update-goldens test/website_capture_test.dart
```

Output is `build/website/<locale>/<screen>.png`. The render tests assert no widget
exceptions before capturing. They use production screens, themes and localization
resources, with fake session/provider state. Ad loading is replaced by the app's
NullAdsService in the Sudoku harness. The seeded Sudoku puzzle comes from the
production generator.

For the Sudoku capture checkout only, suppress `debugButtons()` in
`lib/features/game/game_screen.dart` by making its early-return condition true.
This matches the absence of those buttons in a release build. No production UI
controls or content are removed.

**lœrn font caveat:** all four `assets/fonts/Inter-*.ttf` files at the recorded
revision contain HTML rather than valid fonts. The capture harness uses the SDK's
Roboto as the Android fallback (also registered under Inter for explicit styles),
and Linux Noto Color Emoji for emoji. This does not repair the app's font assets
and does not represent a check of iOS font fallback. The UI itself is unchanged.
Fixing the original font files belongs in a separate app change.

lœrn uses localized sample cards about the solar system. The timer starts 2:14
into a ten-minute session; the back of a flashcard, multiple-choice screen and
result screen are captured. Result dates and shuffled answer positions can vary
between runs. No claim of bit-identical output across platforms is made.

sudøku does not support Swedish or European Portuguese at the source revision.
The Swedish page uses English captures; the Portuguese page uses Brazilian
Portuguese captures. The website labels both fallbacks explicitly.

## Godot (tøwer)

Copy `tower_capture.gd` into the disposable app checkout as
`website_capture.gd`. Import the app with Godot 4.5.2 first, then use a real
renderer (headless mode uses a dummy renderer and cannot produce these images):

```sh
godot --headless --editor --import --quit
xvfb-run -a godot --rendering-method gl_compatibility --audio-driver Dummy \
  --script res://website_capture.gd
```

A normal desktop X11 display works as well. The fixture uses a separate profile,
advances the real STR-3 simulation and captures the game, airport list and VLC-1
briefing in ten languages. This fixture does not prove that the sample traffic is
a safe solution or that the shown progression was earned by a player.

## Website assets

Convert each original PNG without resizing:

```python
from PIL import Image
Image.open(source).save(destination, 'WEBP', lossless=True, method=6)
```

Put the result in `pictures/apps/<app>/<locale>/<screen>.webp`, then refresh the
manifest hashes. Check all captions and locale mappings after app UI changes.
The images are deliberately click-through links to the full-resolution asset.
