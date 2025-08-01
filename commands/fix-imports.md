# Fix Broken Imports

I'll help fix import statements that broke after moving or renaming files.

First, let me analyze your project structure and identify any broken imports using available context and resources. I'll:

1. **Leverage project context** from Claude Code CLI's resource discovery and our conversation
2. **Use `@file` references** to examine specific files we've been working on
3. **Identify import/include patterns** specific to your language and established conventions
4. **Check which imports are broken** by verifying if referenced files exist
5. **Find where files were moved** using contextual awareness of recent changes

Based on what I find and our conversation context, I'll:
- Use Claude Code CLI's understanding of the project to detect import patterns
- Handle the specific syntax for your language based on established patterns
- Preserve your existing code style and conventions we've been following

If I find multiple broken imports, I'll create a todo list to fix them systematically.

For each broken import, I'll:
1. Show you the broken import with its location using `@file` references
2. Search for the moved/renamed file using conversation context
3. Check for ambiguous matches considering our recent work

**For ambiguous cases:**
- If multiple files could match the import
- I'll list all possible options
- Show you the context
- Ask which file is the correct target
- Never guess when unsure

**Error handling:**
- If an import can't be resolved
- I'll report why it failed
- Continue with other fixable imports
- Suggest manual fixes if needed

After fixing imports:
- Verify the syntax is correct
- Ensure no new conflicts were introduced
- Report summary of changes made

This ensures your code continues to work after file reorganization with safety and clarity.