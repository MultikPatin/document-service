from collections.abc import Generator, Sequence


def as_batches[T](
    data: Sequence[T], size: int | None = None
) -> Generator[Sequence[T]]:
    length = len(data)

    middle_length = 100
    max_length = 1000

    if size is None:
        if length <= middle_length:
            s = 10
        elif length <= max_length:
            s = 50
        else:
            s = middle_length
    else:
        s = min(size, max_length)

    return (data[i : i + s] for i in range(0, length, s))
