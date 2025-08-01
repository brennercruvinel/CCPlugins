# Code Review

I'll review your code for potential issues using available context and resources.

Let me examine the relevant files using `@file` references where available, recent changes, and our conversation history to understand what we've been working on. I'll focus my review on:

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

If I find multiple issues, I'll create a todo list to address them systematically, taking into account our conversation context and any patterns we've established.

For each issue I find, I'll:
- Show you exactly where it is using `@file` references when possible
- Explain why it's a problem in the context of our project
- Suggest how to fix it based on established patterns and preferences
- Consider our conversation history for context-aware recommendations

If I encounter errors during review:
- I'll continue checking other files
- Report what couldn't be analyzed
- Focus on the code I can access

This review focuses on real problems that could affect your application, leveraging available context from our conversation and Claude Code CLI's resource discovery to provide more intelligent, contextually-aware feedback.