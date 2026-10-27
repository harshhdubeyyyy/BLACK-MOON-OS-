#!/bin/bash
# Build the Black Moon OS ISO. Run on Arch Linux only.
#   sudo pacman -S archiso
#   ./distro/build.sh
# Output: distro/out/blackmoon-*.iso
set -e
cd -- "$(dirname -- "$0")/archiso"
command -v mkarchiso >/dev/null 2>&1 || {
    echo "mkarchiso not found. On Arch: sudo pacman -S archiso" >&2
    exit 1
}
sudo mkarchiso -v -w /tmp/blackmoon-work -o "$(pwd)/../out" .
echo "ISO built: distro/out/"
