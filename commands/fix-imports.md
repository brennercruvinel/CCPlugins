# Fix Broken Imports

I'll help fix import statements that broke after moving or renaming files using Claude Code CLI's native tools for efficient analysis.

I'll use **Glob tool** to analyze your project structure and **Read tool** to examine import statements, then **Grep tool** to locate moved files. Here's my approach:

1. **Detect your project type** using **Glob patterns** to check for:
   - JavaScript/TypeScript: `package.json`, `**/*.{js,ts,jsx,tsx}`
   - Python: `**/*.py`, `requirements.txt`, `pyproject.toml`
   - Java: `**/*.java`, `pom.xml`, `build.gradle`
   - C/C++: `**/*.{c,cpp,h,hpp}`, `CMakeLists.txt`

2. **Identify import patterns** using **Read tool** on files found by **Glob tool**:
   - ES6/CommonJS imports: `import/require` statements
   - Python imports: `import/from` statements  
   - Java imports: `import` statements
   - C++ includes: `#include` statements

3. **Check broken imports** by using **Glob tool** to verify if referenced files exist:
   - Search with patterns like `**/*{filename}*` for relocated files
   - Use **Grep tool** to find matching exports/classes in potential target files

Based on analysis using native tools, I'll:
- Use **Read tool** to examine existing imports and preserve your code style
- Use **Glob tool** to efficiently search for files across the project structure
- Use **Grep tool** to verify exports and class definitions in target files

If I find multiple broken imports, I'll use **TodoWrite tool** to create a systematic todo list for fixing them.

For each broken import found using **Grep tool**, I'll:
1. Show you the broken import with its location
2. Use **Glob tool** to search for the moved/renamed file with patterns like:
   - `**/*{basename}*` - Find files with similar names
   - `**/{dirname}/**` - Search in likely directories
3. Use **Grep tool** to check for ambiguous matches by searching for exports/classes

**For ambiguous cases:**
- If **Glob tool** finds multiple files that could match the import
- I'll list all possible options using **Read tool** for context
- Show you the context and ask which file is the correct target
- Never guess when unsure

**Error handling:**
- If an import can't be resolved using **Glob/Grep tools**
- I'll report why it failed and continue with other fixable imports
- Suggest manual fixes if needed

After fixing imports using **Read tool** modifications:
- Verify the syntax is correct for your language
- Ensure no new conflicts were introduced
- Report summary of changes made

This approach uses **native Claude Code CLI tools** for **improved performance** on large projects and **consistent file resolution patterns**.