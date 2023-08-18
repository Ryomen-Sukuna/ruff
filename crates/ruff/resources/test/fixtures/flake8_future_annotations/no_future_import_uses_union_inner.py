def main() -> None:
    a_list: list[str | None] = ["hello"]


def hello(y: dict[str | None, int]) -> None:
    z: tuple[str, str | None, str] = tuple(y)
    del z
