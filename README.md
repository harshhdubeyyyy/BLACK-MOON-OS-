# JalOS — a complete teaching OS in Jal Pari

JalOS is every subsystem a modern OS has — bootloader, kernel,
priority scheduler, virtual memory allocator, hierarchical
filesystem with permissions, users, devices, networking, a package
manager, system services, logging, and a ~30-command shell —
implemented in [The Jal Pari Language](https://github.com/jayantt1dubeyy/RED-MOON-)
and running as a single program (`jalos.fg`).

## Black Moon OS — the distro

JalOS also ships inside a real, bootable Arch-based Linux
distribution: XFCE desktop, Firefox/Chromium, GNOME Software,
installer, and Jal Pari. See [`distro/README.md`](distro/README.md)
— build it with `./distro/build.sh` on Arch Linux. (The distro is a
real Linux system; JalOS itself runs *on top of* an OS and is not a
kernel — the distinction is documented in the distro README.)

## Run it

First install Jal Pari (one time), which puts the `jalpari` command
on your PATH — see the RED-MOON- repo's install instructions. Then:

```
./run.sh                  # the built-in demo tour
jalpari run jalos.fg script.txt   # run a script file (see scripts/)
jalpari run jalos.fg ps           # a single command
```

`tests/check.sh` runs the demo tour and diffs it against
`tests/expected_output.txt` — the tour is offline and deterministic,
so it must match exactly.

## What's inside

| Subsystem | What JalOS does |
|---|---|
| Bootloader + kernel + init | Banner, RAM test, rootfs mount, daemon startup, login |
| Process management | Fixed process table, spawn, kill, ps/top |
| Scheduler | Priority scheduling in one-step quanta, tick log |
| Memory management | First-fit free-list allocator over 1024 simulated words, split + coalesce, `malloc`/`free`/`mem` |
| Filesystem | Hierarchical VFS (inodes by index), mkdir/write/cat/cp/mv/rm/ls, `/proc` pseudo-filesystem |
| Permissions + users | root/guest, file owners, owner-or-root checks, `su`, `useradd`, `/etc/passwd` |
| Devices | Console, loopback network device, disk (the VFS) |
| Networking | `ping` (loopback, simulated), `ifconfig`, `httpget` (real HTTP through the host stack) |
| Package manager | `pkg list/search/info/install/remove` — install really fetches the package source over HTTPS from the Jal Pari registry |
| Services + logging | cron (heartbeat every 5 ticks), syslog (`/var/log/syslog`), `logger`, `services` |
| Shell | ~30 commands, script files, single-command mode, `history`, `env`, `uptime`, `df`, `shutdown`, `ai`, `audit` |

## Honest limits

- **Not bootable.** Jal Pari has no pointers, inline assembly,
  interrupts, or freestanding mode, so this runs on top of a host
  OS. A bootable Jal Pari kernel would need a freestanding backend
  first — the big32 RISC-V CPU is the plausible target for that
  someday, not today.
- **No GUI.** No graphics builtins exist, so the desktop is the
  text shell.
- **No passwords worth trusting.** Passwords are compared as plain
  strings (no hashing builtin exists) — the user model demonstrates
  permissions, it does not secure anything real.
- **HTTPS needs direct internet.** `pkg install` and `httpget` over
  HTTPS fail behind HTTP proxies: the language's HTTP client does
  not speak proxy CONNECT yet. Plain HTTP works everywhere.
- **No persistence.** The VFS lives in memory; shutdown loses it.
