# Security Review

## Purpose

This document reviews the security topics covered by the VulnCTF lab, the risks each module demonstrates, and the defensive lessons learned from studying them.

## Modules Reviewed

### 1. SQL Injection

**Observed Risk:** Unsanitized user input is concatenated directly into a SQL query string.

**Defensive Lesson:** Parameterized queries separate SQL logic from data. When user input is passed as a parameter rather than concatenated, it can never alter the structure of the query.

### 2. Stored XSS

**Observed Risk:** User-submitted content is rendered in the browser using Jinja2's `| safe` filter, which disables HTML escaping.

**Defensive Lesson:** User-generated content should never be rendered without escaping. Jinja2 auto-escapes by default — removing `| safe` is sufficient. For applications needing rich text, use a trusted sanitization library.

### 3. IDOR (Insecure Direct Object Reference)

**Observed Risk:** User IDs are accepted from the URL parameter without any server-side authorization check. Any user can view any other user's profile by changing the `id` value.

**Defensive Lesson:** Authorization must be verified server-side for every access to protected resources. The authenticated user's identity must be checked against the resource owner.

### 4. Path Traversal

**Observed Risk:** User-supplied file paths are used to read files from disk. While `os.path.join()` is used, it does not prevent `../` traversal sequences.

**Defensive Lesson:** File paths must be validated against an allowlist or resolved to an absolute path and checked to ensure they remain within a restricted base directory.

### 5. Command Injection

**Observed Risk:** User input is passed directly to a system shell command with `shell=True`, allowing arbitrary command execution.

**Defensive Lesson:** Avoid `shell=True` whenever possible. Pass command arguments as a list. If shell commands are necessary, strictly validate input against an expected pattern.

## Summary of Defensive Principles

- Never trust user input
- Validate, sanitize, and escape at every layer
- Authorize access server-side, not in the frontend
- Use safe APIs (parameterized queries, no `shell=True`)
- Restrict file system access to known safe directories
- Log and monitor suspicious activity
