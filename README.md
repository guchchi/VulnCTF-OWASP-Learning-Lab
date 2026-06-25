<div align="center">

# VulnCTF — OWASP Top 10 Learning Lab

**CTF challenges · web security · vulnerability analysis · secure coding**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-3.0-black)](https://flask.palletsprojects.com)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Code style](https://img.shields.io/badge/code%20style-strict-black)](https://github.com/psf/black)

</div>

A deliberately vulnerable Flask web application with 5 CTF-style challenges covering common web vulnerabilities from the OWASP Top 10. Built for local cybersecurity education.

> &#9888; **This application is intentionally vulnerable. Run locally only — do not deploy publicly.**

---

## Quick Start

```bash
git clone https://github.com/guchchi/VulnCTF-OWASP-Learning-Lab.git
cd VulnCTF-OWASP-Learning-Lab
python -m venv venv
venv\Scripts\activate      # Windows: source venv/bin/activate (macOS/Linux)
pip install -r requirements.txt
python app.py
# Open http://localhost:5000
```

---

## Challenges

| Challenge | Vulnerability | OWASP | Difficulty |
|---|---|---|---|
| SQL Injection | Raw SQL with user input concatenation | A03:2021 — Injection | Easy |
| Stored XSS | Unsafe rendering with `\| safe` | A03:2021 — Injection (XSS) | Easy |
| IDOR | Direct object access without auth check | A01:2021 — Broken Access Control | Easy |
| Path Traversal | Unvalidated file paths allowing `../` | A01:2021 — Broken Access Control | Medium |
| Command Injection | Unsafe shell execution with `shell=True` | A03:2021 — Injection | Medium |

---

## Usage

```bash
python app.py
```

Opens at `http://localhost:5000`. Navigate to each challenge, exploit the vulnerability, capture the flag, and read the write-up for the secure fix.

---

## Project Structure

```
VulnCTF/
├── app.py                  # Flask app with 5 vulnerable routes
├── flag.py                 # CTF flags and mock data
├── secret.txt              # Target file for path traversal
├── pyproject.toml          # Package metadata
├── CHANGELOG.md            # Version history
├── LICENSE                 # MIT license
├── SECURITY.md             # Security policy
├── requirements.txt        # Python dependencies
├── static/
│   └── style.css           # Dark cyber theme
├── templates/
│   ├── index.html          # Challenge dashboard
│   ├── challenge.html      # SQL injection page
│   ├── xss.html            # XSS challenge page
│   ├── idor.html           # IDOR challenge page
│   ├── file.html           # Path traversal page
│   ├── command.html        # Command injection page
│   └── writeup.html        # Solution write-up
├── screenshots/            # README screenshots
└── docs/
    └── PORTFOLIO_SUMMARY.md
```

---

## Cybersecurity Learning Summary

This project taught me how common web vulnerabilities work at the code level:

- Why parameterized queries prevent SQL injection
- Why output encoding stops XSS
- Why server-side authorization checks are essential
- Why file paths must be validated and restricted
- Why user input should never reach a shell command

Understanding these vulnerabilities from an attacker's perspective is essential for building secure systems as a defender.

---

## License

MIT — see [LICENSE](LICENSE).

---

<div align="center">
  <sub>Built for the IIT Kanpur B.Cyber program · Defensive cybersecurity portfolio project</sub>
</div>
