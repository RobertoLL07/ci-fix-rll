def normalize_whitespace(s: str) -> str:
    """
    Collapse repeated whitespace and trim leading/trailing spaces.
    """
    return " ".join(s.split())


def count_words(s: str) -> int:
    """
    Count words separated by whitespace.
    """
    return len(s.split())


def title_case_sentence(s: str) -> str:
    """
    Convert a sentence to title case.
    """
    return s.title()
