any(x.id for x in bar)
all(x.id for x in bar)
any(x.id for x in bar)
all(x.id for x in bar)
any({x.id for x in bar})

# OK
all(x.id for x in bar)
all(x.id for x in bar)
any(x.id for x in bar)
all((x.id for x in bar))


async def f() -> bool:
    return all(await use_greeting(greeting) for greeting in await greetings())


# Special comment handling
any(i.bit_count() for i in range(5))

# Weird case where the function call, opening bracket, and comment are all
# on the same line.
any(i.bit_count() for i in range(5))
