# Project Sync

I'll help you synchronize your development tasks across multiple platforms using MCP integrations.

This command demonstrates the power of CCPlugins MCP integration by connecting with external tools like Jira, Linear, and GitHub to create a unified development workflow.

## What I'll do:

1. **Analyze Project Context**: Scan your codebase for development tasks
2. **Cross-Platform Sync**: Create corresponding tasks in your project management tools
3. **Maintain Traceability**: Link tasks across platforms for easy tracking
4. **Generate Reports**: Provide status updates across all platforms

Let me start by checking your MCP tool configurations:

```bash
# Check if we're in a project directory
if [ ! -d ".git" ]; then
    echo "❌ Not a git repository. Please run this command from your project root."
    exit 1
fi

echo "🔍 Checking MCP tool configurations..."

# Check GitHub CLI availability
if command -v gh &> /dev/null; then
    if gh auth status &>/dev/null; then
        echo "✅ GitHub CLI configured and authenticated"
        GITHUB_READY=true
    else
        echo "⚠️  GitHub CLI found but not authenticated. Run: gh auth login"
        GITHUB_READY=false
    fi
else
    echo "⚠️  GitHub CLI not found. Install from: https://cli.github.com"
    GITHUB_READY=false
fi

# Check environment variables for external tools
echo -e "\n🔧 External tool configurations:"

if [ -n "$JIRA_URL" ] && [ -n "$JIRA_EMAIL" ] && [ -n "$JIRA_API_TOKEN" ]; then
    echo "✅ Jira integration configured"
    JIRA_READY=true
else
    echo "⚠️  Jira integration not configured"
    echo "   Set: JIRA_URL, JIRA_EMAIL, JIRA_API_TOKEN"
    JIRA_READY=false
fi

if [ -n "$LINEAR_API_TOKEN" ]; then
    echo "✅ Linear integration configured"
    LINEAR_READY=true
else
    echo "⚠️  Linear integration not configured"
    echo "   Set: LINEAR_API_TOKEN"
    LINEAR_READY=false
fi

# Check if CCPlugins MCP server is available
if [ -f "$(dirname $(dirname $(readlink -f ~/.claude/commands/commit.md 2>/dev/null || echo ~/.claude/commands/../..)))/mcp/server.py" ]; then
    echo "✅ CCPlugins MCP server available"
    MCP_READY=true
else
    echo "⚠️  CCPlugins MCP server not found"
    MCP_READY=false
fi
```

Now I'll scan your project for development tasks and synchronize them across platforms:

```bash
echo -e "\n📋 Scanning project for development tasks..."

# Find TODO comments
echo "🔍 Finding TODO comments..."
TODO_FILES=$(find . -type f \( -name "*.py" -o -name "*.js" -o -name "*.ts" -o -name "*.java" -o -name "*.go" -o -name "*.rs" -o -name "*.cpp" -o -name "*.c" -o -name "*.md" \) -not -path "./node_modules/*" -not -path "./.git/*" -not -path "./vendor/*" -not -path "./target/*" -exec grep -l "TODO\|FIXME\|HACK\|XXX" {} \; 2>/dev/null)

if [ -n "$TODO_FILES" ]; then
    TODO_COUNT=$(echo "$TODO_FILES" | wc -l)
    echo "  Found $TODO_COUNT files with TODO comments"
    
    # Show sample TODOs
    echo -e "\n📝 Sample TODOs found:"
    echo "$TODO_FILES" | head -3 | while read file; do
        echo "  📄 $file:"
        grep -n "TODO\|FIXME\|HACK\|XXX" "$file" | head -2 | sed 's/^/    /'
    done
else
    echo "  No TODO comments found"
    TODO_COUNT=0
fi

# Check for open GitHub issues
if [ "$GITHUB_READY" = true ]; then
    echo -e "\n🐙 Checking GitHub issues..."
    GH_ISSUES=$(gh issue list --state open --json number,title,labels 2>/dev/null || echo "[]")
    GH_ISSUE_COUNT=$(echo "$GH_ISSUES" | jq length 2>/dev/null || echo 0)
    echo "  Found $GH_ISSUE_COUNT open GitHub issues"
fi

# Analyze project structure for potential improvements
echo -e "\n🏗️  Analyzing project structure..."

# Check for missing standard files
MISSING_FILES=()
[ ! -f "README.md" ] && MISSING_FILES+=("README.md")
[ ! -f "LICENSE" ] && [ ! -f "LICENSE.txt" ] && [ ! -f "LICENSE.md" ] && MISSING_FILES+=("LICENSE")
[ ! -f ".gitignore" ] && MISSING_FILES+=(".gitignore")
[ ! -f "CONTRIBUTING.md" ] && MISSING_FILES+=("CONTRIBUTING.md")
[ ! -f "CHANGELOG.md" ] && [ ! -f "CHANGELOG.txt" ] && MISSING_FILES+=("CHANGELOG.md")

if [ ${#MISSING_FILES[@]} -gt 0 ]; then
    echo "  Missing standard files: ${MISSING_FILES[*]}"
fi

# Check for CI/CD setup
if [ -d ".github/workflows" ] && [ -n "$(ls .github/workflows/*.yml 2>/dev/null)" ]; then
    echo "  ✅ GitHub Actions workflows found"
else
    echo "  ⚠️  No GitHub Actions workflows found"
fi

# Check for testing setup
TEST_INDICATORS=("test" "spec" "pytest.ini" "jest.config" "karma.conf")
TEST_FOUND=false
for indicator in "${TEST_INDICATORS[@]}"; do
    if find . -name "*$indicator*" -not -path "./node_modules/*" -not -path "./.git/*" | grep -q .; then
        TEST_FOUND=true
        break
    fi
done

if [ "$TEST_FOUND" = true ]; then
    echo "  ✅ Testing setup found"
else
    echo "  ⚠️  No testing setup detected"
fi
```

## Cross-Platform Task Synchronization

Based on the analysis, I'll now create synchronized tasks across your configured platforms:

**If you have configured external tools**, I would:

1. **Convert TODOs to Issues**:
   - Create GitHub issues for each TODO comment
   - Create Jira tasks for backend/infrastructure TODOs
   - Create Linear issues for frontend/UI TODOs
   - Link all issues with cross-references

2. **Create Improvement Tasks**:
   - Missing documentation → Documentation epic in Jira
   - Missing CI/CD → DevOps story in Linear
   - Missing tests → QA tasks across platforms

3. **Generate Project Board**:
   - Create GitHub project board
   - Organize tasks by priority and area
   - Link to external tool issues

4. **Setup Automation**:
   - Create webhooks for status synchronization
   - Generate reports combining all platforms
   - Set up notification routing

## Example Synchronization Report

```
📊 Project Sync Summary
======================

📋 Tasks Created:
• GitHub Issues: 8 created
• Jira Stories: 3 created  
• Linear Issues: 5 created

🔗 Cross-References:
• TODO-001 → GitHub #123 → PROJ-456 → LIN-789
• TODO-002 → GitHub #124 → LIN-790

📈 Next Steps:
1. Review prioritization in Jira
2. Assign team members in Linear
3. Update GitHub project board
4. Schedule sprint planning
```

## Configuration Help

To enable full functionality, configure these integrations:

**Jira Setup:**
```bash
export JIRA_URL="https://your-domain.atlassian.net"
export JIRA_EMAIL="your-email@example.com"
export JIRA_API_TOKEN="your-api-token"
```

**Linear Setup:**
```bash
export LINEAR_API_TOKEN="your-linear-api-token"
```

**GitHub Setup:**
```bash
gh auth login
```

This command showcases how CCPlugins MCP integration extends beyond Claude Code CLI's limitations, providing real connectivity to your development ecosystem!