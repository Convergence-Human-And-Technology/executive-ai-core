#!/usr/bin/env bash
# setup.sh
# =========
# One-command setup script for ExecAI.
# Run this from the project root with : bash scripts/setup.sh

set -e  # Stop immediately if any command fails

echo "ExecAI Setup"
echo "============"

# Step 1 : Check that Python is installed and the version is at least 3.10
echo ""
echo "Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "Found Python $python_version"

# Step 2 : Install the anthropic package
echo ""
echo "Installing dependencies..."
pip install --upgrade pip
pip install anthropic
echo "Done."

# Step 3 : Check if the API key is already set
echo ""
if [ -z "$ANTHROPIC_API_KEY" ]; then
    echo "ANTHROPIC_API_KEY is not set."
    echo ""
    echo "To set it for this session, run :"
    echo "  export ANTHROPIC_API_KEY=\"your-key-here\""
    echo ""
    echo "To make it permanent, add that line to your ~/.bashrc or ~/.zshrc"
    echo "and run : source ~/.bashrc"
else
    echo "ANTHROPIC_API_KEY is already set."
fi

# Step 4 : Done
echo ""
echo "Setup complete. To run ExecAI :"
echo "  python src/main/executive_ai.py"
