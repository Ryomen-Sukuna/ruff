_ = "a" "b" "c"

_ = "abc" + "def"

_ = "abc" \
    "def"

_ = (
  "abc" +
  "def"
)

_ = ("abc" + "def")

_ = (
  b"abc" +
  b"def"
)

_ = (
  "abc"
  "def"
)

_ = 'abcdef'

_ = (
  b"abc"
  b"def"
)

_ = """a""" """b"""

_ = """a
b""" """c
d"""

_ = 'ab'

_ = 'ab'

_ = """a""" "b"

_ = 'a' "b"

_ = 'ab'

# Single-line explicit concatenation should be ignored.
_ = "abc" + "def" + "ghi"
_ = f"{foo}abcdef"
_ = f"abc{foo}def"
_ = "abc" + "def" + foo
_ = foo + bar + "abc"
_ = f"abc{foo}{bar}"
_ = f"{foo}abc{bar}"
