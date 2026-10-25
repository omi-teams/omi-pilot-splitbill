"""Pure split logic."""


def split_equal(amount: int, people: int) -> list[int]:
    """Split amount among people; the remainder goes +1 each to the first people."""
    base, extra = divmod(amount, people)
    return [base + (i < extra) for i in range(people)]
