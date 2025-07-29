#!/bin/bash
# CCPlugins Uninstaller for Mac/Linux

set -e

echo "CCPlugins Uninstaller"
echo "===================="

COMMANDS_DIR="$HOME/.claude/commands"

# List of CCPlugins commands (including old ones for compatibility)
COMMANDS=(
    "cleanproject.md"
    "cleanup-types.md"     # Old command (removed)
    "commit.md"
    "context-cache.md"     # Old command (removed)
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

# Count installed commands
INSTALLED=0
for cmd in "${COMMANDS[@]}"; do
    if [ -f "$COMMANDS_DIR/$cmd" ]; then
        ((INSTALLED++))
    fi
done

if [ $INSTALLED -eq 0 ]; then
    echo "[INFO] No CCPlugins commands found."
    exit 0
fi

echo "[FOUND] $INSTALLED CCPlugins commands installed"
read -p "Remove all CCPlugins commands? (y/N): " -n 1 -r
echo

if [[ ! $REPLY =~ ^[Yy]$ ]]; then
    echo "[CANCELLED] Uninstall cancelled."
    exit 0
fi

# Remove commands
REMOVED=0
for cmd in "${COMMANDS[@]}"; do
    if [ -f "$COMMANDS_DIR/$cmd" ]; then
        rm "$COMMANDS_DIR/$cmd"
        echo "  - Removed $cmd"
        ((REMOVED++))
    fi
done

# Clean up cache and backups
CACHE_DIR="$HOME/.claude/.ccplugins_cache"
BACKUP_DIR="$HOME/.claude/.ccplugins_backups"

if [ -d "$CACHE_DIR" ] || [ -d "$BACKUP_DIR" ]; then
    read -p "Also remove cache and backups? (y/N): " -n 1 -r
    echo
    if [[ $REPLY =~ ^[Yy]$ ]]; then
        [ -d "$CACHE_DIR" ] && rm -rf "$CACHE_DIR" && echo "  - Removed cache directory"
        [ -d "$BACKUP_DIR" ] && rm -rf "$BACKUP_DIR" && echo "  - Removed backups directory"
    fi
fi

echo "[SUCCESS] Uninstalled $REMOVED commands"
echo "Thanks for trying CCPlugins!"