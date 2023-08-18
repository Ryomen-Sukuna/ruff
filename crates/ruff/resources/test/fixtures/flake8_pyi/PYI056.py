__all__ = ["A", "B", "C", "D", "E", "Foo"]

__all__.remove("A")

# OK
__all__ += ["D"]
foo = ["Hello", "World"]
foo.bar.append("World")
