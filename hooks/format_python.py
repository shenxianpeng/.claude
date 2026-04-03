#!/usr/bin/env python3
"""
Post-tool-use hook: auto-format Python files after Write / Edit / MultiEdit.

Claude Code passes a JSON object to stdin describing the tool use.
This script extracts the file path and runs `ruff format` on it (falling
back to `black` if ruff is not installed).

Register in .claude/settings.json:

  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit|MultiEdit",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/format_python.py"}]
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

    # The file path lives under tool_input for Write/Edit, or in the first
    # element of tool_input.edits for MultiEdit.
    tool_input = data.get("tool_input", {})
    file_path: str = tool_input.get("file_path", "")
    if not file_path and "edits" in tool_input:
        file_path = tool_input["edits"][0].get("file_path", "")

    if not file_path or not file_path.endswith(".py"):
        return

    # Prefer ruff, fall back to black.
    for formatter in (["ruff", "format", "--quiet", file_path],
                      ["black", "--quiet", file_path]):
        try:
            result = subprocess.run(formatter, capture_output=True)
        except FileNotFoundError:
            continue
        if result.returncode == 0:
            break


if __name__ == "__main__":
    main()
