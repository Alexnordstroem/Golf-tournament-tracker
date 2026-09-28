import json
from datetime import date
from pathlib import Path

from flask import Flask, flash, redirect, render_template, request, url_for


app = Flask(__name__)
app.secret_key = "golf-tracker-local-key"

PROJECT_FOLDER = Path(__file__).parent
TOURNAMENTS_FILE = PROJECT_FOLDER / "data" / "tournaments.json"


def load_tournaments():
    """Read saved tournaments, or start with an empty list."""
    if not TOURNAMENTS_FILE.exists():
        return []

    return json.loads(TOURNAMENTS_FILE.read_text(encoding="utf-8"))


def save_tournaments(tournaments):
    """Write tournament entries to the local JSON file."""
    TOURNAMENTS_FILE.parent.mkdir(exist_ok=True)
    TOURNAMENTS_FILE.write_text(
        json.dumps(tournaments, indent=2),
        encoding="utf-8",
    )


@app.route("/")
def home():
    tournaments = list(enumerate(load_tournaments()))[::-1]
    total_score = sum(tournament["score"] for _, tournament in tournaments)
    return render_template(
        "index.html",
        tournaments=tournaments,
        total_score=total_score,
    )


@app.route("/add", methods=["POST"])
def add_tournament():
    name = request.form.get("name", "").strip()
    score_text = request.form.get("score", "").strip()

    if not name:
        flash("Please enter a tournament name.", "error")
        return redirect(url_for("home"))

    try:
        score = int(score_text)
    except ValueError:
        flash("Please enter a whole-number score.", "error")
        return redirect(url_for("home"))

    if score < 1 or score > 300:
        flash("Score must be between 1 and 300.", "error")
        return redirect(url_for("home"))

    tournaments = load_tournaments()
    tournaments.append(
        {
            "name": name,
            "score": score,
            "date": date.today().strftime("%b %d, %Y"),
        }
    )
    save_tournaments(tournaments)
    flash("Tournament added.", "success")
    return redirect(url_for("home"))


@app.route("/delete/<int:index>", methods=["POST"])
def delete_tournament(index):
    tournaments = load_tournaments()

    if index < 0 or index >= len(tournaments):
        flash("That tournament could not be found.", "error")
        return redirect(url_for("home"))

    deleted_tournament = tournaments.pop(index)
    save_tournaments(tournaments)
    flash(f"{deleted_tournament['name']} was deleted.", "success")
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)