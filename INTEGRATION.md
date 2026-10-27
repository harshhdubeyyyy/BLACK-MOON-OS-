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
- RED-MOON- live `main` currently lags its working tree (Windows
  port, deploy configs, new JalOS unpushed). Until that push lands,
  this repo's vendored JalOS is NEWER than RED-MOON- live — the
  Kaggle notebook handles this by taking the compiler from RED-MOON-
  live and `jalos.fg` from here.
