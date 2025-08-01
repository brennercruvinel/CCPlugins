# Undo Last Operation

I'll help you rollback the last destructive operation performed by CCPlugins commands.

```bash
# Check for CCPlugins backups and recent changes
BACKUP_DIR="$HOME/.claude/.ccplugins_backups"
if [ -d "$BACKUP_DIR" ]; then
    echo "Recent backups:"
    ls -la "$BACKUP_DIR" | tail -10
fi

if git rev-parse --git-dir > /dev/null 2>&1; then
    echo "Git status:"
    git status --short
fi
```

I can restore using:
1. **CCPlugins backup** - From /cleanproject or other commands
2. **Git restore** - If changes haven't been committed
3. **Analysis** - Show what was modified to help you decide

I'll suggest the safest recovery method and let you choose the best approach.