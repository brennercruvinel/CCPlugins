# Clean Project

I'll help clean up development artifacts while preserving your working code.

First, let me create a safety checkpoint and backup:

```bash
# Create backup directory
BACKUP_DIR="$HOME/.claude/.ccplugins_backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
echo "Creating safety backup at: $BACKUP_DIR"

# Verify critical directories are protected
if [ -d "$HOME/.claude" ]; then
    echo "✓ .claude directory detected and will be protected"
fi
```

Then I'll identify what should be cleaned based on:
- Our conversation history
- Common development patterns
- Temporary files and artifacts

I'll look for and remove:
- Debug/log files
- Temporary files
- Failed implementation attempts
- Development artifacts
- Debug statements in code

Important: I will NEVER remove:
- The .claude directory (contains commands and configurations)
- .git directory
- Essential configuration files
- Source code files unless explicitly identified as temporary

When I find multiple items to clean, I'll create a todo list to process them safely.

Before removing anything, I'll:
1. Show you what I plan to remove
2. Create backups of files before deletion
3. Explain why it should be removed
4. Wait for your confirmation

If the cleanup encounters any errors:
- I'll stop immediately
- Report what failed
- Ensure partial changes can be rolled back
- Suggest alternative approaches

After cleanup, I'll verify the project still works properly by:
- Checking build/compile status
- Running basic sanity checks
- Confirming no critical files were affected

The goal is to keep only the clean, working solution while maintaining safety.