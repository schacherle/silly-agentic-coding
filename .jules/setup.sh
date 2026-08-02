#!/usr/bin/env bash
set -euo pipefail

echo "=================================================="
echo "🚀 Initializing Jules Environment Setup..."
echo "=================================================="

# Ensure PATH includes expected binary locations
export PATH="/home/jules/.local/bin:/home/jules/.pyenv/shims:/home/jules/.pyenv/bin:${PATH}"

# Verify Python 3 installation
echo "📌 Checking Python environment..."
python3 --version

# Ensure .jules directory exists for agent journals
echo "📌 Ensuring .jules directory structure..."
mkdir -p .jules

# Ensure permissions are correct
echo "📌 Setting executable permissions on build script..."
chmod +x build.py 2>/dev/null || true

# Compile agent prompts
echo "📌 Compiling agent prompts..."
python3 build.py

# Verify agent prompts consistency
echo "📌 Verifying agent prompt consistency..."
python3 build.py --check

echo "=================================================="
echo "✅ Jules setup completed successfully!"
echo "=================================================="
