# Code Review

I'll review your code for potential issues using Claude Code CLI's native tools for efficient analysis.

I'll use **Glob tool** to identify relevant files and **Read tool** to examine the content, focusing on files we've been working on and any recent changes.

Using **Glob patterns** to target analysis:
- Source files: `**/*.{js,ts,jsx,tsx,py,java,cpp,c,h,cs,php,rb,go,rs,swift}`
- Config files: `**/*.{json,yaml,yml,toml}`
- Excluding: `node_modules/`, `.git/`, `dist/`, `build/`, `target/`, `*.min.js`

For each file found, I'll use **Read tool** to analyze for:

1. **Security Issues**
   - Hardcoded credentials
   - Input validation problems
   - Potential vulnerabilities

2. **Common Bugs**
   - Null/undefined handling
   - Error handling gaps
   - Logic errors

3. **Performance Concerns**
   - Inefficient patterns
   - Memory leaks
   - Unnecessary operations

4. **Code Quality**
   - Dead code
   - Overly complex functions
   - Missing error handling

If I find multiple issues, I'll use **TodoWrite tool** to create a structured todo list for systematic resolution.

For each issue I find using **Read tool** analysis, I'll:
- Show you exactly where it is
- Explain why it's a problem  
- Suggest how to fix it

If I encounter errors during review:
- I'll continue checking other files using **Glob tool**
- Report what couldn't be analyzed
- Focus on the code I can access with **Read tool**

This review leverages native tools for **faster performance** on large projects and **consistent analysis patterns**.