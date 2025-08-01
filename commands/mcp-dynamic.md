# MCP Dynamic Command

I'll create a custom CCPlugins command based on your project context and requirements.

This is a dynamic command that analyzes your project and generates contextual development tasks.

## What I'll do:

1. **Analyze Project Context**: Examine your codebase structure, technologies, and patterns
2. **Identify Opportunities**: Find areas for automation and improvement
3. **Generate Custom Command**: Create a tailored command for your specific needs
4. **Install Command**: Add the new command to your CCPlugins collection

Let me start by analyzing your current project:

```bash
# Check if we're in a project directory
if [ ! -d ".git" ] && [ ! -f "package.json" ] && [ ! -f "setup.py" ] && [ ! -f "pyproject.toml" ] && [ ! -f "Cargo.toml" ] && [ ! -f "go.mod" ]; then
    echo "⚠️  This doesn't appear to be a project directory"
    echo "Please run this command from your project root"
    exit 1
fi

echo "🔍 Analyzing project structure..."
pwd
ls -la

# Detect project type and technologies
echo -e "\n📋 Project Analysis:"

# Check for different project types
if [ -f "package.json" ]; then
    echo "✓ Node.js/JavaScript project detected"
    if command -v jq >/dev/null 2>&1; then
        echo "  Package: $(jq -r '.name // "unknown"' package.json)"
        echo "  Version: $(jq -r '.version // "unknown"' package.json)"
    fi
fi

if [ -f "setup.py" ] || [ -f "pyproject.toml" ] || [ -f "requirements.txt" ]; then
    echo "✓ Python project detected"
fi

if [ -f "Cargo.toml" ]; then
    echo "✓ Rust project detected"
fi

if [ -f "go.mod" ]; then
    echo "✓ Go project detected"
fi

if [ -f "pom.xml" ] || [ -f "build.gradle" ]; then
    echo "✓ Java project detected"
fi

# Check for frameworks and tools
echo -e "\n🛠️  Technologies found:"
[ -d "node_modules" ] && echo "  • Node.js dependencies"
[ -d ".git" ] && echo "  • Git version control"
[ -f "Dockerfile" ] && echo "  • Docker configuration"
[ -f ".github/workflows/"*.yml ] 2>/dev/null && echo "  • GitHub Actions CI/CD"
[ -f "docker-compose.yml" ] && echo "  • Docker Compose"
[ -d ".vscode" ] && echo "  • VS Code configuration"

# Check for existing automation
echo -e "\n⚙️  Existing automation:"
[ -f "Makefile" ] && echo "  • Makefile found"
[ -f "package.json" ] && command -v jq >/dev/null 2>&1 && [ "$(jq '.scripts | length' package.json)" -gt 0 ] && echo "  • npm scripts available"
[ -f "pyproject.toml" ] && echo "  • Python project configuration"

# Look for common patterns that could be automated
echo -e "\n🎯 Automation opportunities:"

# Check for TODOs
todo_count=$(find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.md" \) -not -path "./node_modules/*" -not -path "./.git/*" -exec grep -l "TODO\|FIXME\|HACK" {} \; 2>/dev/null | wc -l)
if [ "$todo_count" -gt 0 ]; then
    echo "  • $todo_count files with TODO comments (could be converted to issues)"
fi

# Check for test files
test_files=$(find . -type f \( -name "*test*" -o -name "*spec*" \) -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null | wc -l)
if [ "$test_files" -gt 0 ]; then
    echo "  • $test_files test files found (could add test automation)"
fi

# Check for documentation
doc_files=$(find . -type f -name "*.md" -not -path "./node_modules/*" -not -path "./.git/*" 2>/dev/null | wc -l)
echo "  • $doc_files documentation files (could add doc generation)"

# Check for code quality tools
if [ -f ".eslintrc.json" ] || [ -f ".eslintrc.js" ] || [ -f "eslint.config.js" ]; then
    echo "  • ESLint configuration found"
fi
if [ -f "pytest.ini" ] || [ -f "pyproject.toml" ]; then
    echo "  • Python testing configuration found"
fi
```

Based on this analysis, I'll suggest and create custom commands that would be most valuable for your project.

## Dynamic Command Generation

Now I'll generate a command tailored to your project's specific needs:

**Usage with arguments:**
```
/mcp-dynamic [command-type] [purpose]
```

**Examples:**
- `/mcp-dynamic test "run all tests and generate coverage report"`
- `/mcp-dynamic deploy "deploy to staging environment"`
- `/mcp-dynamic docs "generate API documentation"`
- `/mcp-dynamic security "scan for vulnerabilities"`

If no arguments are provided, I'll analyze the project and suggest the most beneficial commands to create.

The generated commands will follow CCPlugins conventions:
- Conversational first-person style
- Project-aware and context-sensitive
- Include error handling and validation
- Provide clear feedback
- Integrate with existing tools

This MCP integration extends CCPlugins beyond its current limitations, enabling dynamic command creation based on your actual project needs!