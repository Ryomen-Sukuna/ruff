__all__ = "CONST"  # [invalid-all-format]

__all__ = ["Hello"] + {"world"}  # [invalid-all-format]

__all__ += {"world"}  # [invalid-all-format]

__all__ = {"world"} + ["Hello"]  # [invalid-all-format]

__all__ = {"world"} + ["Hello"]

__all__ = ["Hello"] + {"world"}

__all__ = iter(["Hello", "world"])

__all__ = {"Hello", "world"}

__all__ = foo  # [invalid-all-format]

__all__ = foo.bar  # [invalid-all-format]

__all__ = foo["bar"]  # [invalid-all-format]

__all__ = ["Hello"]

__all__ = ("Hello",)

__all__ = ["Hello"] + ("world",)

__all__ = ["Hello", "world"]

__all__ = ["Hello", "world"]

__all__ = list({"Hello", "world"})

__all__ = ["Hello"] + ["world"]

__all__ = ("Hello", ) + ("world",)

__all__ += ["Hello"]

__all__ += multiprocessing.__all__

__all__ = list[str](["Hello", "world"])
