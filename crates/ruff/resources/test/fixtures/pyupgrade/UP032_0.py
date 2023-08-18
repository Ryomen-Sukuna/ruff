###
# Errors
###

f"{a} {b}"

"{1} {0}".format(a, b)

"{0} {1} {0}".format(a, b)

"{x.y}".format(x=z)

"{x} {y} {x}".format(x=a, y=b)

"{.x} {.y}".format(a, b)

f"{a.b} {c.d}"

f"{a()}"

f"{a.b()}"

f"{a.b().c()}"

f"hello {name}!"

"{}{b}{}".format(a, c, b=b)

'0'

f"{a} {b}"

f"""{a} {b}"""

'foo1'

'foo1'

x = "{a}".format(a=1)

print(f"foo {x} ")

"{a[b]}".format(a=a)

"{a.a[b]}".format(a=a)

"{}{{}}{}".format(escaped, y)

f"{a}"

'({}={{0!e}})'.format(a)

"{[b]}".format(a)

'{[b]}'.format(a)

"""{[b]}""".format(a)

'''{[b]}'''.format(a)

'1'

'123456789 1111111111111111111111111111111111111111111111111111111111111111111111111'

"""
{}
""".format(1)

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa = """
{}
""".format(
    111111
)

"{a}" "{b}".format(a=1, b=1)

(
    "{a}"
    "{b}"
).format(a=1, b=1)

(
    "{a}"
    ""
    "{b}"
    ""
).format(a=1, b=1)

(
    (
        # comment
        "{a}"
        # comment
        "{b}"
    )
    # comment
    .format(a=1, b=1)
)

(
    "{a}"
    "b"
).format(a=1)


def d(osname, version, release):
    return f"{osname}-{version}.{release}"


def e():
    yield '1'


assert '1'


async def c():
    return f"{await 3}"


async def c():
    return "{}".format(1 + await 3)


f"{1 * 2}"

###
# Non-errors
###

# False-negative: RustPython doesn't parse the `\N{snowman}`.
"\N{snowman} {}".format(a)

"{".format(a)

"}".format(a)

"{} {}".format(*a)

"{x} {x}".format(arg)

"{x.y} {x.z}".format(arg)

b"{} {}".format(a, b)

"{:{}}".format(x, y)

"{}{}".format(a)

"" "{}".format(a["\\"])

f'{a["b"]}'

r'"\N{snowman} {}".format(a)'

'123456789 11111111111111111111111111111111111111111111111111111111111111111111111111'

"""
{}
{}
{}
""".format(
1,
2,
111111111111111111111111111111111111111111111111111111111111111111111111111111111111111,
)

aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa = """{}
""".format(
    111111
)

"{}".format(
    [
        1,
        2,
        3,
    ]
)

"{a}".format(
    a=[
        1,
        2,
        3,
    ]
)

(
    "{a}"
    "{1 + 2}"
).format(a=1)

"{}".format(**c)

'1'
