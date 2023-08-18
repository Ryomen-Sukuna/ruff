"""Case: `contextlib` already imported."""
import contextlib


def foo():
    pass


# SIM105
with contextlib.suppress(ValueError):
    foo()
