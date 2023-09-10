"""String manipulation utilities."""


def to_camel(s: str) -> str:
    """Converts a snake case string to a camel case string.

    Args:
        s: A snake case string.

    Returns:
        A camel case string.
    """
    s_l = s.lstrip("_").split("_")
    return "".join([s_l[0], *[el.capitalize() for el in s_l[1:]]])
