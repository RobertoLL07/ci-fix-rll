from src.string_utils import normalize_whitespace, count_words, title_case_sentence


def test_normalize_whitespace():
    assert normalize_whitespace("  hello   world\tfrom\npython  ") == "hello world from python"


def test_count_words():
    assert count_words("hello world from python") == 4


def test_count_words_empty():
    assert count_words("") == 0


def test_title_case_sentence():
    assert title_case_sentence("welcome to string utilities") == "Welcome To String Utilities"
