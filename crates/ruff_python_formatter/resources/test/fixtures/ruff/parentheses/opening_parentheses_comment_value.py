# Opening parentheses end-of-line comment with value in the parentheses

(  # a 1
x)
a2 = (  # a 2
x)
a3 = f(  # a 3
x)
a4 = (  # a 4
x) = a4
a5: List(  # a 5
x) = 5

raise (  # b 1a
x)

def g():
    """Statements that are only allowed in function bodies"""
    return (  # c 1
    x)
async def h():
    """Statements that are only allowed in async function bodies"""
    await (  # c 3
    x)

with (  # d 1
x): pass
match (  # d 2
x):
    case d2:
        pass
match d3:
    case (  # d 3
    x):
        pass
while (  # d 4
x):
    pass
for (  # d 7
x) in (  # d 8
y):
    pass
try:
    pass
except (  # d 9
    x
):
    pass


def e1(  # e 1
x): pass


def e2() -> (  # e 2
x): pass


def e3() -> (
    # e 2
x): pass


def e4() -> (
    x
# e 4
): pass


def e5() -> (  # e 5
    (  # e 5
        x
    )
): pass


def e6() -> (
    (
        # e 6
        x
    )
): pass


def e7() -> (
    (
        x
        # e 7
    )
): pass


def e8() -> (
    (
        x
    )
    # e 8
): pass


class E9(  # e 9
x): pass


f1 = [  # f 1
x]
[  # f 2
x]
f3 = {  # f3
x}
{  # f 4
x}



# Non-empty parentheses: These are not allowed without a value
def f1[  # f1
    T
](): pass
f2 = iter(range(10))
f3 = list(range(10))
f4 = set(range(10))
f5 = {  # f5
    i: i**2 for i in range(10)
}


