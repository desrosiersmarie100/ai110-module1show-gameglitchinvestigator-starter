def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # Map difficulty levels to number ranges
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 50  # smaller range but fewer attempts makes it harder
    return 1, 100  # default fallback


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    # Reject missing input
    if raw is None:
        return False, None, "Enter a guess."

    raw = raw.strip()

    # Reject empty input
    if raw == "":
        return False, None, "Enter a guess."

    # Reject decimal values (game only allows whole numbers)
    if "." in raw:
        return False, None, "Please enter a whole number."

    try:
        value = int(raw)
    except ValueError:
        # Reject non-numeric input
        return False, None, "That is not a number."

    # Reject negative numbers or zero
    if value < 1:
        return False, None, "Please enter a positive whole number."

    return True, value, None


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Correct guess
    if guess == secret:
        return "Win", "🎉 Correct!"

    # Guess is greater than secret → user needs to go lower
    if guess > secret:
        return "Too High", "📉 Go LOWER!"

    # Guess is less than secret → user needs to go higher
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    # Winning gives points based on how quickly the user guessed
    if outcome == "Win":
        points = 100 - 10 * (attempt_number - 1)
        return current_score + max(points, 10)  # minimum 10 points

    # Wrong guesses always reduce score
    if outcome in {"Too High", "Too Low"}:
        return current_score - 5

    # Any unexpected outcome leaves score unchanged
    return current_score