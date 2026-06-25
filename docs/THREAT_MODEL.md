# Threat Model

## Scope

This threat model applies only to the local educational lab environment. It does not represent a real production system. The purpose is to understand how common web security weaknesses appear in application logic.

## Assets

| Asset | Description |
|---|---|
| User account state | Simulated user login state within the lab |
| Protected routes | Routes that should only be accessible by authorized users |
| Admin-only data | User profiles and secrets only intended for specific user IDs |
| Demo challenge data | The flags, posts, and mock data used in challenges |
| Source code examples | The Python and template code containing intentional vulnerabilities |
| File system | Local files accessible through the path traversal module |

## Possible Attackers (Lab Context)

- A user exploring the application beyond intended boundaries
- A user attempting to access another user's profile data
- A user trying to execute commands on the server

## Trust Boundaries

| Boundary | Description |
|---|---|
| Browser / Client | User-controlled environment; all client-side logic is visible and modifiable |
| Application Logic | Server-side code that processes requests |
| Local Backend | Flask route handlers and SQLite database interactions |
| File System | Local disk accessed through file-reading functionality |
| Shell / OS | Operating system shell accessed through command execution |

## Weak Assumptions Demonstrated

- Assuming that hiding a UI element is sufficient access control
- Assuming that user-supplied IDs can be trusted
- Assuming that user input will not contain SQL syntax
- Assuming that user input will not contain shell metacharacters
- Assuming that `os.path.join()` prevents directory traversal
- Assuming that user-generated content is safe to render as HTML

## Risks Studied

| Risk | Module | Description |
|---|---|---|
| Authentication bypass | SQLi | Attacker logs in as any user without knowing credentials |
| Data exposure | IDOR | Attacker views private profile data of other users |
| Script execution | XSS | Attacker injects JavaScript that runs in other users' browsers |
| File disclosure | Path Traversal | Attacker reads files outside the intended directory |
| Remote command execution | Command Injection | Attacker runs arbitrary shell commands on the server |

## Defensive Controls

- Parameterized queries prevent SQL injection
- Output escaping prevents XSS
- Server-side authorization checks prevent IDOR
- Path validation and allowlisting prevent path traversal
- Avoiding `shell=True` and validating input prevents command injection
- Logging and monitoring help detect suspicious activity
