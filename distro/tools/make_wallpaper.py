#!/usr/bin/env python3
"""Black Moon OS pixel-art generator (pure stdlib, no Pillow needed).

Draws a chunky-pixel night scene - gradient sky, blocky moon, stars,
mountain silhouettes, grid ground - and writes it as a true PNG
(IHDR/IDAT/IEND, zlib-compressed scanlines, filter 0).

Usage:
    python3 make_wallpaper.py            # 1920x1080 desktop wallpaper
    python3 make_wallpaper.py splash     # 640x480 syslinux splash

The two outputs share one scene function; only the logical grid and
the pixel scale change, so the art stays recognisably the same.
"""
import struct
import sys
import zlib


def _png(width, height, pixels):
    """pixels: list of rows, each a list of (r, g, b). Returns PNG bytes."""
    def chunk(ctype, data):
        c = struct.pack(">I", len(data)) + ctype + data
        return c + struct.pack(">I", zlib.crc32(ctype + data) & 0xFFFFFFFF)

    ihdr = struct.pack(">IIBBBBB", width, height, 8, 2, 0, 0, 0)
    raw = b"".join(b"\x00" + b"".join(bytes(px) for px in row) for row in pixels)
    return (
        b"\x89PNG\r\n\x1a\n"
        + chunk(b"IHDR", ihdr)
        + chunk(b"IDAT", zlib.compress(raw, 9))
        + chunk(b"IEND", b"")
    )


def _scene(cols, rows):
    """Return a rows x cols grid of (r, g, b) logical pixels."""
    # Deterministic star field (tiny LCG, no random module state surprises).
    seed = 1234567

    def rnd():
        nonlocal seed
        seed = (1103515245 * seed + 12345) & 0x7FFFFFFF
        return seed

    grid = []
    for y in range(rows):
        # Sky gradient: near-black navy at the top -> deep indigo at horizon.
        t = y / max(1, rows - 1)
        r = int(5 + (20 - 5) * t)
        g = int(8 + (24 - 8) * t)
        b = int(22 + (52 - 22) * t)
        grid.append([(r, g, b)] * cols)

    horizon = int(rows * 0.72)
    ground_top = int(rows * 0.86)

    # Stars (sky only, above the mountains).
    for _ in range(cols * rows // 90):
        sx, sy = rnd() % cols, rnd() % max(1, horizon - 18)
        grid[sy][sx] = (255, 244, 200) if rnd() % 4 == 0 else (220, 228, 255)

    # Blocky moon: circle in logical pixels, cream with darker craters.
    mcx, mcy, mr = int(cols * 0.76), int(rows * 0.20), max(6, cols // 11)
    for y in range(mcy - mr - 1, mcy + mr + 2):
        for x in range(mcx - mr - 1, mcx + mr + 2):
            dx, dy = x - mcx, y - mcy
            d2 = dx * dx + dy * dy
            if 0 <= y < rows and 0 <= x < cols:
                if d2 <= mr * mr:
                    grid[y][x] = (245, 233, 200)
                elif d2 <= (mr + 1) * (mr + 1):
                    grid[y][x] = (120, 130, 180)  # faint glow ring
    for cx, cy, cr in [(mcx - 4, mcy - 2, 2), (mcx + 3, mcy + 3, 2),
                       (mcx + 1, mcy - 5, 1)]:
        for y in range(cy - cr, cy + cr + 1):
            for x in range(cx - cr, cx + cr + 1):
                if 0 <= y < rows and 0 <= x < cols:
                    grid[y][x] = (214, 196, 150)

    # Mountain silhouettes: two smoothed random-walk ridges, far then near.
    def ridge(base, amp, color, seed_off):
        s = 987654 + seed_off
        h = base - amp // 2
        for x in range(cols):
            s = (1103515245 * s + 12345) & 0x7FFFFFFF
            h += (s % 5) - 2  # gentle walk: at most 2 logical pixels per column
            h = max(base - amp, min(base, h))
            for y in range(h, rows):
                if y < ground_top:
                    grid[y][x] = color

    ridge(horizon - 8, 14, (26, 30, 68), 1)    # far ridge
    ridge(horizon + 2, 10, (16, 18, 44), 2)    # near ridge

    # Ground: dark checkerboard grid, the retro pixel floor.
    for y in range(ground_top, rows):
        for x in range(cols):
            grid[y][x] = (10, 12, 26) if (x + y) % 2 == 0 else (22, 27, 52)
    return grid


def render(out_path, width, height, scale):
    cols, rows = width // scale, height // scale
    logical = _scene(cols, rows)
    pixels = []
    for ly in range(rows):
        expanded = []
        for lx in range(cols):
            expanded.extend([logical[ly][lx]] * scale)
        for _ in range(scale):
            pixels.append(list(expanded))
    data = _png(width, height, pixels)
    with open(out_path, "wb") as f:
        f.write(data)
    print(f"wrote {out_path} ({width}x{height}, {len(data)} bytes)")


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "splash":
        render("splash.png", 640, 480, 4)
    else:
        render("blackmoon-pixel.png", 1920, 1080, 12)
