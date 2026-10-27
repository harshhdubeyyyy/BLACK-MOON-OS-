#!/bin/sh
# Regression check: the demo tour is offline and deterministic, so its
# output must match tests/expected_output.txt exactly.
# FORGE names the Jal Pari command (default: jalpari on PATH).
FORGE=${FORGE:-jalpari}
cd -- "$(dirname -- "$0")/.."
$FORGE run jalos.fg > /tmp/jalos_check_out.txt 2>&1
rc=$?
if [ $rc -ne 0 ]; then
    echo "check FAILED: jalos.fg exited $rc" >&2
    cat /tmp/jalos_check_out.txt >&2
    exit 1
fi
if diff -u tests/expected_output.txt /tmp/jalos_check_out.txt; then
    echo "check PASSED: demo output matches"
else
    echo "check FAILED: output differs" >&2
    exit 1
fi
