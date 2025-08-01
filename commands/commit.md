# Smart Git Commit

I'll analyze your changes and create a meaningful commit message.

```bash
# Verify git repo and detect changes
if ! git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Error: Not a git repository"
    exit 1
fi

if git diff --cached --quiet && git diff --quiet; then
    echo "No changes to commit"
    exit 0
fi

# Stage modified files if nothing staged
if git diff --cached --quiet; then
    git add -u
fi

# Show what will be committed
git diff --cached --name-status
```

I'll analyze the changes to create a conventional commit message:
- **Type**: feat|fix|docs|style|refactor|test|chore
- **Scope**: component affected (optional)
- **Subject**: clear description

The commit will use your existing git configuration and follow your project's conventions.