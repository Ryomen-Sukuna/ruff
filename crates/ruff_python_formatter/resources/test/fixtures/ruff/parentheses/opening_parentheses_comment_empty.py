# Opening parentheses end-of-line comment without a value in the parentheses

(  # a 1
)
a2 = (  # a 2
)
a3 = f(  # a 3
)
a4 = (  # a 4
) = a4
a5: List(  # a 5
) = 5

raise (  # b 1a
)

def g():
    """Statements that are only allowed in function bodies"""
    return (  # c 1
    )
async def h():
    """Statements that are only allowed in async function bodies"""
    await (  # c 3
    )

with (  # d 1
): pass
match (  # d 2
):
    case d2:
        pass
match d3:
    case (  # d 3
    ):
        pass
while False:
    pass
try:
    pass
except (  # d 9
):
    pass


def e1(  # e 1
): pass


def e2() -> (  # e 2
): pass


class E3(  # e 3
): pass


f1 = [  # f 1
]
[  # f 2
]
f3 = {  # f3
}
{  # f 4
}
