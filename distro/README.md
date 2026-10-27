# Black Moon OS — the distro

Black Moon OS is an Arch-based Linux distribution: Arch's rolling
packages, the XFCE desktop, and JalOS (the teaching OS in Jal Pari)
built in. This directory holds everything needed to build its ISO.

## What is what (do not confuse the two layers)

- **Black Moon OS (this distro)** is a real, bootable Linux system:
  Arch base + XFCE + LightDM + apps. It is built with archiso.
- **JalOS (`../jalos.fg`)** is a teaching OS written in Jal Pari. It
  runs *on top of* an OS (including this one) — it is not a kernel
  and cannot boot hardware. In the distro it ships as an app:
  click "JalOS" on the desktop, or run `blackmoon-jalos`.

## What is inside the ISO

- **CLI:** full Arch CLI — `pacman`, `systemd`, `bash`, `blackmoon-install`
- **GUI:** XFCE desktop + LightDM login (live session autologs in as
  root; installed systems log in as the user you create)
- **Apps:** Firefox + Chromium (browse), GNOME Software + Flatpak
  (browse and install apps graphically), LibreOffice, VLC, mpv,
  GIMP, Inkscape, Evince, Mousepad, and the usual tools
- **Jal Pari:** installed on demand by `blackmoon-install-jalpari`
  (the JalOS desktop icon does this automatically on first run)
- **Installer:** `blackmoon-install` — guided, UEFI + BIOS, destroys
  the target disk, creates a real user with sudo

## Build the ISO (on Arch Linux only)

```
sudo pacman -S archiso
./distro/build.sh
# -> distro/out/blackmoon-*.iso
```

The ISO cannot be built on Debian/Ubuntu or in this sandbox: mkarchiso
needs pacman and Arch's repos. A GitHub Actions workflow that builds
the ISO on a runner is a planned next step (it needs a token with
workflow scope to land here).

## Test it (QEMU)

```
qemu-system-x86_64 -cdrom distro/out/blackmoon-*.iso -m 4096 -enable-kvm -boot d
```

Or write it to a USB stick (destroys the stick's contents):

```
sudo dd if=distro/out/blackmoon-*.iso of=/dev/sdX bs=4M status=progress oflag=sync
```

## Install it

Boot the ISO, open a terminal, run `blackmoon-install`, follow the
prompts, reboot. After first boot: `sudo pacman -Syu`, and
`blackmoon-jalos` for the teaching OS.

## Honest status (read before trusting a build)

- **Profile written, ISO NOT built or booted yet.** The profile
  (package list, bootloader configs, live customizations) is
  complete on paper, but no ISO has been produced from it: this
  workspace is Ubuntu without mkarchiso/pacman, so the first build
  must happen on an Arch machine or runner, and the first boot must
  be tested in a VM.
- **Installer is BETA and untested** — test in a VM before any real
  disk. It wipes its target disk by design.
- **Live session runs as root** (standard for live images, and the
  installed system does not). If the graphical login ever fails to
  appear, the console is still root-autologin: run `startxfce4`.
- **Package list uses official Arch repos only.** AUR packages
  (e.g. pamac, VS Code) are intentionally left out; install them
  after first boot with an AUR helper if you want them.
