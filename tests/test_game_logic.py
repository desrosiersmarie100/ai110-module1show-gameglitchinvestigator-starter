from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


def test_get_range_for_difficulty():
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 100)
    assert get_range_for_difficulty("Hard") == (1, 50)


def test_parse_guess_valid_integer():
    assert parse_guess("42") == (True, 42, None)


def test_parse_guess_blank():
    assert parse_guess("") == (False, None, "Enter a guess.")


def test_parse_guess_non_numeric():
    assert parse_guess("abc") == (False, None, "That is not a number.")


def test_parse_guess_decimal_rejected():
    assert parse_guess("5.5") == (False, None, "Please enter a whole number.")


def test_check_guess_win():
    assert check_guess(10, 10) == ("Win", "🎉 Correct!")


def test_check_guess_too_high():
    assert check_guess(20, 10) == ("Too High", "📉 Go LOWER!")


def test_check_guess_too_low():
    assert check_guess(5, 10) == ("Too Low", "📈 Go HIGHER!")


def test_update_score_win():
    assert update_score(0, "Win", 1) == 100


def test_update_score_wrong_guess():
    assert update_score(50, "TooHigh" if False else "Too High", 2) == 45
    assert update_score(50, "Too Low", 2) == 45