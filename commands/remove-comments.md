# Remove Obvious Comments

I'll clean up redundant comments while preserving valuable documentation.

First, let me identify files with comments to review:

```bash
# Find files modified recently that likely have comments
if [ -d .git ]; then
    echo "Checking recently modified files for comments..."
    # I'll look at files changed recently in your project
else
    echo "Checking source files in the project..."
    # I'll scan for files that typically contain code
fi
```

I'll analyze each file and remove comments that:
- Simply restate what the code does
- Add no value beyond the code itself
- State the obvious (like "constructor" above a constructor)

I'll preserve comments that:
- Explain WHY something is done
- Document complex business logic
- Contain TODOs, FIXMEs, or HACKs
- Warn about non-obvious behavior
- Provide important context

For each file with obvious comments, I'll:
1. Show you the redundant comments I found
2. Explain why they should be removed
3. Show the cleaner version
4. Apply the changes after your confirmation

**💡 Pro Tip:** Enable [automatic formatting hooks](../HOOKS.md) to ensure consistent code style after comment cleanup. Your code will be properly formatted automatically after every modification.

This creates cleaner, more maintainable code where every comment has real value.