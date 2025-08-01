#!/bin/bash
# CCPlugins Installer for Mac/Linux

set -e
COMMANDS_DIR="$HOME/.claude/commands"
mkdir -p "$COMMANDS_DIR"


# Download commands from GitHub
REPO_URL="https://raw.githubusercontent.com/brennercruvinel/CCPlugins/main/commands"
COMMANDS=(
    "cleanproject.md"
    "commit.md"
    "find-todos.md"
    "fix-imports.md"
    "format.md"
    "human-mode.md"
    "make-it-pretty.md"
    "remove-comments.md"
    "review.md"
    "session-end.md"
    "session-start.md"
    "test.md"
    "todos-to-issues.md"
    "undo.md"
)

# Check for existing commands
EXISTING=0
for cmd in "${COMMANDS[@]}"; do
    if [ -f "$COMMANDS_DIR/$cmd" ]; then
        ((EXISTING++))
    fi
done

if [ $EXISTING -gt 0 ]; then
    echo "[WARNING] Found $EXISTING existing commands"
    read -p "Overwrite existing commands? (y/N): " -n 1 -r
    echo
    if [[ ! $REPLY =~ ^[Yy]$ ]]; then
        echo "[CANCELLED] Installation cancelled."
        echo "Tip: Use uninstall script first to remove old commands."
        exit 0
    fi
fi

echo "Downloading commands..."
for cmd in "${COMMANDS[@]}"; do
    curl -sSL "$REPO_URL/$cmd" -o "$COMMANDS_DIR/$cmd"
done

# Download hooks documentation
echo "Downloading hooks integration guide..."
curl -sSL "https://raw.githubusercontent.com/brennercruvinel/CCPlugins/main/HOOKS.md" -o "$COMMANDS_DIR/../HOOKS.md"

echo "CCPlugins installed to $COMMANDS_DIR"
echo "Type / in Claude Code to see available commands"
echo "See ~/.claude/HOOKS.md for automatic formatting setup"