# Learning Notes

## What Is Access Control?

Access control determines who can view or use a specific resource. In web applications, this means ensuring that a user can only access data and functionality that they are permitted to use. Access control failures occur when the application does not properly verify the user's identity and permissions before granting access.

## Why Frontend-Only Security Is Weak

Everything that runs in the browser can be modified by the user. Hiding a button, disabling a form field, or removing a link in the HTML does not prevent an attacker from sending a request directly to the server. Security controls must always be enforced on the server.

## Why Secrets Should Not Be Exposed in Frontend Code

Any value embedded in HTML, JavaScript, or browser-accessible files is visible to anyone who views the page source or uses browser developer tools. API keys, tokens, flags, and internal identifiers should never be placed in client-side code.

## Why Role Checks Matter

Applications with different user roles (admin, editor, viewer) must verify that the user's role matches the required permission for every protected action. Checking the role only in the frontend or only at the start of a session is not sufficient — every request to a protected endpoint must be authorized individually.

## Why Logs and Validation Matter

Logging suspicious activity helps detect attacks in progress. Input validation — rejecting data that does not match expected patterns — reduces the attack surface before the data reaches sensitive logic. Both are essential layers of defense.

## Key Vocabulary

| Term | Meaning |
|---|---|
| Authentication | Verifying who the user is (login) |
| Authorization | Verifying what the user is allowed to do |
| Injection | Inserting malicious input that alters program behavior |
| Escaping | Converting special characters so they are treated as data, not code |
| Parameterized Query | Sending SQL logic and data separately so user input cannot alter the query |
| Least Privilege | Granting only the minimum permissions needed |
