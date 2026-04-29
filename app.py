from flask import Flask, render_template, request, redirect, url_for, jsonify
import sqlite3
from pathlib import Path

import os

DB_PATH = os.getenv("DB_PATH", "/data/incidents.db")

app = Flask(__name__)



def get_db_connection():
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    conn = get_db_connection()
    conn.execute("""
        CREATE TABLE IF NOT EXISTS incidents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT NOT NULL,
            severity TEXT NOT NULL,
            status TEXT NOT NULL DEFAULT 'Open'
        )
    """)
    conn.commit()
    conn.close()


@app.route("/")
def index():
    conn = get_db_connection()
    incidents = conn.execute("SELECT * FROM incidents ORDER BY id DESC").fetchall()
    conn.close()
    return render_template("index.html", incidents=incidents)


@app.route("/incidents", methods=["POST"])
def create_incident():
    title = request.form["title"]
    description = request.form["description"]
    severity = request.form["severity"]

    conn = get_db_connection()
    conn.execute(
        "INSERT INTO incidents (title, description, severity, status) VALUES (?, ?, ?, ?)",
        (title, description, severity, "Open")
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/incidents/<int:incident_id>/update", methods=["POST"])
def update_incident(incident_id):
    new_status = request.form["status"]

    conn = get_db_connection()
    conn.execute(
        "UPDATE incidents SET status = ? WHERE id = ?",
        (new_status, incident_id)
    )
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


@app.route("/incidents/<int:incident_id>/delete", methods=["POST"])
def delete_incident(incident_id):
    conn = get_db_connection()
    conn.execute("DELETE FROM incidents WHERE id = ?", (incident_id,))
    conn.commit()
    conn.close()
    return redirect(url_for("index"))


# Optional API endpoints
@app.route("/api/incidents", methods=["GET"])
def get_incidents_api():
    conn = get_db_connection()
    incidents = conn.execute("SELECT * FROM incidents ORDER BY id DESC").fetchall()
    conn.close()
    return jsonify([dict(row) for row in incidents])


@app.route("/health", methods=["GET"])
def health():
    return jsonify({"status": "healthy"}), 200


if __name__ == "__main__":
    init_db()
    app.run(host="0.0.0.0", port=5001, debug=True)