#!/usr/bin/env python3
# CCPlugins Uninstaller

"""
CCPlugins Uninstaller
Removes command files from ~/.claude/commands/
"""

import os
import shutil
from pathlib import Path

def main():
    # Command files to remove (including old ones for compatibility)
    commands = [
        "cleanproject.md",
        "cleanup-types.md",  # Old command (removed)
        "commit.md",
        "context-cache.md",  # Old command (removed)
        "find-todos.md",
        "fix-imports.md",
        "format.md",
        "human-mode.md",
        "make-it-pretty.md",
        "remove-comments.md",
        "review.md",
        "session-end.md",
        "session-start.md",
        "test.md",
        "todos-to-issues.md",
        "undo.md"
    ]
    
    commands_dir = Path.home() / ".claude" / "commands"
    
    print("CCPlugins Uninstaller")
    print("=" * 40)
    
    if not commands_dir.exists():
        print("[INFO] Commands directory not found. Nothing to uninstall.")
        return
    
    # Count installed commands
    installed = 0
    for cmd in commands:
        if (commands_dir / cmd).exists():
            installed += 1
    
    if installed == 0:
        print("[INFO] No CCPlugins commands found.")
        return
    
    print(f"[FOUND] {installed} CCPlugins commands installed")
    response = input("\nRemove all CCPlugins commands? (y/N): ")
    
    if response.lower() != 'y':
        print("[CANCELLED] Uninstall cancelled.")
        return
    
    # Remove commands
    removed = 0
    for cmd in commands:
        cmd_path = commands_dir / cmd
        if cmd_path.exists():
            try:
                os.remove(cmd_path)
                print(f"  - Removed {cmd}")
                removed += 1
            except Exception as e:
                print(f"  ! Failed to remove {cmd}: {e}")
    
    # Clean up cache and backups if requested
    cache_dir = Path.home() / ".claude" / ".ccplugins_cache"
    backup_dir = Path.home() / ".claude" / ".ccplugins_backups"
    
    if cache_dir.exists() or backup_dir.exists():
        response = input("\nAlso remove cache and backups? (y/N): ")
        if response.lower() == 'y':
            if cache_dir.exists():
                shutil.rmtree(cache_dir)
                print("  - Removed cache directory")
            if backup_dir.exists():
                shutil.rmtree(backup_dir)
                print("  - Removed backups directory")
    
    print(f"\n[SUCCESS] Uninstalled {removed} commands")
    print("Thanks for trying CCPlugins!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[CANCELLED] Uninstall cancelled.")
    except Exception as e:
        print(f"\n[ERROR] Uninstall failed: {e}")