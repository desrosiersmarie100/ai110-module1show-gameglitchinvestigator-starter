# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?

When I first ran the game, it looked okay on the surface, but the actual behavior was inconsistent. The hint system was one of the main problems because the game could give the wrong direction, which made it confusing to play. I also found input issues, since the game needed better validation for blank entries, decimals, and negative numbers. On top of that, some of the logic was all inside `app.py`, which made the code harder to debug and test.

---

## 2. How did you use AI as a teammate?

I used AI tools as a pair-programming assistant while I worked through the bugs. One helpful suggestion was separating the main game logic into `logic_utils.py`, because that made functions like `parse_guess`, `check_guess`, and `update_score` easier to test on their own. I verified those changes by running the app and by running pytest until all the tests passed.

One misleading part was that some code suggestions looked correct at first, but they were not fully reliable in the actual app. For example, I still had to manually test the game to catch the hint-direction problem and input validation issues. That reminded me that AI can help me move faster, but it cannot replace checking the real behavior of the program myself.

---

## 3. Debugging and testing your fixes

I checked my fixes in two ways: manual testing in the Streamlit app and automated testing with pytest. In the app, I used the debug panel to look at the secret number and then tested whether higher guesses said “Go LOWER,” lower guesses said “Go HIGHER,” and invalid inputs were rejected properly. That helped me confirm the gameplay was actually working the way it should.

I also ran pytest to test the logic functions directly. My tests covered difficulty ranges, input parsing, guess outcomes, and score updates. Seeing all 10 tests pass helped confirm that the fixes were not just visual but actually correct in the code.

---

## 4. What did you learn about Streamlit and state?

I learned that Streamlit reruns the script every time the user interacts with the page, which can reset values if they are not stored properly. Because of that, `st.session_state` was necessary to keep track of the secret number, attempts, score, history, difficulty, and game status. Without session state, the game would not behave consistently from one guess to the next.

The simplest way I would explain it is that Streamlit keeps reloading the app, so session state is what lets the program remember important information between reruns.

---

## 5. Looking ahead: your developer habits

One habit I want to keep is testing both the code logic and the actual app instead of assuming one passing check means everything works. In this project, pytest helped me confirm the helper functions were correct, but I still needed to run the Streamlit app to make sure the real gameplay worked. That was a good reminder that passing tests do not automatically mean the full user experience is bug-free.

Going forward, I also want to be more deliberate when using AI. AI was useful for refactoring, brainstorming fixes, and helping with tests, but I still had to verify everything step by step. This project taught me that responsible AI use means treating it like a helper, not like something I should trust automatically.