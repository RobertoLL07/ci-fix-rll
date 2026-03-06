from src.string_utils import normalize_whitespace, count_words, title_case_sentence
# Comment to re-rerun grade action

def test_normalize_whitespace():
    assert normalize_whitespace("  hello   coding\tagents\n101  ") == "hello coding agents 101"


def test_count_words():
    assert count_words("hello coding agents 101") == 4


def test_count_words_empty():
    assert count_words("") == 0


def test_title_case_sentence():
    assert title_case_sentence("welcome to coding agents") == "Welcome To Coding Agents"
