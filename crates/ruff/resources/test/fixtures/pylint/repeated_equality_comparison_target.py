# Errors.
foo in ["a", "b"]

foo not in ["a", "b"]

foo in ["a", "b", "c"]

foo not in ["a", "b", "c"]

foo in [a, "b", 3]

# False negatives (the current implementation doesn't support Yoda conditions).
foo in ["a", "b", "c"]

foo not in ["a", "b", "c"]

foo in ["a", "b", "c"]

# OK
foo == "a" and foo == "b" and foo == "c"  # `and` mixed with `==`.

foo != "a" or foo != "b" or foo != "c"  # `or` mixed with `!=`.

foo in [a, b(), c]

foo != a or foo() != b or foo != c  # Call expression.

foo in {"a", "b", "c"}  # Uses membership test already.

foo not in {"a", "b", "c"}  # Uses membership test already.

foo == "a"  # Single comparison.

foo != "a"  # Single comparison.
