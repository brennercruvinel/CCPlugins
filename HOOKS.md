# Claude Code CLI Hooks Integration

This guide explains how to integrate CCPlugins with Claude Code CLI's hooks system for automatic code formatting and other post-processing tasks.

## What are Hooks?

Hooks in Claude Code CLI allow you to automatically run commands after certain tool operations. This is particularly useful for:
- **Automatic code formatting** after Edit/MultiEdit/Write operations
- **Linting fixes** after code changes
- **Import organization** after file modifications
- **Custom post-processing** workflows

## Setup

### 1. Create Claude Code CLI Configuration

Create or edit your Claude Code CLI configuration file at `~/.claude/config.json`:

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

**🚀 Quick Start:** Check out the [example configurations](examples/) for ready-to-use setups for popular formatters.

### 2. Hook Configuration Structure

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "ToolName1|ToolName2",
      "hooks": [
        {
          "type": "command",
          "command": "your-formatting-command \"$file_path\""
        }
      ]
    }]
  }
}
```

**Key Components:**
- `PostToolUse`: Runs hooks after tool execution
- `matcher`: Regular expression matching tool names (Edit, MultiEdit, Write, etc.)
- `command`: Shell command to execute
- `$file_path`: Variable containing the path of the modified file

## Example Configurations

### JavaScript/TypeScript with Prettier

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

### JavaScript/TypeScript with ESLint + Prettier

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [
        {
          "type": "command",
          "command": "npx eslint --fix \"$file_path\""
        },
        {
          "type": "command",
          "command": "npx prettier --write \"$file_path\""
        }
      ]
    }]
  }
}
```

### Python with Black

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [{
        "type": "command",
        "command": "black \"$file_path\""
      }]
    }]
  }
}
```

### Python with Black + isort

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [
        {
          "type": "command",
          "command": "isort \"$file_path\""
        },
        {
          "type": "command",
          "command": "black \"$file_path\""
        }
      ]
    }]
  }
}
```

### Go with gofmt

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [{
        "type": "command",
        "command": "gofmt -w \"$file_path\""
      }]
    }]
  }
}
```

### Rust with rustfmt

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [{
        "type": "command",
        "command": "rustfmt \"$file_path\""
      }]
    }]
  }
}
```

### Multi-language Setup

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [
        {
          "type": "command",
          "command": "if [[ \"$file_path\" =~ \\.(js|ts|jsx|tsx)$ ]]; then npx prettier --write \"$file_path\"; fi"
        },
        {
          "type": "command",
          "command": "if [[ \"$file_path\" =~ \\.py$ ]]; then black \"$file_path\"; fi"
        },
        {
          "type": "command",
          "command": "if [[ \"$file_path\" =~ \\.go$ ]]; then gofmt -w \"$file_path\"; fi"
        }
      ]
    }]
  }
}
```

## Integration with CCPlugins Commands

### Enhanced `/format` Command

When hooks are configured, the `/format` command becomes even more powerful:
- Manual formatting still works as before
- Automatic formatting happens after every code modification
- Consistent style across all operations

### Works with All Commands

Hooks integrate seamlessly with all CCPlugins commands that modify code:
- `/fix-imports` - Auto-format after import fixes
- `/remove-comments` - Auto-format after comment cleanup
- `/make-it-pretty` - Double formatting for extra cleanliness
- `/test` - Auto-format test files after modifications

## Best Practices

### 1. Respect Project Configuration

Ensure your formatters respect project-specific configuration:
```json
{
  "type": "command",
  "command": "npx prettier --write \"$file_path\""
}
```
Prettier automatically finds `.prettierrc`, `prettier.config.js`, etc.

### 2. Handle Missing Tools Gracefully

```json
{
  "type": "command", 
  "command": "command -v prettier >/dev/null 2>&1 && npx prettier --write \"$file_path\" || echo 'Prettier not found, skipping formatting'"
}
```

### 3. File Type Filtering

Only format relevant files:
```json
{
  "type": "command",
  "command": "if [[ \"$file_path\" =~ \\.(js|ts|jsx|tsx|json|css|scss|md)$ ]]; then npx prettier --write \"$file_path\"; fi"
}
```

### 4. Performance Considerations

For large projects, consider using formatters' built-in file filtering:
```json
{
  "type": "command",
  "command": "npx prettier --write \"$file_path\" --ignore-path .gitignore"
}
```

## Troubleshooting

### Common Issues

1. **Hook not running**: Check the matcher pattern matches your tool usage
2. **Command not found**: Ensure formatters are installed and in PATH
3. **Permission issues**: Check file permissions and formatter access
4. **Infinite loops**: Avoid hooks that trigger more tool usage

### Debug Hook Execution

Enable Claude Code CLI debug mode to see hook execution:
```bash
export CLAUDE_DEBUG=1
claude your-command
```

### Testing Hooks

Test your hook configuration:
```bash
# Test if your formatter works
npx prettier --write test-file.js

# Test file type detection
if [[ "test.js" =~ \.(js|ts)$ ]]; then echo "matches"; fi
```

## Advanced Configurations

### Conditional Formatting by Project

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write",
      "hooks": [{
        "type": "command",
        "command": "if [ -f package.json ]; then npx prettier --write \"$file_path\"; elif [ -f requirements.txt ]; then black \"$file_path\"; fi"
      }]
    }]
  }
}
```

### Custom Formatting Script

Create a custom script `~/.claude/format-file.sh`:
```bash
#!/bin/bash
file="$1"
extension="${file##*.}"

case "$extension" in
  js|ts|jsx|tsx|json|css|scss|md)
    npx prettier --write "$file"
    ;;
  py)
    black "$file"
    isort "$file"
    ;;
  go)
    gofmt -w "$file"
    ;;
  rs)
    rustfmt "$file"
    ;;
  *)
    echo "No formatter configured for .$extension files"
    ;;
esac
```

Then use it in your hooks:
```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Edit|MultiEdit|Write", 
      "hooks": [{
        "type": "command",
        "command": "~/.claude/format-file.sh \"$file_path\""
      }]
    }]
  }
}
```

## Benefits

✅ **Automatic consistency** - Never commit unformatted code again  
✅ **Zero friction** - Formatting happens transparently  
✅ **Project-aware** - Respects your project's style configuration  
✅ **Tool agnostic** - Works with any formatter or linter  
✅ **Composable** - Combine multiple tools in sequence  

## Learn More

- [Claude Code CLI Hooks Guide](https://docs.anthropic.com/en/docs/claude-code/hooks-guide)
- [Hook Configuration Examples](https://docs.anthropic.com/en/docs/claude-code/hooks-guide#sample-hook-example)
- [CCPlugins Commands Documentation](commands/)