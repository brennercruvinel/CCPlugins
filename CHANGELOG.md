# Changelog

All notable changes to CCPlugins will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- **MCP Integration**: Model Context Protocol server for external tool connectivity
  - `/mcp-dynamic` - Dynamic command generation based on project context
  - `/project-sync` - Multi-platform task synchronization (Jira, Linear, GitHub)
  - Jira integration for issue creation and management
  - Linear integration for issue tracking
  - Enhanced GitHub operations beyond basic API
  - Project scaffolding with multiple templates (Python CLI, Web App, API Service, Claude Plugin)
  - Context analysis for intelligent automation recommendations
- `/undo` - Rollback last destructive operation with backup support
- `/make-it-pretty` - Improve code readability without changing functionality (includes type improvements)
- `/todos-to-issues` - Convert TODO comments to GitHub issues automatically
- `/human-mode` - Switch to pragmatic mode for practical solutions
- Enhanced error handling across all commands
- Ambiguity checking for `/fix-imports` command
- Automatic backup creation in `/cleanproject`
- Uninstall scripts (uninstall.py and uninstall.sh) for easy removal
- TodoWrite integration in commands that process multiple items
- Prompt before overwriting existing commands during installation

### Changed
- Installation now includes MCP commands and features
- README updated with MCP integration documentation
- Enhanced installer output with MCP feature highlights

### Removed
- `/context-cache` - Removed as Claude Code already maintains context automatically
- `/cleanup-types` - Merged functionality into `/make-it-pretty`
- Automatic backup folders during installation (was creating unnecessary duplicates)

### Changed
- Improved error handling and recovery instructions in all commands
- Commands now report failures gracefully and suggest alternatives
- Maintained minimalist approach without framework-specific assumptions
- Enhanced README with clearer technical explanation of how commands work
- Added advanced usage examples and limitations section to documentation

### Fixed
- **Critical**: `/cleanproject` no longer attempts to remove `.claude` directory (#5)
- `/cleanproject` now explicitly protects critical directories (.claude, .git)
- `/commit` no longer adds Claude signatures or co-authorship to commits
- `/format` and `/test` commands now properly detect tools without assuming specific languages
- Removed all language-specific references for true framework agnosticism
- Fixed md5sum compatibility issue for macOS in `/context-cache`
- Replaced framework-specific directory patterns with generic ones
- Removed hardcoded file extensions from commands
- Fixed curl installation error on Linux - install script now downloads command files from GitHub directly instead of expecting local files

## [1.6.0] - 2025-01-25

### Added
- Basic testing with Kimi K2 compatibility
- Cross-platform installation support (Windows/Mac/Linux)
- 11 productivity commands for common development workflows
- `/cleanproject` - Remove debug artifacts and clean up after development sessions
- `/commit` - Analyze changes and create conventional commit messages
- `/format` - Auto-detect and run the project's code formatter
- `/test` - Run tests and automatically fix simple failures
- `/review` - Comprehensive code review for bugs, security, and performance
- `/remove-comments` - Remove obvious comments while preserving valuable documentation
- `/cleanup-types` - Remove TypeScript 'any' types and suggest proper types (now part of `/make-it-pretty`)
- `/fix-imports` - Fix broken imports after moving or renaming files
- `/find-todos` - Find all TODO, FIXME, and HACK comments in your codebase
- `/session-start` - Begin a documented coding session with goals tracking
- `/session-end` - Summarize accomplishments and prepare handoff notes

### Changed
- Improved README with better examples and time-saving metrics
- Enhanced installation process with automatic backup of existing commands

### Fixed
- Installation script compatibility across different operating systems

## [1.5.0] - 2025-12-15

### Added
- Initial release with core command set
- Python-based installer
- Shell script for Unix-like systems

[Unreleased]: https://github.com/brennercruvinel/CCPlugins/compare/v1.6.0...HEAD
[1.6.0]: https://github.com/brennercruvinel/CCPlugins/compare/v1.5.0...v1.6.0
[1.5.0]: https://github.com/brennercruvinel/CCPlugins/releases/tag/v1.5.0
