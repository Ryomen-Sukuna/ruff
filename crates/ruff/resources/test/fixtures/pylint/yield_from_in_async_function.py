async def success():
    yield 42


async def fail():
    yield from (1, 2, 3)
