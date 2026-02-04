#!/bin/bash
# Setup script for Password Analyser using uv
# Run this once to initialize the project: ./setup.sh

set -e  # Exit on any error

echo ""
echo "═══════════════════════════════════════════════════════════════════════════════"
echo "🔐 Password Security Checker - Setup"
echo "═══════════════════════════════════════════════════════════════════════════════"
echo ""

# Check if uv is installed
if ! command -v uv &> /dev/null; then
    echo "📥 Installing uv (Python package manager)..."
    pip install uv
    echo "✅ uv installed successfully"
else
    echo "✅ uv is already installed"
fi

echo ""
echo "📦 Creating virtual environment in .venv/"
uv venv .venv

echo "📥 Activating environment and installing dependencies..."
source .venv/bin/activate
uv pip install -e .

echo ""
echo "═══════════════════════════════════════════════════════════════════════════════"
echo "✅ Setup Complete!"
echo "═══════════════════════════════════════════════════════════════════════════════"
echo ""
echo "Next steps:"
echo ""
echo "1️⃣  Activate the environment:"
echo "    source .venv/bin/activate"
echo ""
echo "2️⃣  Run the application:"
echo ""
echo "    💻 CLI Version:"
echo "       python password_analyser.py"
echo ""
echo "    🌐 Web Version:"
echo "       python app.py"
echo "       Open http://localhost:5000 in your browser"
echo ""
echo "═══════════════════════════════════════════════════════════════════════════════"
echo ""
