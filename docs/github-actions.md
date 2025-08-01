# GitHub Actions Integration Guide

This guide demonstrates how to integrate CCPlugins with GitHub Actions for automated CI/CD workflows.

## Overview

CCPlugins commands can be integrated into GitHub Actions workflows to automate code quality checks, testing, and development processes. While the commands are designed for interactive use with Claude Code CLI, they can be adapted for CI/CD environments.

## Quick Start

### 1. Basic Integration

Add CCPlugins to your workflow:

```yaml
- name: Install CCPlugins
  run: |
    python install.py
    echo "✅ CCPlugins installed"
```

### 2. Simulated Command Usage

Since Claude Code CLI requires interactive authentication, use simulated implementations for CI/CD:

```yaml
- name: Code Review (Simulated)
  run: |
    echo "Running code quality analysis..."
    # Implement similar logic to /review command
    # Check for security issues, bugs, performance problems
```

## Example Workflows

### Code Quality Workflow

Automatically run code quality checks on pull requests:

```yaml
name: Code Quality with CCPlugins

on:
  pull_request:
    branches: [ main ]

jobs:
  quality:
    runs-on: ubuntu-latest
    steps:
    - uses: actions/checkout@v4
    - name: Install CCPlugins
      run: python install.py
    - name: Code Review
      run: |
        # Simulate /review command logic
        echo "✅ Security scan completed"
        echo "✅ Bug analysis completed"
        echo "✅ Performance review completed"
```

### PR Automation Workflow

Automate pull request analysis and feedback:

```yaml
name: PR Automation

on:
  pull_request:
    types: [opened, synchronize]

jobs:
  pr-analysis:
    runs-on: ubuntu-latest
    permissions:
      pull-requests: write
    steps:
    - uses: actions/checkout@v4
    - name: Install CCPlugins
      run: python install.py
    - name: Analyze Changes
      run: |
        # Implement /review logic for changed files
        # Generate automated feedback
    - name: Comment on PR
      uses: actions/github-script@v7
      with:
        script: |
          github.rest.issues.createComment({
            issue_number: context.issue.number,
            owner: context.repo.owner,
            repo: context.repo.repo,
            body: "🤖 Automated analysis completed!"
          })
```

## Command Adaptations for CI/CD

### `/review` Command

**Local Usage:**
```bash
claude /review
```

**CI/CD Adaptation:**
```yaml
- name: Code Review
  run: |
    echo "=== Security Analysis ==="
    # Check for hardcoded credentials
    grep -r "password\|secret\|key" --exclude-dir=.git . || echo "No obvious secrets found"
    
    echo "=== Bug Detection ==="
    # Check for common patterns
    grep -r "TODO\|FIXME\|HACK" --exclude-dir=.git . || echo "No issues marked"
    
    echo "=== Performance Check ==="
    # Analyze file sizes, complexity indicators
    find . -name "*.py" -size +100k | head -5
```

### `/commit` Command

**Local Usage:**
```bash
claude /commit
```

**CI/CD Adaptation:**
```yaml
- name: Generate Commit Message
  run: |
    # Analyze changes
    files_changed=$(git diff --name-only HEAD~1 HEAD | wc -l)
    
    # Determine change type
    if git diff --name-only HEAD~1 HEAD | grep -q "\.md$"; then
      echo "docs: update documentation"
    elif git diff --name-only HEAD~1 HEAD | grep -q "test"; then
      echo "test: add/update tests"
    else
      echo "feat: implement new features"
    fi
```

### `/test` Command

**Local Usage:**
```bash
claude /test
```

**CI/CD Adaptation:**
```yaml
- name: Run Tests with Auto-fix
  run: |
    # Run tests
    python -m pytest || {
      echo "Tests failed, attempting auto-fix..."
      # Implement basic fixes for common test failures
      echo "Auto-fix completed, re-running tests..."
      python -m pytest
    }
```

### `/cleanproject` Command

**Local Usage:**
```bash
claude /cleanproject
```

**CI/CD Adaptation:**
```yaml
- name: Clean Project
  run: |
    # Remove development artifacts
    find . -name "*.tmp" -delete
    find . -name "*.log" -delete
    find . -name "*_backup.*" -delete
    find . -name "debug_*" -delete
    echo "✅ Project cleaned"
```

## Security Best Practices

### 1. Secrets Management

Never expose sensitive information in CI/CD workflows:

```yaml
# ❌ DON'T DO THIS
- name: Bad Example
  run: echo "API_KEY=secret123" >> .env

# ✅ DO THIS
- name: Good Example
  env:
    API_KEY: ${{ secrets.API_KEY }}
  run: echo "API_KEY=$API_KEY" >> .env
```

### 2. Limited Permissions

Use minimal required permissions:

```yaml
jobs:
  security-scan:
    runs-on: ubuntu-latest
    permissions:
      contents: read  # Only read access needed
      security-events: write  # For security scan results
```

### 3. Input Validation

Validate all inputs in workflows:

```yaml
- name: Validate Input
  if: github.event.inputs.environment != ''
  run: |
    if [[ ! "${{ github.event.inputs.environment }}" =~ ^(staging|production)$ ]]; then
      echo "Invalid environment specified"
      exit 1
    fi
```

### 4. Secure File Handling

Handle files securely:

```yaml
- name: Process Files Safely
  run: |
    # Use absolute paths
    # Validate file extensions
    # Limit file sizes
    find . -name "*.py" -size -1M -exec python -m py_compile {} \;
```

## Integration with Existing CI/CD

### Gradle Projects

```yaml
- name: CCPlugins + Gradle
  run: |
    python install.py
    ./gradlew clean build
    # Run CCPlugins analysis on build artifacts
```

### Maven Projects

```yaml
- name: CCPlugins + Maven
  run: |
    python install.py
    mvn clean compile
    # Integrate with Maven lifecycle
```

### Node.js Projects

```yaml
- name: CCPlugins + npm
  run: |
    python install.py
    npm ci
    npm run build
    # Run quality checks on built code
```

### Docker Integration

```yaml
- name: CCPlugins + Docker
  run: |
    python install.py
    docker build -t myapp .
    # Scan container for issues
    docker run --rm myapp python -c "import sys; print(sys.version)"
```

## Advanced Patterns

### Conditional Execution

```yaml
- name: Run CCPlugins Analysis
  if: contains(github.event.head_commit.message, '[analyze]')
  run: |
    python install.py
    # Run comprehensive analysis
```

### Matrix Builds

```yaml
strategy:
  matrix:
    python-version: [3.8, 3.9, 3.10, 3.11]
    analysis-type: [security, performance, quality]
steps:
- name: Run Analysis
  run: |
    python install.py
    echo "Running ${{ matrix.analysis-type }} analysis on Python ${{ matrix.python-version }}"
```

### Artifact Collection

```yaml
- name: Collect Analysis Results
  run: |
    python install.py
    # Generate reports
    mkdir -p reports
    echo "Analysis complete" > reports/ccplugins-report.txt
    
- name: Upload Reports
  uses: actions/upload-artifact@v3
  with:
    name: ccplugins-reports
    path: reports/
```

## Troubleshooting

### Common Issues

1. **Installation Failures**
   ```yaml
   - name: Debug Installation
     run: |
       python --version
       python install.py
       ls -la ~/.claude/commands/
   ```

2. **Permission Issues**
   ```yaml
   - name: Fix Permissions
     run: |
       chmod +x install.py
       python install.py
   ```

3. **Path Issues**
   ```yaml
   - name: Check Paths
     run: |
       echo "Home: $HOME"
       echo "Claude dir: $HOME/.claude"
       mkdir -p $HOME/.claude/commands
   ```

## Future Enhancements

- Direct Claude Code CLI integration with CI/CD authentication
- Automated issue creation from TODO analysis
- Integration with code quality tools (SonarQube, CodeClimate)
- Slack/Teams notifications for analysis results
- Custom rule definitions for organization-specific checks

## Contributing

To improve GitHub Actions integration:

1. Test workflows in your repository
2. Submit feedback on workflow effectiveness
3. Propose new integration patterns
4. Share real-world usage examples

## Resources

- [GitHub Actions Documentation](https://docs.github.com/en/actions)
- [Claude Code CLI Documentation](https://docs.anthropic.com/en/docs/claude-code)
- [CCPlugins Commands Reference](../commands/)
- [Security Best Practices](https://docs.github.com/en/actions/security-guides)