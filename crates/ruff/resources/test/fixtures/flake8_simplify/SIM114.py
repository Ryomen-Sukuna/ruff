# Errors
if a or c:
    b
if x in [1, 2]:
    for _ in range(20):
        print("hello")
if x in [1, 2]:
    for _ in range(20):
        print("hello")
if x in [1, 2]:
    for _ in range(20):
        print("hello")
if result.eofs in ["F", "E"]:
    errors = 1
elif result.eofs == "S":
    skipped = 1


# OK
def complicated_calc(*arg, **kwargs):
    return 42


def foo(p):
    if p == 2:
        return complicated_calc(microsecond=0)
    elif p == 3:
        return complicated_calc(microsecond=0, second=0)
    return None


a = False
b = True
c = True

if a or not b and c:
    z = 1
elif b:
    z = 2
errors = 1
if a or c:
    # Ignore branches with diverging comments because it means we're repeating
    # the bodies because we have different reasons for each branch
    x = 1


def foo():
    a = True
    b = False
    if a > b or a == b:  # end-of-line
        return 3
    elif a < b or b is None:  # end-of-line
        return 4
