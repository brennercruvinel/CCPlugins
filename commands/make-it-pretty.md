# Make It Pretty

I'll improve code readability while preserving exact functionality.

First, let me create a safety commit and backup:

```bash
# Create a commit before changes
git add -A
git commit -m "Backup before prettifying code" || echo "No changes to commit"

# Create backup folder
BACKUP_DIR="$HOME/.claude/.prettify_backup_$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
echo "Creating backup at: $BACKUP_DIR"
```

I'll identify files to beautify based on:
- Files you specify, or if none specified, analyze the entire application
- Recently modified code
- Our conversation context

```bash
# Copy files to backup before modifications
if [ -n "$ARGUMENTS" ]; then
    cp -r "$ARGUMENTS" "$BACKUP_DIR/" 2>/dev/null || true
else
    # Backup all source files based on project structure
    echo "Backing up source files..."
fi
```

I'll improve:
- Variable and function names for clarity
- Code organization and structure
- Remove unused code and clutter
- Simplify complex expressions
- Group related functionality
- Fix loose or generic type declarations
- Add missing type annotations where supported
- Make types more specific based on usage

My approach:
1. Analyze current code patterns and type usage
2. Apply consistent naming conventions
3. Improve type safety where applicable
4. Reorganize for better readability
5. Remove redundancy without changing logic

I'll ensure:
- All functionality remains identical
- Tests continue to pass (if available)
- No behavior changes occur
- Backups are available for rollback

After beautifying, I'll:
- Show a summary of improvements
- Verify everything still works
- Create another commit with the improvements

```bash
# After prettifying, commit the changes
git add -A
git commit -m "Prettify code: improve readability and organization" || echo "No changes made"
```

This helps transform working code into maintainable code without risk.