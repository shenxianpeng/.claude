Create a new $ARGUMENTS

Steps:
1. **Identify type** – determine from the argument what is being created (function, class, module, CLI script, API endpoint, test file, etc.)
2. **Gather context** – read CLAUDE.md and any closely related existing files to understand conventions, naming patterns, and project structure
3. **Scaffold** – generate the new file (or code block) with:
   - Correct location in the project tree
   - Appropriate imports and dependencies
   - Docstrings / type hints following project conventions
   - Placeholder logic with `TODO` comments where implementation is needed
   - A matching test file skeleton if the project uses tests
4. **Wire up** – if the new item needs to be registered somewhere (e.g. added to `__init__.py`, a router, a config file), make those connections
5. **Summarise** – list every file created or modified and explain what still needs to be implemented

Follow the existing code style and do not introduce new dependencies unless absolutely necessary.
