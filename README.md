```
 ██████╗██╗      █████╗ ██╗   ██╗██████╗ ███████╗     ██████╗ ██████╗ ██████╗ ███████╗
██╔════╝██║     ██╔══██╗██║   ██║██╔══██╗██╔════╝    ██╔════╝██╔═══██╗██╔══██╗██╔════╝
██║     ██║     ███████║██║   ██║██║  ██║█████╗      ██║     ██║   ██║██║  ██║█████╗  
██║     ██║     ██╔══██║██║   ██║██║  ██║██╔══╝      ██║     ██║   ██║██║  ██║██╔══╝  
╚██████╗███████╗██║  ██║╚██████╔╝██████╔╝███████╗    ╚██████╗╚██████╔╝██████╔╝███████╗
 ╚═════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚═════╝ ╚══════╝     ╚═════╝ ╚═════╝ ╚═════╝ ╚══════╝
                                                                                         
██████╗ ██╗     ██╗   ██╗ ██████╗ ██╗███╗   ██╗███████╗                               
██╔══██╗██║     ██║   ██║██╔════╝ ██║████╗  ██║██╔════╝                               
██████╔╝██║     ██║   ██║██║  ███╗██║██╔██╗ ██║███████╗                               
██╔═══╝ ██║     ██║   ██║██║   ██║██║██║╚██╗██║╚════██║                               
██║     ███████╗╚██████╔╝╚██████╔╝██║██║ ╚████║███████║                               
╚═╝     ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝╚═╝  ╚═══╝╚══════╝                               
```

# Automate the `Boring Stuff`
[![Version](https://img.shields.io/badge/version-1.6.0-blue.svg)](https://github.com/brennercruvinel/CCPlugins)
[![Claude Code CLI](https://img.shields.io/badge/for-Claude%20Code%20CLI-purple.svg)](https://docs.anthropic.com/en/docs/claude-code)
[![Tested on](https://img.shields.io/badge/tested%20on-Opus%204%20%26%20Sonnet%204-orange.svg)](https://claude.ai)
[![Also works with](https://img.shields.io/badge/also%20works%20with-Kimi%20K2-1783ff.svg)](https://github.com/MoonshotAI/Kimi-K2)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](https://github.com/brennercruvinel/CCPlugins/blob/main/CONTRIBUTING.md)

## What is `CCPlugins`?

Productivity commands for Claude Code CLI that `save 2-3 hours per week` on repetitive tasks.

### You know the drill...

🤦 Ask Claude to fix a bug → `Get 15 test files`<br>
😤 Request a simple refactor → `Receive a dissertation on clean code`<br>
🙄 "Please add a button" → `Complete UI framework rewrite`<br>
😭 Every conversation → `"Act like a google engineer who doesn't overengineer"`

CCPlugins is a curated set of commands that extend Claude Code Cli with common development workflows. These commands handle the dumb work, since the agent (opus 4 / sonnet 4 or kimi k2) already knows your codebase, they just tell it what to do with that knowledge.

## Quick Links

- [Installation](#installation) - Get started in 30 seconds
- [Commands](#commands) - See all available commands
- [How It Works](#how-it-works) - Understanding the magic
- [Technical Notes](#technical-notes) - Why conversational design matters
- [Contributing](#contributing) - Help make it better

## Installation

### Quick Install

**Mac/Linux:**
```bash
curl -sSL https://raw.githubusercontent.com/brennercruvinel/CCPlugins/main/install.sh | bash
```

**Windows/Cross-platform:**
```bash
python install.py
```

### Manual Install
```bash
git clone https://github.com/brennercruvinel/CCPlugins.git
cd CCPlugins
python install.py
```

## Commands
Pre-configured commands that make Claude Code work like the senior engineer you keep asking for.

### Development Workflow

*Remove `debug artifacts` and clean up after development sessions*
```
/cleanproject
```



*Analyze changes and create `conventional commit messages`*
```
/commit
```



*Auto-detect and run the `project's code formatter`*
```
/format
```



*Run tests and automatically `fix simple failures`*
```
/test
```
---
### Code Quality

*`Comprehensive code review` for bugs, security, and performance*
```
/review
```



*`Remove obvious comments` while preserving valuable documentation*
```
/remove-comments
```



*Remove TypeScript `any types` and suggest proper types*
```
/cleanup-types
```



*`Fix broken imports` after moving or renaming files*
```
/fix-imports
```



*Find all `TODO`, `FIXME` , and `HACK` comments in your codebase*
```
/find-todos
```
---
### Session Management

*Begin a `documented coding session` with goals tracking*
```
/session-start
```



*`Summarize accomplishments` and prepare handoff notes*
```
/session-end
```
---
### Safety & Performance

*`Rollback last operation` with automatic backup restore*
```
/undo
```



*Cache project context to `speed up` subsequent commands*
```
/context-cache
```


## Real World Example

### Before `/cleanproject`:
```
src/
├── UserService.js
├── UserService.test.js
├── UserService_backup.js    # Old version
├── debug.log               # Debug output
├── test_temp.js           # Temporary test
└── notes.txt              # Dev notes
```

### After `/cleanproject`:
```
src/
├── UserService.js          # Clean production code
└── UserService.test.js     # Actual tests preserved
```

## How It Works

CCPlugins are markdown files that provide intelligent instructions to Claude Code. When you type a command:

1. Claude reads the command definition from `~/.claude/commands/`
2. Analyzes your project context
3. Executes the appropriate actions
4. Provides clear feedback

**Language/Framework Agnostic**: Commands are designed to work with any programming language, framework, or project structure. They analyze your codebase context and adapt accordingly, no framework-specific assumptions or hardcoded patterns that could interfere with your existing setup.

## Technical Notes

### Command Philosophy
Commands are written in **first person** ("I'll help you...") rather than imperative ("Do this..."). This design choice transforms Claude Code from a command executor into a **collaborative assistant**, creating a more conversational and helpful interaction.

```markdown
✅ Good: "I'll analyze your code and fix broken imports..."
❌ Avoid: "Analyze code and fix broken imports..."
```

This approach:
- Makes Claude feel like a `"partner"`, not a tool (and for some reason, it actually works better this way)
- Sets `clear expectations` about what will happen
- Creates a more natural, `human-like interaction`
- `Reduces the intimidation` factor for new users

> **Note:** Basic testing with Kimi K2 shows excellent compatibility, but more validation and testing is needed to ensure full accuracy across all commands.

### User Commands Indicator
Custom commands appear with a `(user)` tag in Claude Code CLI to distinguish them from built-in commands. This is normal and indicates your commands are properly installed.

```
/commit
    Smart Git Commit (user)    ← Your custom command
/help
    Show help                  ← Built-in command
```

## Time Savings

| Task | Manual Time | With Commands | Time Saved |
|------|-------------|---------------|------------|
| Git commits | 5-10 min | 30 sec | ~9 min |
| Code cleanup | 20-30 min | 1 min | ~25 min |
| Test fixes | 15-20 min | 2-5 min | ~15 min |
| Code review | 20 min | 2 min | ~18 min |
| Rollback mistakes | 10-15 min | 30 sec | ~12 min |

**Average: 2-3 hours saved per week**

## Requirements

- Claude Code CLI
- Python 3.6+ (for installer)
- Git (for version control commands)

## Contributing

We welcome contributions that help developers save time. See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## License

MIT License - see [LICENSE](LICENSE) file for details.


*Built by a developer tired of typing `please act like a senior engineer` in every conversation.*