# Contributing to ExecAI

Thank you for taking the time to contribute. This guide explains how to do it correctly.

---

## Table of Contents

1. [Code of Conduct](#1-code-of-conduct)
2. [How to Report a Bug](#2-how-to-report-a-bug)
3. [How to Request a Feature](#3-how-to-request-a-feature)
4. [How to Submit Code](#4-how-to-submit-code)
5. [Code Style](#5-code-style)
6. [Commit Message Format](#6-commit-message-format)

---

## 1. Code of Conduct

By contributing, you agree to follow the [Code of Conduct](CODE_OF_CONDUCT.md).
Respectful, clear communication is expected from everyone.

---

## 2. How to Report a Bug

Before opening an issue, search existing issues to avoid duplicates.

To report a bug :

1. Go to the [Issues](https://github.com/Convergence-Human-And-Technology/executive-ai-core/issues) tab
2. Click "New issue"
3. Choose the "Bug report" template
4. Fill in every section (steps to reproduce, expected behavior, actual behavior, environment)

A good bug report includes the exact error message, the Python version, and the OS.

---

## 3. How to Request a Feature

Feature requests are welcome. To open one :

1. Go to the [Issues](https://github.com/Convergence-Human-And-Technology/executive-ai-core/issues) tab
2. Click "New issue"
3. Choose the "Feature request" template
4. Describe the problem you are trying to solve, not just the solution you have in mind

---

## 4. How to Submit Code

**Step 1 : Fork the repository**

Click the "Fork" button on GitHub. This creates your own copy of the project.

**Step 2 : Clone your fork**

```bash
git clone https://github.com/YOUR-USERNAME/executive-ai-core.git
cd executive-ai-core
```

**Step 3 : Create a branch**

Never work directly on `main`. Create a descriptive branch name.

```bash
git checkout -b feature/add-cli-argument
```

**Step 4 : Make your changes**

Keep changes small and focused. One feature or fix per pull request.

**Step 5 : Run the tests**

```bash
python -m pytest src/test/ -v
```

All tests must pass before you submit.

**Step 6 : Commit your changes**

Follow the commit format described below.

**Step 7 : Push and open a pull request**

```bash
git push origin feature/add-cli-argument
```

Then go to your fork on GitHub and click "Compare and pull request".

---

## 5. Code Style

- Python 3.10+ syntax only
- Every function must have a docstring
- Every non-obvious line must have a comment that explains the "why", not the "what"
- Use descriptive variable names. `steps` is better than `s`. `goal` is better than `g`.
- No line longer than 100 characters
- No external dependencies beyond `anthropic` unless clearly justified

The goal of this project is pedagogy. Code that is harder to read is worse code here, even if it is more efficient.

---

## 6. Commit Message Format

Use this format :

```
type: short description in lowercase (under 72 characters)

Optional longer explanation if needed.
```

Types :

| Type | When to use |
|---|---|
| feat | A new feature |
| fix | A bug fix |
| docs | Documentation only |
| test | Adding or fixing tests |
| refactor | Code change that is not a fix or feature |
| chore | Build process, dependencies, tooling |

Examples :

```
feat: add --goal command-line argument
fix: handle empty response from plan()
docs: clarify token explanation in README
test: add test for empty line filtering in plan()
```
