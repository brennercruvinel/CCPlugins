# Clean Project

I'll clean up development artifacts while preserving working code.

I'll identify and remove:
- Debug/log files and temporary artifacts
- Failed implementation attempts
- Development leftovers and debug statements

Protected directories: `.claude`, `.git`, essential configs, source code.

```bash
# Safety backup
BACKUP_DIR="$HOME/.claude/.ccplugins_backups/$(date +%Y%m%d_%H%M%S)"
mkdir -p "$BACKUP_DIR"
```

I'll show what I plan to remove, create backups, and verify the project still works after cleanup.