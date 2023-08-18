# Errors

for item in {"apples", "lemons", "water"}:  # flags in-line set literals
    print(f"I like {item}.")

numbers_list = list({1, 2, 3})

numbers_set = {1, 2, 3}

numbers_dict = {str(i): i for i in {1, 2, 3}}  # flags sets in dict comprehensions

numbers_gen = iter({1, 2, 3})

# Non-errors

items = {"apples", "lemons", "water"}
for item in items:  # only complains about in-line sets (as per Pylint)
    print(f"I like {item}.")

for item in ["apples", "lemons", "water"]:  # lists are fine
    print(f"I like {item}.")

for item in ("apples", "lemons", "water"):  # tuples are fine
    print(f"I like {item}.")

numbers_list = [1, 2, 3]

numbers_set = {1, 2, 3}

numbers_dict = {str(i): i for i in [1, 2, 3]}  # lists in dict comprehensions are fine

numbers_gen = iter((1, 2, 3))

for item in {"apples", "lemons", "water"}:  # set constructor is fine
    print(f"I like {item}.")

for number in set(range(10)):  # set comprehensions are fine
    print(number)

for item in {*numbers_set, 4, 5, 6}:  # set unpacking is fine
    print(f"I like {item}.")
