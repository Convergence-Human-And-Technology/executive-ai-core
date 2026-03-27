# Security Policy

## Supported Versions

| Version | Supported |
|---|---|
| 1.x | Yes |

---

## Reporting a Vulnerability

Do not open a public GitHub issue to report a security vulnerability. Public issues are visible to everyone, including malicious actors.

Instead, send an email directly to : convergence-tech@proton.me

Include in your report :

- A description of the vulnerability
- Steps to reproduce it
- The potential impact (what an attacker could do)
- Your suggested fix, if you have one

You will receive a response within 72 hours. If the vulnerability is confirmed, a fix will be released as soon as possible and you will be credited in the changelog (unless you prefer anonymity).

---

## Security Notes for Users

**API Key**

Never put your `ANTHROPIC_API_KEY` directly in your Python files or commit it to Git. Use environment variables as shown in the README. If you accidentally expose a key, revoke it immediately from [console.anthropic.com](https://console.anthropic.com/).

**Model Outputs**

The AI's outputs are not validated or sanitized. Do not pass them directly to system commands, database queries, or any security-sensitive context without review.
