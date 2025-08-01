# Remove Obvious Comments

I'll clean up redundant comments while preserving valuable documentation using Claude Code CLI's native tools for efficient analysis.

I'll use **Glob tool** to identify source files and **Read tool** to analyze comment patterns:

**File targeting with Glob patterns**:
- Source files: `**/*.{js,ts,jsx,tsx,py,java,cpp,c,h,cs,php,rb,go,rs,swift}`
- Recently modified files (if in git repo): Use conversation context
- Exclude: `node_modules/`, `.git/`, `dist/`, `build/`

**Comment analysis using Read tool**:
- JavaScript/TypeScript: `//` and `/* */` comments
- Python: `#` and `"""` docstring comments  
- Java/C++: `//` and `/* */` comments
- Other languages: Appropriate comment syntax

Using **Read tool** analysis, I'll remove comments that:
- Simply restate what the code does
- Add no value beyond the code itself  
- State the obvious (like "constructor" above a constructor)

I'll preserve comments that:
- Explain WHY something is done
- Document complex business logic
- Contain TODOs, FIXMEs, or HACKs (found using **Grep tool**)
- Warn about non-obvious behavior
- Provide important context

For each file with obvious comments found by **Glob/Read tools**, I'll:
1. Show you the redundant comments I found
2. Explain why they should be removed
3. Show the cleaner version
4. Apply the changes after your confirmation

This approach uses **native tools** for **faster comment analysis** and **consistent cleanup patterns** across different programming languages.