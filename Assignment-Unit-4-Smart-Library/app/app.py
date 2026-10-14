import os
import sqlite3
from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY", "change-this-before-production")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATA_DIR = os.environ.get("DATA_DIR", os.path.join(BASE_DIR, "data"))
DB_PATH = os.path.join(DATA_DIR, "library.db")

os.makedirs(DATA_DIR, exist_ok=True)


def get_db():
    connection = sqlite3.connect(DB_PATH)
    connection.row_factory = sqlite3.Row
    return connection


def initialize_database():
    with get_db() as db:
        db.execute("""
            CREATE TABLE IF NOT EXISTS books (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                title TEXT NOT NULL,
                author TEXT NOT NULL,
                category TEXT NOT NULL,
                status TEXT NOT NULL DEFAULT 'Available',
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

        count = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]

        if count == 0:
            sample_books = [
                ("Python Programming", "Mark Lutz", "Technology", "Available"),
                ("Artificial Intelligence", "Stuart Russell", "Technology", "Borrowed"),
                ("Clean Code", "Robert C. Martin", "Technology", "Available"),
                ("The Alchemist", "Paulo Coelho", "Fiction", "Available"),
                ("Atomic Habits", "James Clear", "Self-Help", "Borrowed"),
            ]

            db.executemany(
                "INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, ?)",
                sample_books,
            )


initialize_database()


@app.route("/")
def index():
    search = request.args.get("q", "").strip()

    with get_db() as db:
        if search:
            pattern = f"%{search}%"
            books = db.execute("""
                SELECT * FROM books
                WHERE title LIKE ? OR author LIKE ? OR category LIKE ?
                ORDER BY id DESC
            """, (pattern, pattern, pattern)).fetchall()
        else:
            books = db.execute(
                "SELECT * FROM books ORDER BY id DESC"
            ).fetchall()

        total = db.execute("SELECT COUNT(*) FROM books").fetchone()[0]
        available = db.execute(
            "SELECT COUNT(*) FROM books WHERE status = 'Available'"
        ).fetchone()[0]
        borrowed = db.execute(
            "SELECT COUNT(*) FROM books WHERE status = 'Borrowed'"
        ).fetchone()[0]

    return render_template(
        "index.html",
        books=books,
        total=total,
        available=available,
        borrowed=borrowed,
        search=search,
    )


@app.route("/add", methods=["POST"])
def add_book():
    title = request.form.get("title", "").strip()
    author = request.form.get("author", "").strip()
    category = request.form.get("category", "").strip()

    if not title or not author or not category:
        flash("Please complete all book details.", "error")
        return redirect(url_for("index"))

    with get_db() as db:
        db.execute(
            "INSERT INTO books (title, author, category, status) VALUES (?, ?, ?, 'Available')",
            (title, author, category),
        )

    flash("Book added successfully.", "success")
    return redirect(url_for("index"))


@app.route("/toggle/<int:book_id>", methods=["POST"])
def toggle_status(book_id):
    with get_db() as db:
        book = db.execute(
            "SELECT status FROM books WHERE id = ?", (book_id,)
        ).fetchone()

        if book is None:
            flash("Book not found.", "error")
        else:
            new_status = (
                "Borrowed" if book["status"] == "Available" else "Available"
            )
            db.execute(
                "UPDATE books SET status = ? WHERE id = ?",
                (new_status, book_id),
            )
            flash(f"Book marked as {new_status.lower()}.", "success")

    return redirect(url_for("index"))


@app.route("/health")
def health():
    try:
        with get_db() as db:
            db.execute("SELECT 1")
        return {"status": "healthy"}, 200
    except sqlite3.Error:
        return {"status": "unhealthy"}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
