# Integration: BLACK-MOON-OS- × RED-MOON-

Mirror note from the distro side. The full contract lives in
RED-MOON-'s `docs/INTEGRATION.md`; this file records what this repo
takes from RED-MOON- and what is verified.

## What this repo vendors from RED-MOON-

- `jalos.fg` (repo root) and
  `distro/archiso/airootfs/usr/share/blackmoon/jalos.fg` are
  byte-identical copies of RED-MOON-'s `examples/os/jalos.fg`.
  RED-MOON- owns JalOS; this repo vendors it. Do not edit these
  copies here — change JalOS in RED-MOON- and re-sync.
- Current vendored version: 1408 lines, with `ai` (perceptron) and
  `audit` commands. Minimum compiler: RED-MOON- v1.1.0 (JalOS needs
  arrays of structs, `break`, string indexing).

## What this repo owns

The archiso distro profile (`distro/`): XFCE + LightDM, the
retro-pixel + macOS-glass theme (picom, plank, terminus-font, pixel
wallpaper), local-AI packages and `blackmoon-ai`, the cybersecurity
toolkit and `blackmoon-sec`, and the `blackmoon-install` guided
installer (which installs RED-MOON- into the target system via its
`scripts/install.sh`).

## Verified combinations

| RED-MOON- | This repo | Verified | How |
|---|---|---|---|
| v1.1.0 (`d56a903`) | `6fab40f` | 27 Oct 2026 | Kaggle kernel v1 COMPLETE; log shows demo, `ai`, `audit` |
| working tree post-1.1.0 | `6fab40f` | 27 Oct 2026 | All 3 `jalos.fg` copies byte-identical; demo 254 lines identical |
| `627904d` | `8fa46c2` | 27 Oct 2026 | Fresh public clones of both repos: full native suite PASS + sync check 9/9 |
| `6a92164f` | `a98cddb` | 27 Oct 2026 | Kaggle kernel v2 COMPLETE; log shows demo, `ai`, `audit`; clones used contain the proxy code |

## How to re-sync (after a JalOS change in RED-MOON-)

1. Copy RED-MOON-'s `examples/os/jalos.fg` over both copies here.
2. Run RED-MOON-'s check from its checkout:
   `python3 tools/check_jalos_sync.py --blackmoon <this directory>`.
3. Push this repo (`scripts/push_jalos.py`) — only on the owner's
   explicit word; pushes are external publication.

## Known limits

- The ISO is unbuilt/unbooted (needs an Arch builder); theme,
  AI/sec launchers, and installer theme-copying are untested until
  first boot.
- No code drift at present: RED-MOON- live now contains the same
  JalOS as this repo (drift closed 27 Oct 2026). Verification gap
  CLOSED 27 Oct 2026: Kaggle kernel v2 ran the current code refs
  to COMPLETE (see matrix).
