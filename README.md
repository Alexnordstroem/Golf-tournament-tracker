# Golf Tournament Tracker

A lightweight web app for keeping a personal record of golf tournaments. Add tournament names and scores, review your round history, see your combined score, and remove entries you no longer need.

## Features

- Record a tournament name and whole-number score from 1 to 300.
- Automatically save the date the entry is added.
- Display the newest tournaments first.
- Calculate the combined score of all saved tournaments.
- Delete individual tournaments from the list.
- Save entries locally between app restarts.
- Use a responsive layout on desktop and mobile screens.

## Technologies

- **Python** runs the application logic.
- **Flask** handles web requests and serves the pages.
- **HTML and Jinja templates** provide the form and tournament list.
- **CSS** styles the responsive interface.
- **JSON** stores tournament data locally.

## Requirements

- Python 3.10 or newer
- `pip`, included with most Python installations

## Installation and run

Open PowerShell in the project folder. Create a virtual environment, activate it, install Flask, and start the app:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
py -m pip install -r requirements.txt
py app.py
```

If PowerShell prevents virtual environment activation, skip the activation command and use the environment's Python directly:

```powershell
py -m venv .venv
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python app.py
```

When the server starts, visit <http://127.0.0.1:5000> in your browser. To stop it, focus the terminal and press `Ctrl+C`.

## How to use

1. Enter a tournament name.
2. Enter your final score as a whole number between 1 and 300.
3. Select **Add to tournament list**. The saved entry appears in the history with the date it was recorded.
4. Review the saved tournament count and combined total strokes above the list. Both update when entries change.
5. Select **Delete** beside a tournament to remove it.

## Project files

```text
app.py                  Flask routes, score validation, and JSON storage
templates/index.html    Page structure and dynamic tournament list
static/style.css        Colors, layout, and responsive styling
requirements.txt        Python package dependencies
data/tournaments.json   Tournament data, created when the first entry is saved
```

The `data/tournaments.json` file is stored on your computer and excluded from Git. Keep a copy of it if you want to back up your tournament history.

## Notes

This app uses Flask's built-in development server for local use. It is intended for a personal tracker, not for deployment as a public production website.