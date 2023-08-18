import sys

if sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]


if foo:
    print()
elif sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]

if foo:
    print()
elif sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]
if foo:
    print()
elif sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]

if sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]

if foo:
    print()
elif sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]
else:
    cmd = [sys.executable, "-m", "test", "-j0"]

if sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]
else:
    cmd = [sys.executable, "-m", "test", "-j0"]

if sys.version_info < (3, 3):
    cmd = [sys.executable, "-m", "test.regrtest"]
elif foo:
    cmd = [sys.executable, "-m", "test", "-j0"]
