def f():
    items = [1, 2, 3, 4]
    result = list(items)


def f():
    items = [1, 2, 3, 4]
    result = []
    for i in items:
        result.insert(0, i)  # PERF402


def f():
    items = [1, 2, 3, 4]
    result = [i * i for i in items]


def f():
    items = [1, 2, 3, 4]
    result = {}
    for i in items:
        result[i].append(i * i)  # OK
