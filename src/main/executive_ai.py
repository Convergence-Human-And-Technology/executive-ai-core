# executive_ai.py
# ================
#
# An "executive AI" (also called an "agentic AI") is an AI that :
#   1. Receives a high-level GOAL from the user
#   2. Plans the STEPS needed to reach that goal
#   3. Executes each step one by one, using the AI as the engine
#   4. Reports the RESULTS
#
# This is different from a simple chatbot, which only answers one question at a time.
# An executive AI can complete complex, multi-step tasks on its own.
#
# The entire logic is in this one file.
# Read it top to bottom, like a story.
#
# Author  : Convergence - Human And Technology
# License : MIT
# Date    : 27/03/2026

import os          # Standard Python module to read environment variables
import anthropic   # Official Anthropic SDK  ->  install with : pip install anthropic


# ─────────────────────────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────────────────────────
# We connect to the Claude AI using our API key.
# The key is stored in an environment variable, NOT in this file.
# Storing secrets in code is a major security risk - always use env vars.
# How to set it :
#   Linux/macOS  : export ANTHROPIC_API_KEY="sk-ant-..."
#   Windows CMD  : set ANTHROPIC_API_KEY=sk-ant-...
# ─────────────────────────────────────────────────────────────
client = anthropic.Anthropic(api_key=os.environ["ANTHROPIC_API_KEY"])

# The model we use. Check https://docs.anthropic.com for the latest model names.
MODEL = "claude-sonnet-4-6"


# ─────────────────────────────────────────────────────────────
# HELPER : ask_ai()
# ─────────────────────────────────────────────────────────────
def ask_ai(role: str, task: str) -> str:
    """
    Send a message to Claude and return its text response.

    Parameters :
      role  -> the "system prompt" that tells Claude what role to play
      task  -> the actual task or question we send to Claude

    Returns :
      Claude's response as a plain Python string
    """
    response = client.messages.create(
        model=MODEL,
        max_tokens=512,   # Limit the response length (1 token ~ 0.75 words)
        system=role,      # The system prompt defines Claude's behavior
        messages=[
            {"role": "user", "content": task}  # Our message to Claude
        ]
    )
    # .content[0].text  ->  the text of the first (and only) response block
    # .strip()          ->  removes leading/trailing whitespace
    return response.content[0].text.strip()


# ─────────────────────────────────────────────────────────────
# PHASE 1 : plan()
# ─────────────────────────────────────────────────────────────
def plan(goal: str) -> list:
    """
    Ask Claude to break a high-level goal into a numbered list of steps.

    Parameters :
      goal -> the user's objective (e.g. "Summarize the benefits of solar energy")

    Returns :
      A Python list where each item is one step as a string
    """
    # The system prompt makes Claude behave strictly as a planner.
    # We tell it exactly what format to use, so the response is easy to parse.
    planner_role = (
        "You are a planner. "
        "Given a goal, return ONLY a numbered list of steps, one per line. "
        "No introduction. No explanation. No conclusion. Just the steps."
    )
    raw = ask_ai(planner_role, f"Goal : {goal}")

    # Split the response text into individual lines.
    # The list comprehension filters out any empty lines.
    return [line.strip() for line in raw.split("\n") if line.strip()]


# ─────────────────────────────────────────────────────────────
# PHASE 2 : execute()
# ─────────────────────────────────────────────────────────────
def execute(step: str) -> str:
    """
    Ask Claude to perform a single step and return a concise result.

    Parameters :
      step -> one step from the plan (e.g. "1. Find the definition of solar energy")

    Returns :
      Claude's output for that step, as a plain string
    """
    # Same AI model, different role. The system prompt changes the behavior entirely.
    executor_role = (
        "You are an executor. "
        "Perform the task and return the result concisely. "
        "No preamble. No explanation. Just the result."
    )
    return ask_ai(executor_role, step)


# ─────────────────────────────────────────────────────────────
# MAIN LOOP : run()
# ─────────────────────────────────────────────────────────────
def run(goal: str) -> list:
    """
    The executive AI pipeline : goal -> plan -> execute -> report.
    This function ties everything together.

    Parameters :
      goal -> the high-level task you want the AI to complete

    Returns :
      A list of results, one per step
    """
    print(f"\nGoal : {goal}")
    print("=" * 60)

    # Phase 1 : Planning
    # We ask Claude to produce the list of steps
    print("\nPhase 1 - Planning")
    steps = plan(goal)
    for i, step in enumerate(steps, start=1):
        print(f"  {i}. {step}")

    # Phase 2 : Execution
    # We loop over each step and ask Claude to perform it
    print("\nPhase 2 - Execution")
    results = []
    for i, step in enumerate(steps, start=1):
        print(f"\n  Step {i} : {step}")
        result = execute(step)
        results.append(result)
        print(f"  Result : {result}")

    # Phase 3 : Summary
    print("\n" + "=" * 60)
    print(f"Done. {len(steps)} step(s) completed.")

    return results  # Return the results so other scripts can use them


# ─────────────────────────────────────────────────────────────
# ENTRY POINT
# ─────────────────────────────────────────────────────────────
# This block only runs when you execute this file directly.
# It does NOT run when another script imports this file as a module.
# This is a standard Python pattern : if __name__ == "__main__"
# ─────────────────────────────────────────────────────────────
if __name__ == "__main__":
    default_goal = "Research and summarize the three main benefits of solar energy"

    # Ask the user for a goal, or fall back to the default
    user_input = input(f"\nEnter your goal (or press Enter to use the default) : ").strip()
    goal = user_input if user_input else default_goal

    run(goal)
