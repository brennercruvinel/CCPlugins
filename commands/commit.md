# Smart Git Commit

I'll analyze your changes and create a meaningful commit message using available context.

First, let me check if this is a git repository and what's changed, leveraging our conversation history to understand the context of these changes:

```bash
# Verify we're in a git repository
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository"
    echo "This command requires git version control"
    exit 1
fi

# Check if we have changes to commit
if ! git diff --cached --quiet || ! git diff --quiet; then
    echo "Changes detected:"
    git status --short
else
    echo "No changes to commit"
    exit 0
fi

# Show detailed changes
git diff --cached --stat
git diff --stat
```

Now I'll analyze the changes to determine:
1. What files were modified (using `@file` references where available)
2. The nature of changes (feature, fix, refactor, etc.) based on our conversation context
3. The scope/component affected, informed by our recent work and project understanding

If the analysis or commit encounters errors:
- I'll explain what went wrong
- Suggest how to resolve it
- Ensure no partial commits occur

```bash
# If nothing is staged, I'll stage modified files (not untracked)
if git diff --cached --quiet; then
    echo "No files staged. Staging modified files..."
    git add -u
fi

# Show what will be committed
git diff --cached --name-status
```

Based on the analysis and our conversation context, I'll create a conventional commit message:
- **Type**: feat|fix|docs|style|refactor|test|chore
- **Scope**: component or area affected (using project context)
- **Subject**: clear description in present tense, informed by our work
- **Body**: why the change was made (leveraging conversation history if needed)

```bash
# I'll create the commit with the analyzed message
# Example: git commit -m "fix(auth): resolve login timeout issue"
```

The commit message will be concise, meaningful, and follow your project's conventions if I can detect them from recent commits or our conversation history.

**Important**: I will NEVER:
- Add "Co-authored-by" or any Claude signatures
- Include "Generated with Claude Code" or similar messages
- Modify git config or user credentials
- Add any AI/assistant attribution to the commit

The commit will use only your existing git user configuration, maintaining full ownership and authenticity of your commits.