# TODOs to GitHub Issues

I'll scan your codebase for TODO comments and create GitHub issues automatically using Claude Code CLI's native tools for efficient scanning.

First, I'll verify GitHub repository setup using **Read tool** to check configuration:

I'll check for:
- `.git/config` using **Read tool** to verify GitHub remote
- GitHub CLI availability (I'll note if `gh` is needed)
- Authentication status (I'll guide you if setup is needed)

**TODO Discovery using native tools**:
- Use **Grep tool** with pattern: `(?i)\b(?:TODO|FIXME|HACK)\b.*`
- Target **Glob patterns**: `**/*.{js,ts,py,java,cpp,c,h,cs,php,rb,go,rs,swift,md}`
- Exclude: `node_modules/`, `.git/`, `dist/`, `build/`

**Context analysis using Read tool**:
For each TODO found by **Grep tool**, I'll use **Read tool** to extract surrounding code context.

When I find multiple TODOs using **Grep tool**, I'll use **TodoWrite tool** to track which ones have been converted to issues.

For each TODO found, I'll:
1. Use **Read tool** to extract the comment content and surrounding code context
2. Create a descriptive issue title based on the TODO content
3. Include file location and context in the issue body
4. Add appropriate labels (bug, enhancement, etc.)
5. Create the issue on GitHub using available tools

I'll handle rate limits and show you a summary of all created issues.

This approach uses **native tools** for **faster TODO discovery** and **systematic issue creation** with **consistent formatting**.