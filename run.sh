#!/bin/sh
# Run the JalOS demo tour (or pass a script file / single command).
# FORGE names the Jal Pari command (default: jalpari on PATH).
FORGE=${FORGE:-jalpari}
if ! command -v $FORGE >/dev/null 2>&1; then
    echo "jalpari not found. Install The Jal Pari Language first:" >&2
    echo "  https://github.com/jayantt1dubeyy/RED-MOON-" >&2
    exit 1
fi
cd -- "$(dirname -- "$0")"
$FORGE run jalos.fg "$@"
