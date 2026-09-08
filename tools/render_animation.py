from __future__ import annotations

import math
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "media"
FRAMES = OUT / "animation_frames"


W, H = 1280, 720
SCALE = 8.0
CX, CY = 640, 350
PHASES = ["A", "B", "C", "A", "B", "C"]
COIL_CENTERS = [-20, -12, -4, 4, 12, 20]
POLE_CENTERS = [-36, -24, -12, 0, 12, 24, 36]
MAGNET_CENTERS = [-42, -37, -30, -25, -18, -13, -6, -1, 6, 11, 18, 23, 30, 35, 42, 47]


def mm_to_x(mm: float, camera: float = 0.0) -> float:
    return CX + (mm - camera) * SCALE


def z_to_y(radius_mm: float, depth: float = 0.0) -> float:
    return CY - radius_mm * SCALE * 0.72 + depth


def rounded_rect(draw: ImageDraw.ImageDraw, box, radius, fill, outline=None, width=1):
    draw.rounded_rectangle(box, radius=radius, fill=fill, outline=outline, width=width)


def cyl(draw: ImageDraw.ImageDraw, x0, x1, radius, fill, outline, yoff=0, alpha=255):
    y0 = CY - radius * SCALE * 0.72 + yoff
    y1 = CY + radius * SCALE * 0.72 + yoff
    color = fill + (alpha,)
    edge = outline + (min(alpha + 20, 255),)
    draw.rectangle((x0, y0, x1, y1), fill=color, outline=edge)
    draw.ellipse((x0 - 6, y0, x0 + 6, y1), fill=color, outline=edge)
    draw.ellipse((x1 - 6, y0, x1 + 6, y1), fill=color, outline=edge)
    draw.line((x0, y0 + 3, x1, y0 + 3), fill=(255, 255, 255, 70), width=2)


def draw_shadow(base: Image.Image):
    layer = Image.new("RGBA", base.size, (0, 0, 0, 0))
    d = ImageDraw.Draw(layer, "RGBA")
    d.ellipse((260, 540, 1020, 630), fill=(0, 0, 0, 70))
    base.alpha_composite(layer.filter(ImageFilter.GaussianBlur(18)))


def draw_fixed_stack(draw: ImageDraw.ImageDraw):
    cyl(draw, mm_to_x(-47), mm_to_x(47), 6.0, (42, 47, 51), (80, 88, 96), alpha=145)
    cyl(draw, mm_to_x(-47), mm_to_x(47), 5.1, (16, 18, 20), (110, 116, 122), alpha=90)

    for i, c in enumerate(MAGNET_CENTERS):
        x0, x1 = mm_to_x(c - 2.5), mm_to_x(c + 2.5)
        fill = (206, 69, 67) if (i // 2) % 2 == 0 else (61, 121, 201)
        cyl(draw, x0, x1, 5.0, fill, (235, 235, 235), yoff=0, alpha=210)

    for c in POLE_CENTERS:
        x0, x1 = mm_to_x(c - 1), mm_to_x(c + 1)
        cyl(draw, x0, x1, 5.0, (190, 196, 202), (235, 235, 235), yoff=0, alpha=240)


def draw_bobbin(draw: ImageDraw.ImageDraw, travel: float):
    bob_x0, bob_x1 = mm_to_x(-22.5 + travel), mm_to_x(22.5 + travel)
    cyl(draw, bob_x0, bob_x1, 6.7, (238, 231, 216), (120, 113, 100), yoff=13, alpha=245)
    for c in [-20, -12, -4, 4, 12, 20]:
        x = mm_to_x(c + travel)
        cyl(draw, x - 2, x + 2, 8.4, (238, 231, 216), (120, 113, 100), yoff=13, alpha=250)

    phase_colors = {
        "A": (190, 85, 31),
        "B": (216, 132, 38),
        "C": (157, 67, 28),
    }
    for c, phase in zip(COIL_CENTERS, PHASES):
        x0, x1 = mm_to_x(c - 2 + travel), mm_to_x(c + 2 + travel)
        cyl(draw, x0, x1, 8.4, phase_colors[phase], (91, 39, 20), yoff=13, alpha=252)
        for k in range(5):
            x = x0 + (k + 0.5) * (x1 - x0) / 5
            draw.arc((x - 12, CY - 48 + 13, x + 12, CY + 48 + 13), 90, 270, fill=(255, 196, 95, 95), width=2)
        draw.text((x0 + 8, CY + 86), phase, fill=(235, 235, 235), anchor="mm")

    for c in [-22.5, 22.5]:
        x = mm_to_x(c + travel)
        cyl(draw, x - 2, x + 2, 8.4, (238, 231, 216), (120, 113, 100), yoff=13, alpha=245)


def draw_scale(draw: ImageDraw.ImageDraw, font, travel: float):
    y = 612
    x0, x1 = mm_to_x(-20), mm_to_x(20)
    draw.line((x0, y, x1, y), fill=(210, 216, 222), width=3)
    for t in [-20, 0, 20]:
        x = mm_to_x(t)
        draw.line((x, y - 9, x, y + 9), fill=(210, 216, 222), width=2)
        draw.text((x, y + 22), f"{t:+d} mm", fill=(210, 216, 222), font=font, anchor="mm")
    draw.ellipse((mm_to_x(travel) - 7, y - 7, mm_to_x(travel) + 7, y + 7), fill=(246, 190, 77))
    draw.text((W // 2, 62), "Rev64 tubular linear motor - moving six-coil bobbin inside fixed magnet/pole stack", fill=(245, 247, 250), font=font, anchor="mm")
    draw.text((W // 2, 98), "Illustrative render from recovered CAD dimensions; guides, mounting, end retention and wiring exits remain to be designed", fill=(180, 188, 196), font=font, anchor="mm")


def render_frame(i: int, n: int, font) -> Image.Image:
    t = i / n
    travel = 20.0 * math.sin(2 * math.pi * t)
    img = Image.new("RGBA", (W, H), (18, 21, 25, 255))
    bg = ImageDraw.Draw(img, "RGBA")
    for y in range(H):
        shade = int(18 + 28 * y / H)
        bg.line((0, y, W, y), fill=(shade, shade + 3, shade + 6, 255))
    draw_shadow(img)
    draw = ImageDraw.Draw(img, "RGBA")
    draw_fixed_stack(draw)
    draw_bobbin(draw, travel)
    draw_scale(draw, font, travel)
    return img.convert("P", palette=Image.Palette.ADAPTIVE, colors=128)


def main() -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    FRAMES.mkdir(parents=True, exist_ok=True)
    try:
        font = ImageFont.truetype("arial.ttf", 22)
    except OSError:
        font = ImageFont.load_default()
    frames = [render_frame(i, 90, font) for i in range(90)]
    for idx, frame in enumerate(frames):
        frame.convert("RGBA").save(FRAMES / f"rev64_animation_{idx:03d}.png")
    gif_path = OUT / "rev64_real_life_motion.gif"
    frames[0].save(
        gif_path,
        save_all=True,
        append_images=frames[1:],
        duration=40,
        loop=0,
        optimize=True,
    )
    poster = frames[12].convert("RGBA")
    poster.save(OUT / "rev64_animation_preview.png")
    print(gif_path)


if __name__ == "__main__":
    main()
