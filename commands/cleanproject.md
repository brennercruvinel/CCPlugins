# Clean Project

I'll help clean up development artifacts while preserving your working code using Claude Code CLI's native tools for safe and efficient cleanup.

First, I'll create a safety checkpoint using **Read tool** to examine project structure and **Glob tool** to identify backup-worthy files.

I'll use **Glob patterns** to identify what should be cleaned based on:
- **Debug/log patterns**: `**/*.{log,debug,tmp}`, `**/debug_*`, `**/temp_*`
- **Artifact patterns**: `**/*.{bak,old,orig}`, `**/node_modules/`, `**/dist/`, `**/build/`
- **Editor patterns**: `**/*.{swp,swo,DS_Store}`, `**/*~`
- **Test artifacts**: `**/coverage/`, `**/.pytest_cache/`, `**/__pycache__/`

Using **Glob tool** to systematically search for cleanup targets:
- Debug/log files with patterns like `**/*.{log,debug,tmp}`
- Temporary files using `**/temp_*`, `**/tmp_*`, `**/*~` patterns
- Failed implementation attempts (identified from conversation context)
- Development artifacts in `**/dist/`, `**/build/`, `**/.cache/`
- Debug statements in code (found using **Grep tool** for `console.log`, `print(`, `fmt.Print`)

**Protected patterns** (NEVER removed):
- The `.claude` directory: `**/.claude/**`
- Git repository: `**/.git/**`
- Essential configs: `package.json`, `requirements.txt`, `Cargo.toml`, etc.
- Source code files unless explicitly identified as temporary

When I find multiple items to clean, I'll use **TodoWrite tool** to create a systematic todo list for safe processing.

Before removing anything found by **Glob/Grep tools**, I'll:
1. Show you what I plan to remove with exact file paths
2. Use **Read tool** to verify file content before deletion
3. Explain why each item should be removed
4. Wait for your confirmation

If the cleanup encounters any errors:
- I'll stop immediately and report what failed
- Ensure partial changes can be rolled back
- Suggest alternative approaches

After cleanup, I'll verify the project still works by:
- Using **Glob tool** to check build/compile status with patterns like `package.json`, `Makefile`
- Running basic sanity checks on remaining files
- Confirming no critical files were affected

This approach uses **native tools** for **better performance** and **safer cleanup** with **consistent patterns** across project types.