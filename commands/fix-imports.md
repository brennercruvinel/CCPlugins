# Fix Broken Imports

I'll fix import statements that broke after moving or renaming files.

I'll analyze your project to:
1. Detect project type and import patterns
2. Identify broken imports by verifying referenced files exist
3. Find where files were moved by searching matching filenames

For each broken import, I'll:
- Show the broken import and location
- Search for the moved/renamed file
- Fix imports using correct paths

For ambiguous cases with multiple possible matches, I'll list options and ask for clarification rather than guessing.

After fixing, I'll verify syntax correctness and ensure no new conflicts were introduced.