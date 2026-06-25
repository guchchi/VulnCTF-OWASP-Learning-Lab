# Evidence

## Screenshots

The `screenshots/` directory contains images captured during local lab testing. Below is the current inventory and what each screenshot documents.

### Inventory

| File | What It Proves |
|---|---|
| `127.0.0.1_5000_.png` | Challenge dashboard showing all 5 module descriptions and safety disclaimer |
| `127.0.0.1_5000_challenge_sqli.png` | SQL Injection challenge page with the login form vulnerable to injection |
| `127.0.0.1_5000_challenge_xss.png` | Stored XSS challenge page showing the comment section and search feature |
| `127.0.0.1_5000_challenge_idor.png` | IDOR challenge showing a user profile accessed via the `id` parameter |
| `127.0.0.1_5000_challenge_file.png` | Path Traversal challenge showing the file reader interface |
| `127.0.0.1_5000_challenge_command.png` | Command Injection challenge showing the ping tool input form |

### Planned Additions

| Screenshot | What It Proves |
|---|---|
| SQL Injection — Flag Captured | Shows the flag returned after `' OR 1=1 --` injection |
| Stored XSS — Flag Revealed | Shows the admin's comment containing the flag in page source |
| IDOR — Admin Profile with Flag | Shows user ID 1 admin profile with flag visible |
| Path Traversal — secret.txt | Shows the flag obtained by reading secret.txt |
| Command Injection — Output | Shows command output after injection with `&&` chaining |
| Write-up Page | Shows the solution documentation for a module |

## Demo Video

*A demo video may be added in the future to show the full learning flow.*

## Live Demo

*This lab is intended for local use only. No public live demo is available.*

## Notes

- All screenshots are captured from the local lab running on `localhost:5000`.
- The lab uses only fake/demo data — no real user information is involved.
- Screenshots are stored in the `screenshots/` directory at the repository root.
