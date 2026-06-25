<div align="center">

# VulnCTF — OWASP Learning Lab

**Web Security · Vulnerability Analysis · Secure Coding · Local Educational Lab**

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://python.org)
[![Flask](https://img.shields.io/badge/flask-3.0-black)](https://flask.palletsprojects.com)
[![Educational Project](https://img.shields.io/badge/project-educational-yellow)](#)
[![Defensive Security](https://img.shields.io/badge/focus-defensive-green)](#)
[![OWASP Learning](https://img.shields.io/badge/owasp-learning-orange)](#)

</div>

VulnCTF is a safe educational cybersecurity lab for learning common web application security concepts through controlled examples, documentation, and defensive analysis. It is built as a deliberately vulnerable Flask application with five challenge modules, each demonstrating a specific class of web security weakness.

> **This application is intentionally vulnerable. Run it locally only for learning purposes. Do not deploy publicly.**

---

## Project Status

Active — local educational lab. Currently includes 5 OWASP-aligned vulnerability modules with a solution write-up page.

---

## Why I Built This

I built this project to move from reading about web vulnerabilities to understanding them at the code level. Instead of only studying theory, this lab lets me:

- See exactly how unsafe patterns look in source code
- Understand why each pattern is risky by exploiting it in a controlled setting
- Learn the corresponding defensive fix for each vulnerability
- Document what I learned in clear, written notes

---

## Cybersecurity Problem Statement

Web applications frequently suffer from security issues rooted in:

- Unsafe handling of user-supplied input
- Missing or weak authorization checks
- Reliance on client-side-only controls
- Use of dangerous APIs without understanding the risks

This lab demonstrates these problems through small, focused examples so that the underlying principles are clear before moving to more complex real-world scenarios.

---

## What This Lab Demonstrates

- How unsafe code patterns create security weaknesses
- Why input validation, authorization, and safe APIs matter
- How each vulnerability can be identified, exploited, and fixed
- The difference between insecure and secure implementations

---

## Security Concepts Covered

| Concept | Module | Defensive Lesson |
|---|---|---|
| SQL Injection | SQLi | Use parameterized queries |
| Cross-Site Scripting | Stored XSS | Never trust user content; escape output |
| Insecure Direct Object Reference | IDOR | Authorize every access server-side |
| Path Traversal | File Reader | Validate and restrict file paths |
| Command Injection | Ping Tool | Avoid shell=True; validate input strictly |

---

## Lab Modules

| Module | Vulnerability Class | OWASP Category | Difficulty |
|---|---|---|---|
| SQL Injection | Injection | A03:2021 — Injection | Easy |
| Stored XSS | Cross-Site Scripting | A03:2021 — Injection | Easy |
| IDOR | Broken Access Control | A01:2021 — Broken Access Control | Easy |
| Path Traversal | Broken Access Control | A01:2021 — Broken Access Control | Medium |
| Command Injection | Injection | A03:2021 — Injection | Medium |

Each module includes a challenge page, a hint system, and a flag to capture. The write-up page explains the vulnerability, shows the insecure code, demonstrates exploitation, and provides the secure fix.

---

## Architecture

```
Browser → Flask Routes → Challenge Logic → Mock Data (flags, users, posts)
                           ↓
                    Write-up Page (remediation docs)
```

### Folder Structure

```
VulnCTF/
├── app.py                  # Flask application with 5 vulnerable routes
├── flag.py                 # CTF flags and mock data
├── secret.txt              # Target file for path traversal challenge
├── pyproject.toml          # Package metadata
├── README.md               # This file
├── SECURITY.md             # Security policy and responsible use
├── requirements.txt        # Dependencies
├── docs/                   # Documentation
│   ├── SECURITY_REVIEW.md
│   ├── THREAT_MODEL.md
│   ├── LEARNING_NOTES.md
│   ├── EVIDENCE.md
│   └── FUTURE_IMPROVEMENTS.md
├── static/
│   └── style.css           # Application styles
├── templates/              # Jinja2 templates
│   ├── index.html          # Challenge dashboard
│   ├── challenge.html      # SQL injection page
│   ├── xss.html            # Stored XSS page
│   ├── idor.html           # IDOR page
│   ├── file.html           # Path traversal page
│   ├── command.html        # Command injection page
│   └── writeup.html        # Full solution write-up
└── screenshots/            # Lab screenshots and evidence
```

---

## Screenshots & Evidence

The `screenshots/` directory contains images captured during local lab testing. Each screenshot documents a specific stage of the learning flow.

*Screenshots are added as the lab is exercised and documented. See [docs/EVIDENCE.md](docs/EVIDENCE.md) for the current screenshot inventory and captions.*

---

## How to Run Locally

### Prerequisites

- Python 3.8+
- pip

### Setup

```bash
git clone https://github.com/guchchi/VulnCTF-OWASP-Learning-Lab.git
cd VulnCTF-OWASP-Learning-Lab

python -m venv venv
venv\Scripts\activate      # Windows
source venv/bin/activate   # macOS / Linux

pip install -r requirements.txt
python app.py
```

Open [http://localhost:5000](http://localhost:5000) in your browser.

---

## How to Use the Lab Safely

1. Run this application only on your local machine
2. Do not expose it to any network — bind to `127.0.0.1` if possible (current default binds to `0.0.0.0`)
3. Do not deploy it on any public or shared server
4. Use the lab to learn — attempt each challenge, read the write-up, and understand the fix
5. Do not use these techniques against any system without explicit authorization

---

## Example Learning Flow

1. Start the application and open the dashboard
2. Pick a challenge — SQL Injection is recommended first
3. Read the challenge description and try to solve it using the hint
4. Capture the flag as proof of understanding
5. Read the write-up page to see the vulnerable code, exploitation, and secure fix
6. Reflect on why the vulnerability exists and how it could be prevented in a real application

---

## Defensive Takeaways

- Parameterized queries prevent SQL injection entirely
- Output encoding — or simply not using `| safe` — stops XSS
- Authorization must happen server-side, not in the frontend
- File access should be restricted to a known safe directory
- Shell commands with user input should be avoided; if necessary, validate the input strictly and avoid `shell=True`

---

## Limitations

- This is a student-built educational lab. It does not represent a full vulnerability disclosure or professional security audit.
- Some modules are simplified to focus on one concept at a time.
- The lab is designed for local learning only and should not be used against real websites or systems.
- More test coverage, logging, secure-code comparison examples, and documentation can be added over time.

---

## Future Improvements

See [docs/FUTURE_IMPROVEMENTS.md](docs/FUTURE_IMPROVEMENTS.md) for the full list of planned enhancements.

Planned additions include:

- More OWASP Top 10 modules (broken authentication, sensitive data exposure, SSRF)
- Side-by-side insecure vs secure code comparison pages
- Automated test cases for each vulnerability
- Improved logging and monitoring simulation
- Role-based demo users with different permission levels
- Docker setup for easier local deployment

---

## Portfolio Evidence Note

This project demonstrates my practical interest in cybersecurity through safe lab-based learning, documentation, and analysis of common web security concepts. It is part of my cybersecurity learning portfolio and is also included as supporting background evidence for academic cybersecurity applications.

---

## Ethical Use Disclaimer

This repository is created only for defensive cybersecurity learning, secure coding awareness, and safe lab-based practice. Do not use this project, its examples, or its techniques to test, scan, exploit, or attack any system without clear permission.

---

## License

MIT — see [LICENSE](LICENSE).
