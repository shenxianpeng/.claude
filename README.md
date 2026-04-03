# .claude

A template repository demonstrating the best-practice folder structure for
[Claude Code](https://claude.ai/code) configuration.

## Folder Structure

```
your-project/
├── CLAUDE.md                  # Project instructions read by Claude at session start
├── CLAUDE.local.md            # Personal overrides (gitignored)
└── .claude/
    ├── settings.json          # Shared project settings committed to version control
    ├── settings.local.json    # Personal settings overrides (gitignored)
    ├── commands/              # Custom slash commands available as /project:<name>
    │   ├── commit.md          # /project:commit — generate a conventional commit message
    │   ├── review.md          # /project:review — run a code review
    │   └── test.md            # /project:test   — generate tests for a file or function
    └── .gitignore             # Excludes local-only files from version control
```

## File Reference

### `CLAUDE.md` (project root)

The primary instruction file Claude reads at the beginning of every session.
Keep it under ~200 lines; split large rule-sets into separate files and import
them with `@path/to/file.md` syntax.

Recommended sections:
- **Project Overview** – what the project does
- **Tech Stack** – languages, frameworks, key libraries
- **Common Commands** – build, test, lint, format
- **Code Style & Conventions** – naming, exports, structure
- **Repository Structure** – quick map of important directories
- **Important Notes** – constraints or context Claude must always respect

### `CLAUDE.local.md` (project root, gitignored)

Personal overrides that should not be shared with the team (e.g. local paths,
personal preferences, work-in-progress notes).

### `.claude/settings.json`

Shared project settings committed to version control.  Controls which tools
and shell commands Claude is permitted to use:

```jsonc
{
  "permissions": {
    "allow": [
      "Bash(python *)",
      "Bash(pip install *)",
      "Bash(pytest *)",
      "Bash(pytest)",
      "Bash(ruff check *)",
      "Bash(black *)"
    ],
    "deny": [
      "Bash(rm -rf *)"
    ]
  }
}
```

See the [Claude Code settings docs](https://docs.anthropic.com/en/docs/claude-code/settings)
for the full list of available options.

### `.claude/settings.local.json` (gitignored)

Personal overrides for `settings.json` — same schema, not committed.

### `.claude/commands/`

Markdown files that become **custom slash commands** inside Claude Code.  Each
file is accessible as `/project:<filename-without-extension>`.

| File | Command | Purpose |
|------|---------|---------|
| `commit.md` | `/project:commit` | Generate a conventional commit message for staged changes |
| `review.md` | `/project:review <target>` | Run a structured code review |
| `test.md`   | `/project:test <target>`   | Generate tests for a file or function |

Commands may include `$ARGUMENTS` as a placeholder for user-supplied input.

## Usage

1. **Copy this repository** into the root of your project as `.claude/`:
   ```bash
   cp -r /path/to/.claude-template/.claude  your-project/.claude
   ```
2. **Copy `CLAUDE.md`** to the root of your project and fill in the blanks.
3. **Adjust `settings.json`** to match your project's allowed/denied commands.
4. **Add or remove commands** in `.claude/commands/` to match your workflow.
5. **Add `.claude/settings.local.json` and `CLAUDE.local.md`** to your
   project's `.gitignore` (already handled inside `.claude/.gitignore`).

## Resources

- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
- [CLAUDE.md guide](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Custom slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Settings reference](https://docs.anthropic.com/en/docs/claude-code/settings)