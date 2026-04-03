#!/usr/bin/env python3
"""
Post-tool-use hook: run linter on Python files after Write / Edit / MultiEdit
and emit any warnings as a notification without blocking Claude.

Linting errors are printed to stderr so Claude Code can surface them as a
notification, prompting Claude to fix issues in the same session.

Register in .claude/settings.json:

  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/lint_python.py"}]
      }
    ]
  }
"""

import json
import subprocess
import sys


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        return

    tool_input = data.get("tool_input", {})
    file_path: str = tool_input.get("file_path", "")
    if not file_path and "edits" in tool_input:
        file_path = tool_input["edits"][0].get("file_path", "")

    if not file_path or not file_path.endswith(".py"):
        return

    # Run ruff check (non-zero exit = lint errors found).
    try:
        result = subprocess.run(
            ["ruff", "check", "--output-format=text", file_path],
            capture_output=True,
            text=True,
        )
    except FileNotFoundError:
        return

    if result.returncode != 0 and result.stdout:
        # Print to stderr so Claude Code surfaces it as a notification.
        print(result.stdout, file=sys.stderr, end="")


if __name__ == "__main__":
    main()
