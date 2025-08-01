# Example Hooks Configurations

This directory contains example hook configurations for popular formatters and tools.

## Quick Setup

Copy the appropriate configuration to your `~/.claude/config.json` file.

## JavaScript/TypeScript Projects

### Prettier Only
```bash
cp examples/prettier.config.json ~/.claude/config.json
```

### ESLint + Prettier
```bash
cp examples/eslint-prettier.config.json ~/.claude/config.json
```

## Python Projects

### Black Only
```bash
cp examples/black.config.json ~/.claude/config.json
```

### Black + isort
```bash
cp examples/black-isort.config.json ~/.claude/config.json
```

## Multi-Language Projects

### Auto-detect Formatters
```bash
cp examples/multi-language.config.json ~/.claude/config.json
```

## Custom Setups

### Project-Specific Formatting
```bash
cp examples/conditional.config.json ~/.claude/config.json
```

For more detailed configuration options and troubleshooting, see the [main hooks guide](../HOOKS.md).