# CCPlugins MCP Integration

This directory contains the Model Context Protocol (MCP) server implementation for CCPlugins, enabling external tool connectivity and dynamic command generation.

## What is MCP?

Model Context Protocol allows Claude Code CLI to connect with external tools and services, extending functionality beyond built-in capabilities. The CCPlugins MCP server provides:

- **External Tool Integration**: Connect with Jira, Linear, GitHub API, and other development tools
- **Dynamic Command Generation**: Create context-aware commands based on project analysis
- **Advanced Template System**: Generate project scaffolding and boilerplate code
- **Resource Management**: Access project context and configuration data

## Quick Start

### 1. Installation

The MCP server is included with CCPlugins. Install CCPlugins first:

```bash
# Install CCPlugins
python install.py

# The MCP server files are in the mcp/ directory
```

### 2. Configuration

Configure Claude Desktop to use the CCPlugins MCP server by adding to your Claude Desktop configuration file:

**Location:**
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`
- Linux: `~/.config/claude/claude_desktop_config.json`

**Configuration:**
```json
{
  "mcpServers": {
    "ccplugins": {
      "command": "python",
      "args": ["/path/to/ccplugins/mcp/server.py"],
      "cwd": "/path/to/ccplugins",
      "env": {
        "JIRA_URL": "https://your-domain.atlassian.net",
        "JIRA_EMAIL": "your-email@example.com",
        "JIRA_API_TOKEN": "your-jira-api-token",
        "LINEAR_API_TOKEN": "your-linear-api-token",
        "GITHUB_TOKEN": "your-github-token"
      }
    }
  }
}
```

Replace `/path/to/ccplugins` with the actual path to your CCPlugins installation.

### 3. Environment Variables

Set up environment variables for external tool integrations:

```bash
# Jira Integration
export JIRA_URL="https://your-domain.atlassian.net"
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your-jira-api-token"

# Linear Integration
export LINEAR_API_TOKEN="your-linear-api-token"

# GitHub Integration (optional, gh CLI used if available)
export GITHUB_TOKEN="your-github-token"
```

## Available Tools

### Jira Integration

Create and manage Jira issues directly from Claude Code CLI:

```python
# Create a new issue
jira_create_issue(
    summary="Fix bug in authentication flow",
    description="Detailed description of the bug",
    project="PROJ",
    issue_type="Bug"
)
```

### Linear Integration

Integrate with Linear for issue tracking:

```python
# Create a Linear issue
linear_create_issue(
    title="Implement new feature",
    description="Feature description",
    team_id="team-id",
    priority=2
)
```

### Advanced GitHub Operations

Extended GitHub functionality beyond the basic todos-to-issues command:

```python
# Bulk operations on GitHub issues
github_advanced(
    operation="bulk_create",
    data={
        "issues": [
            {
                "title": "Issue 1",
                "body": "Description",
                "labels": ["bug", "urgent"]
            }
        ]
    }
)
```

### Project Scaffolding

Generate new projects from templates:

```python
# Create a new project
project_scaffold(
    template="python-cli",
    name="my-new-tool",
    options={
        "author_name": "Your Name",
        "author_email": "you@example.com"
    }
)
```

### Context Analysis

Analyze project structure for dynamic command generation:

```python
# Analyze current project
context_analyze(
    path=".",
    analysis_type="general"
)
```

## Dynamic Commands

The MCP integration enables dynamic command creation through the `/mcp-dynamic` command:

```bash
# In Claude Code CLI
/mcp-dynamic

# Or with specific parameters
/mcp-dynamic test "create comprehensive test suite"
/mcp-dynamic deploy "setup deployment pipeline"
```

This command:
1. Analyzes your project structure and technologies
2. Identifies automation opportunities
3. Generates custom CCPlugins commands
4. Installs them for immediate use

## Available Templates

The scaffolding system includes these built-in templates:

- **python-cli**: Python command-line application
- **web-app**: Web application starter (Node.js/Express)
- **api-service**: REST API service
- **claude-plugin**: Claude Code CLI plugin template

## Resources

The MCP server provides these resources:

- `ccplugins://project/context` - Current project analysis
- `ccplugins://templates/list` - Available project templates
- `ccplugins://tools/config` - External tool configuration status

## Prompts

Available MCP prompts for enhanced functionality:

- `create_command` - Generate new CCPlugins commands
- `optimize_workflow` - Suggest workflow improvements

## Troubleshooting

### Common Issues

1. **Server not starting**: Check Python path and dependencies
2. **Tool integrations not working**: Verify environment variables are set
3. **Commands not appearing**: Restart Claude Desktop after configuration changes

### Debugging

Enable debug logging by checking `/tmp/ccplugins-mcp.log`:

```bash
tail -f /tmp/ccplugins-mcp.log
```

### Testing the Server

Test the MCP server manually:

```bash
cd /path/to/ccplugins
python mcp/server.py
```

Then send a test request:

```json
{"jsonrpc": "2.0", "method": "initialize", "params": {}, "id": 1}
```

## Integration Examples

### Example 1: Automated Issue Creation from TODOs

```markdown
# In a custom command
I'll scan for TODO comments and create issues in both Jira and Linear:

1. Find all TODO comments in the codebase
2. Create Jira issues for backend TODOs
3. Create Linear issues for frontend TODOs
4. Update the code comments with issue references
```

### Example 2: Project Health Check

```markdown
# Custom health check command
I'll analyze your project and create improvement tasks:

1. Check for missing documentation
2. Verify CI/CD setup
3. Scan for security issues
4. Create GitHub issues for each improvement needed
```

### Example 3: Release Automation

```markdown
# Release preparation command
I'll prepare your project for release:

1. Update version numbers
2. Generate changelog from git history
3. Create GitHub release
4. Update project documentation
```

## API Reference

For detailed API documentation, see the individual integration files:

- `integrations/jira.py` - Jira API wrapper
- `integrations/linear.py` - Linear API wrapper
- `integrations/github_advanced.py` - Enhanced GitHub operations
- `templates/scaffolder.py` - Project scaffolding system

## Contributing

To add new integrations or templates:

1. Create integration file in `integrations/`
2. Add tool definition to `server.py`
3. Update this documentation
4. Test with Claude Desktop

For templates:
1. Add template function to `scaffolder.py`
2. Create template files in `templates/[template-name]/`
3. Include `template.json` configuration
4. Test scaffolding process