from flask import Flask, request, render_template, session, redirect, url_for
import sqlite3
import os
import subprocess
from typing import Any, Dict, List, Optional, Tuple
from flag import FLAGS, USERS, POSTS

app = Flask(__name__)
app.secret_key = "supersecretkey123"

DB_PATH = os.path.join(os.path.dirname(__file__), "vulnctf.db")


def init_db() -> None:
    if os.path.exists(DB_PATH):
        os.remove(DB_PATH)
    conn = sqlite3.connect(DB_PATH)
    c = conn.cursor()
    c.execute("CREATE TABLE users (id INTEGER PRIMARY KEY, username TEXT, password TEXT)")
    c.execute("INSERT INTO users VALUES (1, 'admin', 'admin123')")
    c.execute("INSERT INTO users VALUES (2, 'guest', 'guest123')")
    c.execute("INSERT INTO users VALUES (3, 'hacker', 'letmein')")
    conn.commit()
    conn.close()


init_db()


@app.route("/")
def index() -> str:
    return render_template("index.html")


# Educational vulnerability: SQL Injection
@app.route("/challenge/sqli", methods=["GET", "POST"])
def challenge_sqli() -> str:
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")
        conn = sqlite3.connect(DB_PATH)
        c = conn.cursor()
        query = f"SELECT * FROM users WHERE username='{username}' AND password='{password}'"
        try:
            c.execute(query)
            user = c.fetchone()
            if user:
                message = f"Login successful! Welcome {user[1]}. {FLAGS['sqli']}"
            else:
                message = "Invalid credentials"
        except Exception as e:
            message = f"Error: {e}"
        conn.close()
    return render_template("challenge.html", title="SQL Injection", challenge="sqli", message=message)


# Educational vulnerability: Stored XSS
@app.route("/challenge/xss", methods=["GET", "POST"])
def challenge_xss() -> str:
    search = request.args.get("search", "")
    posts: List[Dict[str, Any]] = POSTS
    message = ""
    if request.method == "POST":
        new_post = request.form.get("comment", "")
        if new_post:
            posts.append({"id": len(posts) + 1, "user": "you", "content": new_post})
            message = "Comment added!"
    return render_template("xss.html", search=search, posts=posts, message=message)


# Educational vulnerability: IDOR (Insecure Direct Object Reference)
@app.route("/challenge/idor")
def challenge_idor() -> str:
    user_id = request.args.get("id", 1, type=int)
    user = USERS.get(user_id)
    if not user:
        return "User not found", 404
    return render_template("idor.html", user=user, user_id=user_id)


# Educational vulnerability: Path Traversal
@app.route("/challenge/file")
def challenge_file() -> str:
    filename = request.args.get("file", "")
    content = ""
    if filename:
        safe_path = os.path.join(os.path.dirname(__file__), filename)
        try:
            with open(safe_path, "r") as f:
                content = f.read()
        except Exception:
            content = "File not found or cannot be read"
    return render_template("file.html", filename=filename, content=content)


# Educational vulnerability: Command Injection
@app.route("/challenge/command", methods=["GET", "POST"])
def challenge_command() -> str:
    output = ""
    command = ""
    if request.method == "POST":
        ip = request.form.get("ip", "")
        command = f"ping -n 1 {ip}"
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, timeout=5).decode()
        except subprocess.TimeoutExpired:
            output = "Command timed out"
        except Exception as e:
            output = str(e)
    return render_template("command.html", output=output, command=command)


@app.route("/writeup")
def writeup() -> str:
    return render_template("writeup.html")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
