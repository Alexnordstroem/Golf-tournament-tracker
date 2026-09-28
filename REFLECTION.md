# Project Reflection

## Project goal

The Golf Tournament Tracker was created to provide a simple way to record tournament names and scores. Its main page brings the entry form and saved tournament history together, making it easy to add a round and review previous results.

## What the project does

The app uses Flask to receive form submissions and render the tournament list. It validates that each score is a whole number from 1 to 300, records the date an entry is added, and saves tournament data locally in a JSON file. The list shows the newest entries first, includes a combined score, and provides a delete button for removing an entry.

## What I learned

This project demonstrates how a web form connects to Python code: the browser sends the tournament details, Flask checks the values, and the page displays the updated data. It also shows how a JSON file can provide simple local persistence without setting up a database. Keeping the HTML, CSS, and Python in separate files makes each part of the app easier to understand and change.

## Challenges and decisions

A key decision was to store the tournament data in a JSON file. This keeps the app approachable for a small personal project, while allowing entries to remain available after the server stops. The app also calculates the total from the saved entries each time the page loads, so the total stays in sync when a tournament is added or deleted.

## Possible improvements

- Add the ability to edit a tournament after saving it.
- Use a database such as SQLite if the app grows or needs more robust data handling.
- Add filters or summaries, such as average score or results by year.
- Add automated tests for score validation, saving, and deleting tournaments.

## Conclusion

The tracker is a useful starting point for a small Flask application. It combines a form, server-side validation, local data storage, and a responsive interface while keeping the codebase small enough to explore and extend.
