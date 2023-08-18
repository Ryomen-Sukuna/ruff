def f():
    items = [1, 2, 3, 4]
    result = [i for i in items if i % 2]


def f():
    items = [1, 2, 3, 4]
    result = [i * i for i in items]


def f():
    items = [1, 2, 3, 4]
    result = list(items)


def f():
    items = [1, 2, 3, 4]
    result = list(items)


def f():
    items = [1, 2, 3, 4]
    result = {}
    for i in items:
        result[i].append(i)  # OK


def f():
    items = [1, 2, 3, 4]
    result = []
    for i in items:
        if i not in result:
            result.append(i)  # OK


def f():
    fibonacci = [0, 1]
    fibonacci.extend(sum(fibonacci[-2:]) for _ in range(20))
    print(fibonacci)


def f():
    foo = object()
    foo.fibonacci = [0, 1]
    foo.fibonacci.extend(sum(foo.fibonacci[-2:]) for _ in range(20))
    print(foo.fibonacci)
