"""Port the three native splash timelines onto their original SVG artwork.

Run from any directory: python tools/branding/generate.py
No runtime dependencies, font downloads, or app engines are needed on the site.
"""
from pathlib import Path
import math
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[2]
NS = "http://www.w3.org/2000/svg"
ET.register_namespace("", NS)


def element(tag, **attrs):
    return ET.Element(f"{{{NS}}}{tag}", {k.replace('_', '-'): str(v) for k, v in attrs.items()})


def clamp(x):
    return max(0, min(1, x))


def keyframes(name, frames):
    return "@keyframes " + name + "{" + "".join(
        f"{i / (len(frames) - 1) * 100:.4f}%{{{frame}}}" for i, frame in enumerate(frames)
        if i in (0, len(frames) - 1) or frames[i - 1] != frame or frames[i + 1] != frame
    ) + "}"


def generate(app):
    svg = ET.parse(ROOT / f"tools/branding/sources/{app}.svg").getroot()
    # Source titles are optional; these images are decorative beside app names.
    for child in list(svg):
        if child.tag == f"{{{NS}}}title":
            svg.remove(child)
    rules, animations = [], []
    times = [i * 3.3 / 165 for i in range(166)]

    if app == "loern":
        nodes = [(440, 300), (507, 263), (581, 249), (669, 245), (754, 274), (531, 420), (714, 442)]
        # Insert impulses before the wordmark, matching BrandScenePainter.
        insert_at = next(i for i, c in enumerate(svg) if c.get("id") == "wordmark")
        impulses = element("g")
        for i, (x, y) in enumerate(nodes):
            for suffix, radius, growth, strength in [("halo", 12, 17, .12), ("core", 5, 5, .9)]:
                name = f"pulse-{i}-{suffix}"
                impulses.append(element("circle", cx=x, cy=y, r=radius, fill="#c9ac73", opacity=0, id=name))
                rules.append(f"#{name}{{transform-origin:{x}px {y}px;animation:{name} 3.3s linear both}}")
                frames = []
                for t in times:
                    progress = clamp((t - (.6 + i * .23)) / .65)
                    pulse = math.sin(math.pi * progress) ** 2
                    frames.append(f"opacity:{pulse * strength:.5f};transform:scale({1 + pulse * growth / radius:.5f})")
                animations.append(keyframes(name, frames))
        svg.insert(insert_at, impulses)

    elif app == "sudoku":
        motif = svg.find(f"{{{NS}}}g")
        motif.set("id", "grid")
        # The source consists of a grid, then five [pulse, cell, digit] groups.
        cells = list(motif)[9:]
        assert len(cells) == 15, "Sudoku artwork structure changed; review the port"
        for i in range(5):
            pulse, cell, digit = cells[i * 3:i * 3 + 3]
            for node, suffix in [(pulse, "pulse"), (cell, "cell"), (digit, "digit")]:
                name = f"cell-{i}-{suffix}"
                node.set("id", name)
                rules.append(f"#{name}{{animation:{name} 3.3s linear both}}")
                frames = []
                for t in times:
                    p = clamp((t - (.6 + i * .35)) / .45)
                    opacity = {"pulse": math.sin(math.pi * p) ** 2 * .66, "cell": p * .85, "digit": p * p * (3 - 2 * p)}[suffix]
                    frames.append(f"opacity:{opacity:.5f}")
                animations.append(keyframes(name, frames))
        fading = list(svg)[1:]
        # Fade the entire artwork, as the native splash does; background stays.
        for i, node in enumerate(fading):
            name = f"fade-{i}"
            node.set("class", name)
            rules.append(f".{name}{{animation:fade-in .35s linear both}}")
        animations.append("@keyframes fade-in{from{opacity:0}to{opacity:1}}")

    else:
        backdrop = svg.find(".//*[@id='tower-background']")
        rules.append("#tower-background{animation:tower 3.3s linear both}")
        frames = []
        for t in times:
            p = clamp((t - 2.25) / .5)
            eased = p * p * (3 - 2 * p)
            frames.append(f"opacity:{eased:.5f};transform:translateY({12 * (1 - eased):.5f}px)")
        animations.append(keyframes("tower", frames))
        letters = element("g", id="letters")
        for path in list(svg):
            if path.get("fill") == "#f0eadb":
                svg.remove(path)
                letters.append(path)
        svg.insert(list(svg).index(backdrop) + 1, letters)
        rules.append("#letters{animation:fade-in .35s linear both}")
        animations.append("@keyframes fade-in{from{opacity:0}to{opacity:1}}")
        slash = list(svg)[-1]
        assert slash.get("stroke") == "#c9ac73"
        slash.set("id", "slash")
        a, b = (272.8, 612.0167), (403.59, 446.65)
        length = math.dist(a, b)
        dx, dy = (b[0] - a[0]) / length, (b[1] - a[1]) / length
        angle = math.degrees(math.atan2(dy, dx))
        plane = element("g", id="plane", opacity=0, stroke="#c9ac73", fill="none")
        plane.append(element("path", d="M-9 0H11M-2 -8V8", stroke_width=2.5))
        plane.append(element("path", d="M-7 -3V3", stroke_width=2))
        svg.append(plane)
        rules.append(f"#slash{{stroke-dasharray:{length:.5f};animation:slash 3.3s linear both}}")
        rules.append("#plane{animation:flight 3.3s linear both}")
        flight_frames, slash_frames = [], []
        for t in times:
            f = clamp((t - .6) / 1.65)
            distance = -100 / .541 + f * (length + 200 / .541)
            reveal = clamp((distance - 11 / .541) / length)
            opacity = clamp(min(f / .1, (1 - f) / .14)) if .6 <= t < 2.25 else 0
            x, y = a[0] + dx * distance, a[1] + dy * distance
            flight_frames.append(f"opacity:{opacity:.5f};transform:translate({x:.5f}px,{y:.5f}px) rotate({angle:.5f}deg) scale({1.1 / .541:.5f})")
            slash_frames.append(f"stroke-dashoffset:{length * (1 - reveal):.5f}")
        animations += [keyframes("flight", flight_frames), keyframes("slash", slash_frames)]

    # Static artwork is the default, including unsupported CSS and reduced motion.
    style = element("style")
    style.text = "@media (prefers-reduced-motion:no-preference){" + "".join(rules + animations) + "}"
    svg.insert(0, style)
    destination = ROOT / f"pictures/brand/{app}-splash.svg"
    ET.ElementTree(svg).write(destination, encoding="utf-8", xml_declaration=False)
    print(f"{destination.relative_to(ROOT)}: {destination.stat().st_size} bytes")


if __name__ == "__main__":
    for app in ["loern", "sudoku", "tower"]:
        generate(app)
