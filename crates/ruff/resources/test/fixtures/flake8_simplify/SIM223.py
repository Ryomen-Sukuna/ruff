if a and f() and b and g() and False:  # OK
    pass

if a and f() and False and g() and b:  # SIM223
    pass

if False and f() and a and g() and b:  # SIM223
    pass

if a and False and f() and b and g():  # SIM223
    pass


if a or f() or b or g() or True:  # OK
    pass

if a or f() or True or g() or b:  # OK
    pass

if True or f() or a or g() or b:  # OK
    pass

if a or True or f() or b or g():  # OK
    pass


a and "" and False  # SIM223

a and "foo" and False and "bar"  # SIM223

a and 0 and False  # SIM223

a and 1 and False and 2  # SIM223

a and 0.0 and False  # SIM223

a and 0.1 and False and 0.2  # SIM223

a and [] and False  # SIM223

a and [] and False

a and [1] and False and [2]  # SIM223

a and [1] and False and [2]

a and {} and False  # SIM223

a and {} and False

a and {1: 1} and False and {2: 2}  # SIM223

a and dict({1: 1}) and False and dict({2: 2})  # SIM223

a and set() and False  # SIM223

a and set(set()) and False  # SIM223

a and {1} and False and {2}  # SIM223

a and {1} and False and {2}

a and () and False  # SIM222

a and () and False

a and (1,) and False and (2,)  # SIM222

a and (1, ) and False and (2, )

a and frozenset() and False  # SIM222

a and frozenset(frozenset()) and False  # SIM222

a and frozenset({1}) and False and frozenset({2})  # SIM222

a and frozenset(frozenset({1})) and False and frozenset(frozenset({2}))  # SIM222


# Inside test `a` is simplified.

bool(a and [] and False and [])  # SIM223

assert False

0 if False else 1

while False:  # SIM223
    pass

[
    0
    for a in range(10)
    for b in range(10)
    if a and [] and False and []  # SIM223
    if b and [] and False and []  # SIM223
]

{
    0
    for a in range(10)
    for b in range(10)
    if a and [] and False and []  # SIM223
    if b and [] and False and []  # SIM223
}

{
    0: 0
    for a in range(10)
    for b in range(10)
    if a and [] and False and []  # SIM223
    if b and [] and False and []  # SIM223
}

(
    0
    for a in range(10)
    for b in range(10)
    if a and [] and False and []  # SIM223
    if b and [] and False and []  # SIM223
)

# Outside test `a` is not simplified.

a and [] and False and []  # SIM223

if f(a and [] and False and []):  # SIM223
    pass
