# Find TODOs

I'll locate all TODO comments and unfinished work markers in your codebase using native Claude Code CLI tools for optimal performance.

I'll use the **Grep tool** with regex patterns to efficiently search for various TODO markers across your entire codebase:

I'll search for these patterns using **Grep tool** with efficient regex patterns:
- **TODO/Todo/todo**: General tasks to complete - Pattern: `(?i)\b(?:TODO|FIXME|HACK|XXX|NOTE)\b.*`
- **FIXME/Fixme/fixme**: Known issues that need fixing
- **HACK/Hack/hack**: Temporary workarounds  
- **XXX**: Warnings or problematic code
- **NOTE/Note**: Important notes that might indicate incomplete work

The **Grep tool** will search across all relevant file types using **Glob patterns** to include:
- Source code files: `**/*.{js,ts,jsx,tsx,py,java,cpp,c,h,cs,php,rb,go,rs,swift}`
- Configuration files: `**/*.{json,yaml,yml,toml,ini,cfg}`
- Documentation: `**/*.{md,txt,rst}`
- Excluding: `node_modules/`, `.git/`, `dist/`, `build/`, `target/`

For each marker found using the **Grep tool**, I'll show:
1. **File location** with line number (from grep results)
2. **The full comment** with context
3. **Surrounding code** using **Read tool** to understand what needs to be done
4. **Priority assessment** based on the marker type

I'll organize findings by:
- **Critical** (FIXME, HACK, XXX): Issues that could cause problems
- **Important** (TODO): Features or improvements needed
- **Informational** (NOTE): Context that might need attention

Using **Read tool** for context analysis, I'll also identify:
- TODOs that reference missing implementations
- Placeholder code that needs replacement
- Incomplete error handling
- Stubbed functions awaiting implementation

This approach leverages Claude Code CLI's native tools for **faster performance** on large codebases and **consistent results** across different project types.