<p align="center">
  <img src="https://github.com/convergence-human-technology/executive-ai-core/ExecAI-executive-ai-core-co.png" alt="ExecAI - A Minimal Executive AI" width="100%" height="100%">
</p>

# ExecAI - A Minimal Executive AI

![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![GitHub stars](https://img.shields.io/github/stars/Convergence-Human-And-Technology/executive-ai-core?style=social)
![GitHub last commit](https://img.shields.io/github/last-commit/Convergence-Human-And-Technology/executive-ai-core)
![Maintained](https://img.shields.io/badge/Maintained-yes-green.svg)
![GitHub forks](https://img.shields.io/github/forks/Convergence-Human-And-Technology/executive-ai-core?style=social)
![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)

A minimal, fully commented Python implementation of an executive AI agent.
Built by [Convergence - Human And Technology](https://github.com/Convergence-Human-And-Technology) for students, teachers, and junior developers.

The entire logic fits in one Python file with fewer than 90 lines of code.
Every concept, every line, every choice is explained.

---

## Table of Contents

1. [What is this project ?](#1-what-is-this-project)
2. [What is an Executive AI ?](#2-what-is-an-executive-ai)
3. [Core Concepts](#3-core-concepts)
4. [Project Structure](#4-project-structure)
5. [Prerequisites](#5-prerequisites)
6. [Installation](#6-installation)
7. [Usage](#7-usage)
8. [How It Works](#8-how-it-works)
9. [Running Tests](#9-running-tests)
10. [Contributing](#10-contributing)
11. [License](#11-license)
12. [Contact](#12-contact)

---

## 1. What is this project ?

ExecAI is a small Python project that shows, step by step, how to build an executive AI (also called an agentic AI) from scratch.

The goal is to understand how autonomous AI agents work, not just use them. You will see the full pipeline : from a plain text goal typed by the user, down to the raw API call, and back up to the final result printed in the terminal.

This project is for you if :

- You are a student (18+) who wants to go beyond using ChatGPT and understand what is happening under the hood
- You are a junior developer curious about how AI agents actually work
- You are a teacher looking for a clean, minimal example to use in class
- You want working code you can read, run, and modify in under an hour

There is no magic here. Just Python, one API call per step, and clear comments.

---

## 2. What is an Executive AI ?

Most people interact with AI as a chatbot : you ask a question, it answers. That is called a reactive AI.

An executive AI is different. It receives a high-level goal and figures out by itself what to do to reach it. It plans, it acts, it reports. It does not wait for you to tell it each step.

A simple analogy :

| Type | Analogy | Behavior |
|---|---|---|
| Reactive AI | A taxi driver | Takes you exactly where you say, nothing more |
| Executive AI | A travel agent | Takes your destination, plans the route, books everything, handles problems |

In code, this breaks down into three phases :

| Phase | What happens | Who does it |
|---|---|---|
| Planning | The AI reads the goal and writes a list of concrete steps | Claude, with a "planner" system prompt |
| Execution | The AI runs each step one by one | Claude, with an "executor" system prompt |
| Reporting | The results are collected and printed | Python |

The key insight is that we use the same AI model for both phases. What changes is the system prompt we give it. The AI does not "know" it is an agent. We create that behavior through prompt design.

---

## 3. Core Concepts

These are the four concepts you will encounter in the code. Read them once before opening the source file.

**API (Application Programming Interface)**

An API is a standardized way for two programs to communicate over the internet. Here, our Python script sends a message to Anthropic's servers, and Claude processes it and sends a response back. We use the official `anthropic` Python package, which handles all the network details for us.

**System Prompt**

When you call an AI through an API, you can include a "system prompt" before the conversation begins. This is a private instruction that shapes how the AI behaves during the entire exchange. In a chatbot product like Claude.ai, this is written by the company. In this project, we write it ourselves, which is why we can make Claude behave as a planner in one call and as an executor in the next.

**Token**

AI models do not process words, they process tokens. A token is roughly three quarters of a word in English (the word "basketball" is one token, but "anthropology" might be two). When you set `max_tokens=512` in an API call, you are capping the length of the AI's response at around 380 words. Tokens also determine cost : Anthropic charges per input token and per output token.

**Environment Variable**

An environment variable is a value stored in your operating system, outside of your code. We use one called `ANTHROPIC_API_KEY` to store the API key. This is the standard practice for secrets. If you write the key directly in your Python file and push it to GitHub, it becomes public. Environment variables prevent that.

---

## 4. Project Structure

```
executive-ai-core/
├── .github/
│   ├── workflows/
│   │   └── ci.yml                  # Automated tests run on every push (CI/CD)
│   ├── ISSUE_TEMPLATE/
│   │   ├── bug_report.md           # Template when someone reports a bug
│   │   └── feature_request.md      # Template when someone requests a feature
│   └── PULL_REQUEST_TEMPLATE.md    # Template for code contributions
├── docs/
│   └── architecture.md             # Detailed technical architecture
├── src/
│   ├── main/
│   │   └── executive_ai.py         # The source code - start here
│   └── test/
│       └── test_executive_ai.py    # Automated tests
├── scripts/
│   └── setup.sh                    # One-command setup script
├── img/                            # Screenshots and diagrams
├── .gitignore                      # Files that Git should not track
├── .editorconfig                   # Shared editor settings for all contributors
├── LICENSE                         # MIT License
├── README.md                       # This file
├── CONTRIBUTING.md                 # How to contribute to this project
├── CHANGELOG.md                    # History of changes between versions
├── SECURITY.md                     # How to report security vulnerabilities
└── CODE_OF_CONDUCT.md              # Community behavior standards
```

Where to start : open `src/main/executive_ai.py`. That file is the entire project. Everything else supports it.

---

## 5. Prerequisites

| Requirement | Minimum version | How to check |
|---|---|---|
| Python | 3.10 | `python --version` |
| pip | 23.0 | `pip --version` |
| Anthropic API key | N/A | [Get one here](https://console.anthropic.com/) |

No other tools, frameworks, or services are required.

The free tier of the Anthropic API is enough to run this project. A typical execution (5 steps) costs a fraction of a cent.

---

## 6. Installation

**Step 1 : Clone the repository**

Cloning downloads the project files from GitHub to your computer.

```bash
git clone https://github.com/Convergence-Human-And-Technology/executive-ai-core.git
cd executive-ai-core
```

**Step 2 : Install the dependency**

This project has one external dependency : the `anthropic` package. It is the official Python SDK (Software Development Kit) from Anthropic that handles API calls.

```bash
pip install anthropic
```

**Step 3 : Set your API key**

Get your key from [console.anthropic.com](https://console.anthropic.com/), then set it as an environment variable.

On Linux or macOS :
```bash
export ANTHROPIC_API_KEY="sk-ant-your-key-here"
```

On Windows (Command Prompt) :
```cmd
set ANTHROPIC_API_KEY=sk-ant-your-key-here
```

On Windows (PowerShell) :
```powershell
$env:ANTHROPIC_API_KEY = "sk-ant-your-key-here"
```

This variable is only available in the current terminal session. For a permanent setup, add the export line to your shell profile (`~/.bashrc`, `~/.zshrc`, etc.).

Or run the setup script, which handles everything :

```bash
bash scripts/setup.sh
```

---

## 7. Usage

Run the main script from the project root :

```bash
python src/main/executive_ai.py
```

The script will ask you for a goal. Type anything, or press Enter to use the default example.

```
Enter your goal (or press Enter to use the default) : Explain the three causes of climate change
```

Example output :

```
Goal : Explain the three causes of climate change
============================================================

Phase 1 - Planning
  1. Define climate change in one sentence
  2. Describe cause one : greenhouse gas emissions
  3. Describe cause two : deforestation
  4. Describe cause three : industrial agriculture
  5. Summarize all three causes in a conclusion

Phase 2 - Execution

  Step 1 : Define climate change in one sentence
  Result : Climate change refers to long-term shifts in temperatures and weather
           patterns, primarily caused by human activities since the 1800s.

  Step 2 : Describe cause one : greenhouse gas emissions
  Result : Burning fossil fuels such as coal, oil, and natural gas releases CO2
           and methane, which trap heat in the atmosphere.

  ...

============================================================
Done. 5 step(s) completed.
```

---

## 8. How It Works

Here is the full execution flow, from your input to the final output :

```
You type a goal
       |
       v
 +-----------+
 |  plan()   |    Calls Claude with the "planner" system prompt.
 |           |    Claude returns a numbered list of steps as plain text.
 |           |    Python splits that text into a list of strings.
 +-----------+
       |
       v
 [step 1, step 2, step 3, ...]
       |
       v
 +-------------+
 | execute()   |    For each step, calls Claude with the "executor" prompt.
 |  (in loop)  |    Claude performs the step and returns a concise result.
 |             |    Results are collected in a Python list.
 +-------------+
       |
       v
 [result 1, result 2, result 3, ...]
       |
       v
 +-----------+
 |  run()    |    Prints a formatted summary to the terminal.
 | (prints)  |
 +-----------+
```

Notice that the whole system makes N+1 API calls where N is the number of steps : one call to plan, then one call per step to execute. This is the simplest possible architecture for an executive AI.

More advanced agents add memory (storing past actions), tool use (calling external APIs), and error recovery (retrying failed steps). Those are the next things to explore once you understand this baseline.

---

## 9. Running Tests

The tests live in `src/test/test_executive_ai.py`. They use mocking to simulate the AI's responses without making real API calls. This means tests run instantly and do not require an API key.

With pytest (recommended) :

```bash
pip install pytest
python -m pytest src/test/ -v
```

With the built-in unittest module (no install needed) :

```bash
python -m unittest src/test/test_executive_ai.py -v
```

Expected output :

```
test_ignores_empty_lines ... ok
test_returns_list ... ok
test_returns_non_empty_string ... ok
test_returns_stripped_string ... ok

Ran 4 tests in 0.003s
OK
```

---

## 10. Contributing

Contributions are welcome. Read [CONTRIBUTING.md](CONTRIBUTING.md) for the full process.

Good first issues for beginners :

- Add a `--goal` command-line argument so the user does not need to type interactively
- Save the results to a Markdown file instead of just printing to the terminal
- Add a `max_steps` parameter to cap the number of steps the planner can produce
- Write tests for the `run()` function using mocking
- Add support for a second AI provider (OpenAI, Mistral, or Ollama for local models)

---

## 11. License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for the full text.

MIT means : you can use, copy, modify, and distribute this code freely, for any purpose, as long as you include the original license notice. You do not need to ask permission.

---

## 12. Contact

Project maintained by [Convergence - Human And Technology](https://github.com/Convergence-Human-And-Technology)

- Email : convergence-tech@proton.me
- LinkedIn : [company/convergence-organization](https://www.linkedin.com/company/convergence-organization)
- Facebook : [Convergence - Human And Technology](https://www.facebook.com/people/Convergence-Human-And-Technology/61578483081894/)
- GitHub : [Convergence-Human-And-Technology](https://github.com/Convergence-Human-And-Technology)

---

Last updated : 27/03/2026
