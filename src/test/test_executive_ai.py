# test_executive_ai.py
# =====================
#
# Unit tests for executive_ai.py
#
# What is a unit test ?
#   A unit test checks that one small piece of code (a "unit") works correctly.
#   We test each function in isolation, not the whole system at once.
#
# What is mocking ?
#   Mocking means replacing a real function with a fake one during tests.
#   Here, we mock the Claude API calls so we do not need a real API key,
#   and so tests run instantly without spending money.
#
# How to run these tests :
#   python -m pytest src/test/ -v
#   python -m unittest src/test/test_executive_ai.py -v

import unittest
from unittest.mock import patch, MagicMock  # Built-in Python mocking tools
import sys
import os

# Add the src/ directory to the Python path so we can import our module
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from main.executive_ai import ask_ai, plan, execute, run


class TestAskAI(unittest.TestCase):
    """Tests for the ask_ai() helper function."""

    @patch("main.executive_ai.client")  # Replace the real API client with a fake one
    def test_returns_stripped_string(self, mock_client):
        """ask_ai() must return a plain string with no leading or trailing whitespace."""
        # Set up the fake API response
        mock_response = MagicMock()
        mock_response.content[0].text = "  Hello world  "  # Text with extra spaces
        mock_client.messages.create.return_value = mock_response

        result = ask_ai("You are a tester.", "Say hello.")

        # The result should be stripped of whitespace
        self.assertEqual(result, "Hello world")
        self.assertIsInstance(result, str)


class TestPlan(unittest.TestCase):
    """Tests for the plan() function."""

    @patch("main.executive_ai.ask_ai")  # Replace ask_ai with a fake version
    def test_returns_list(self, mock_ask_ai):
        """plan() must always return a Python list."""
        mock_ask_ai.return_value = "1. Step one\n2. Step two\n3. Step three"

        steps = plan("Do something useful")

        self.assertIsInstance(steps, list)    # Must be a list
        self.assertEqual(len(steps), 3)       # Must have 3 items

    @patch("main.executive_ai.ask_ai")
    def test_ignores_empty_lines(self, mock_ask_ai):
        """plan() must filter out empty lines from the AI response."""
        mock_ask_ai.return_value = "1. Step one\n\n2. Step two\n\n"

        steps = plan("Any goal")

        # Empty lines must not appear in the result
        self.assertEqual(len(steps), 2)


class TestExecute(unittest.TestCase):
    """Tests for the execute() function."""

    @patch("main.executive_ai.ask_ai")
    def test_returns_non_empty_string(self, mock_ask_ai):
        """execute() must return a non-empty string."""
        mock_ask_ai.return_value = "Task completed."

        result = execute("1. Do a specific task")

        self.assertIsInstance(result, str)
        self.assertGreater(len(result), 0)  # String must not be empty


if __name__ == "__main__":
    unittest.main(verbosity=2)
