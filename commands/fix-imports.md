# Fix Broken Imports

I'll help fix import statements that broke after moving or renaming files.

First, let me analyze your project structure and identify any broken imports. I'll:

1. **Detect your project type** from file patterns and configurations
2. **Identify import/include patterns** specific to your language
3. **Check which imports are broken** by verifying if referenced files exist
4. **Find where files were moved** by searching for matching filenames

Based on what I find, I'll:
- Detect the import patterns used in your project
- Handle the specific syntax for your language
- Preserve your existing code style

If I find multiple broken imports, I'll create a todo list to fix them systematically.

For each broken import, I'll:
1. Show you the broken import with its location
2. Search for the moved/renamed file
3. Check for ambiguous matches

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