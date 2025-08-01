# Auto Format Code

I'll format your code using the project's configured formatter.

First, let me check if this project has a formatter configured by analyzing:
- Configuration files in the project root
- Build or task runner setups
- Editor configuration files
- Code style definitions

Based on what I find, I'll determine the appropriate formatting approach for your project.

I'll format only the files that have been modified to:
- Avoid unnecessary changes
- Keep the formatting focused
- Prevent touching vendor/dependency directories

After formatting, I'll show you what changed.

If no formatter is found:
- I'll list what I searched for
- Suggest popular formatters for your project type
- Ask if you'd like me to format manually using language conventions

If formatting fails:
- I'll show the exact error
- Explain what might be wrong
- Suggest fixes or alternatives

This ensures consistent code style according to your project's standards.

## Automatic Formatting with Hooks

For seamless formatting on every code change, consider setting up Claude Code CLI hooks. This will automatically format code after Edit/MultiEdit/Write operations without manual intervention.

See the [Hooks Integration Guide](../HOOKS.md) for setup instructions and examples for popular formatters like Prettier, Black, ESLint, and more.

**Quick Setup Example:**
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [{
        "type": "command", 
        "command": "npx prettier --write \"$file_path\""
      }]
    }]
  }
}
```

Add this to `~/.claude/config.json` to automatically format JavaScript/TypeScript files.