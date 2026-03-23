# 🎮 Game Glitch Investigator

## Project Overview
This project involved debugging and repairing an AI-generated number guessing game built with Streamlit. The original version had several logic and state issues that made the game unreliable. The goal was to identify the bugs, fix them, refactor the game logic into helper functions, and verify the repairs with pytest.

## Bugs Found
- The game logic was mixed directly into `app.py`, which made it harder to test.
- The hint logic was incorrect in the original version.
- Input handling was unreliable for blank input, decimals, and non-numeric values.
- Score updates were inconsistent.
- Streamlit session state needed to be handled correctly so the game would behave consistently.

## Fixes Applied
- Refactored helper functions into `logic_utils.py`
- Fixed guess checking so the hints match the actual secret number
- Improved input validation for blank, decimal, and invalid entries
- Corrected score calculation logic
- Used `st.session_state` to properly manage attempts, score, history, difficulty, and game status

## Files
- `app.py` — Streamlit interface and main game flow
- `logic_utils.py` — helper functions for difficulty, parsing, guess checking, and scoring
- `tests/test_game_logic.py` — pytest tests for game logic
- `reflection.md` — project reflection

## How to Run
Install dependencies:

```bash
pip install -r requirements.txt