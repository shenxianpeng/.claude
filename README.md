# .claude

A template repository demonstrating the best-practice folder structure for
[Claude Code](https://claude.ai/code) configuration.

## Folder Structure

```
your-project/
├── CLAUDE.md                      # Project instructions read by Claude at session start
├── CLAUDE.local.md                # Personal overrides (gitignored)
└── .claude/
    ├── settings.json              # Shared project settings committed to version control
    ├── settings.local.json        # Personal settings overrides (gitignored)
    ├── commands/                  # Custom slash commands available as /project:<name>
    │   ├── commit.md              # /project:commit       — generate a conventional commit message
    │   ├── create.md              # /project:create       — scaffold a new file or component
    │   ├── document.md            # /project:document     — add or update docstrings / docs
    │   ├── explain.md             # /project:explain      — explain what a piece of code does
    │   ├── fix.md                 # /project:fix          — diagnose and fix an issue
    │   ├── pr-description.md      # /project:pr-description — generate a PR description
    │   ├── refactor.md            # /project:refactor     — refactor code without changing behaviour
    │   ├── review.md              # /project:review       — run a structured code review
    │   └── test.md                # /project:test         — generate tests for a file or function
    ├── hooks/                     # Shell/Python scripts triggered by Claude Code lifecycle events
    │   ├── format_python.py       # PostToolUse: auto-format edited Python files (ruff / black)
    │   ├── lint_python.py         # PostToolUse: run ruff on edited Python files and surface warnings
    │   └── prevent_rm_rf.py       # PreToolUse:  block dangerous `rm -rf` commands
    └── .gitignore                 # Excludes local-only files from version control
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
and shell commands Claude is permitted to use, and registers lifecycle hooks:

```jsonc
{
  "permissions": {
    "allow": [
      "Bash(python *)",
      "Bash(pytest *)",
      "Bash(ruff check *)",
      "Bash(git diff *)"
    ],
    "deny": [
      "Bash(rm -rf *)"
    ]
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/prevent_rm_rf.py"}]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [
          {"type": "command", "command": "python3 .claude/hooks/format_python.py"},
          {"type": "command", "command": "python3 .claude/hooks/lint_python.py"}
        ]
      }
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
| `commit.md`          | `/project:commit`           | Generate a conventional commit message for staged changes |
| `create.md`          | `/project:create <what>`    | Scaffold a new file, class, module, or component |
| `document.md`        | `/project:document <target>`| Add or update docstrings and inline comments |
| `explain.md`         | `/project:explain <target>` | Explain what a piece of code does |
| `fix.md`             | `/project:fix <issue>`      | Diagnose and apply a fix for a bug or error |
| `pr-description.md`  | `/project:pr-description`   | Generate a structured pull request description |
| `refactor.md`        | `/project:refactor <target>`| Improve code quality without changing behaviour |
| `review.md`          | `/project:review <target>`  | Run a structured code review |
| `test.md`            | `/project:test <target>`    | Generate tests for a file or function |

Commands may include `$ARGUMENTS` as a placeholder for user-supplied input.

### `.claude/hooks/`

Python scripts that Claude Code executes automatically at specific lifecycle
events.  All hooks receive a JSON payload on stdin describing the event.

| Script | Event | Trigger | What it does |
|--------|-------|---------|--------------|
| `format_python.py` | `PostToolUse` | `Write|Edit|MultiEdit` | Runs `ruff format` (or `black`) on the modified `.py` file |
| `lint_python.py`   | `PostToolUse` | `Write|Edit|MultiEdit` | Runs `ruff check` and surfaces warnings to Claude via stderr |
| `prevent_rm_rf.py` | `PreToolUse`  | `Bash` | Blocks commands matching dangerous `rm -rf` patterns |

Hooks are configured in `settings.json` under the `"hooks"` key.
See the [hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
for the full event list and payload schema.

## Usage

1. **Copy this repository** into the root of your project as `.claude/`:
   ```bash
   cp -r /path/to/.claude-template/.claude  your-project/.claude
   ```
2. **Copy `CLAUDE.md`** to the root of your project and fill in the blanks.
3. **Adjust `settings.json`** to match your project's allowed/denied commands.
4. **Add or remove commands** in `.claude/commands/` to match your workflow.
5. **Enable or disable hooks** in `settings.json` and `.claude/hooks/` as needed.
6. **Add `.claude/settings.local.json` and `CLAUDE.local.md`** to your
   project's `.gitignore` (already handled inside `.claude/.gitignore`).

## Resources

- [Claude Code documentation](https://docs.anthropic.com/en/docs/claude-code)
- [CLAUDE.md guide](https://docs.anthropic.com/en/docs/claude-code/memory)
- [Custom slash commands](https://docs.anthropic.com/en/docs/claude-code/slash-commands)
- [Hooks reference](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Settings reference](https://docs.anthropic.com/en/docs/claude-code/settings)