# Find TODOs

I'll locate all TODO comments and unfinished work markers in your codebase, using conversation context and available resources.

First, let me scan for various TODO patterns, focusing on files we've been working on and using `@file` references where relevant:

```bash
# Common TODO patterns across different languages
echo "Searching for TODOs, FIXMEs, and other markers..."

# Count different types based on project structure
echo "Analyzing codebase for markers..."

# Results will be shown after analysis
```

I'll search for these patterns:
- **TODO/Todo/todo**: General tasks to complete
- **FIXME/Fixme/fixme**: Known issues that need fixing
- **HACK/Hack/hack**: Temporary workarounds
- **XXX**: Warnings or problematic code
- **NOTE/Note**: Important notes that might indicate incomplete work
- Various comment styles based on your project's languages

For each marker found, I'll show:
1. **File location** with line number (using `@file` references when possible)
2. **The full comment** with context from our conversation
3. **Surrounding code** to understand what needs to be done
4. **Priority assessment** based on the marker type and our recent work

I'll organize findings by:
- **Critical** (FIXME, HACK, XXX): Issues that could cause problems
- **Important** (TODO): Features or improvements needed
- **Informational** (NOTE): Context that might need attention

I'll also identify:
- TODOs that reference missing implementations
- Placeholder code that needs replacement
- Incomplete error handling
- Stubbed functions awaiting implementation

This helps you track and prioritize unfinished work in your codebase, leveraging conversation context and Claude Code CLI's understanding of your project to provide more intelligent insights.