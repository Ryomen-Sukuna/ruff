x = set(range(3))
x = set(range(3))
y = f"{{a if a < 6 else 0 for a in range(3)}}"
_ = f"{{a if a < 6 else 0 for a in range(3)}}"
print(f"Hello {set(range(3))} World")


def f(x):
    return x


print(f'Hello {set("abc")} World')
print(f"Hello {set('abc')} World")
print(f"Hello {{f(a) for a in 'abc'}} World")
print(f"{set('abc') - set('ab')}")
print(f"{set('abc') - set('ab')}")

# The fix generated for this diagnostic is incorrect, as we add additional space
# around the set comprehension.
print(f"{{set('abc')}}")
