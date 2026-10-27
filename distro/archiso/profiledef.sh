#!/usr/bin/env bash
# Black Moon OS archiso profile.
# Build ONLY on Arch Linux: sudo pacman -S archiso, then see ../build.sh.
# This file is read by mkarchiso; it is NOT executed as a script.
# shellcheck disable=SC2034
iso_name="blackmoon"
iso_label="BLACKMOON_$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y%m)"
iso_publisher="Black Moon OS <https://github.com/jayantt1dubeyy/BLACK-MOON-OS->"
iso_application="Black Moon OS live/iso"
iso_version="$(date --date="@${SOURCE_DATE_EPOCH:-$(date +%s)}" +%Y.%m.%d)"
install_dir="blackmoon"
buildmodes=('iso')
bootmodes=('bios.syslinux.mbr' 'bios.syslinux.eltorito' 'uefi-ia32.grub.esp' 'uefi-x64.grub.esp' 'uefi-ia32.grub.eltorito' 'uefi-x64.grub.eltorito')
arch="x86_64"
pacman_conf="pacman.conf"
airootfs_image_type="squashfs"
airootfs_image_tool_options=('-comp' 'xz' '-Xbcj' 'x86' '-b' '1M' '-Xdict-size' '1M')
# Modes applied to airootfs files at build time (git modes do not matter).
file_permissions=(
  ["/usr/local/bin/blackmoon-install"]="0:0:755"
  ["/usr/local/bin/blackmoon-install-jalpari"]="0:0:755"
  ["/usr/local/bin/blackmoon-jalos"]="0:0:755"
  ["/usr/local/bin/blackmoon-welcome"]="0:0:755"
  ["/usr/local/bin/blackmoon-ai"]="0:0:755"
  ["/usr/local/bin/blackmoon-sec"]="0:0:755"
  ["/usr/local/bin/blackmoon-blackarch"]="0:0:755"
  ["/usr/local/bin/blackmoon-mac"]="0:0:755"
  ["/usr/local/bin/blackmoon-notes"]="0:0:755"
  ["/usr/local/bin/blackmoon-gallery"]="0:0:755"
  ["/usr/local/bin/blackmoon-browser"]="0:0:755"
  ["/usr/local/bin/blackmoon-code"]="0:0:755"
  ["/usr/local/bin/blackmoon-wallpaper"]="0:0:755"
)
