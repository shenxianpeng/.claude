#!/usr/bin/env python3
"""
Pre-tool-use hook: block accidental deletion of important paths.

Intercepts Bash tool calls and exits with a non-zero code (which causes
Claude Code to cancel the command) if the command matches a dangerous
pattern such as `rm -rf /` or `rm -rf ~`.

Register in .claude/settings.json:

  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [{"type": "command", "command": "python3 .claude/hooks/prevent_rm_rf.py"}]
      }
    ]
  }
"""

import json
import re
import sys

# Patterns that should never be executed.
BLOCKED_PATTERNS = [
    r"rm\s+-rf?\s+/(?!\w)",   # rm -rf / or rm -r /
    r"rm\s+-rf?\s+~",          # rm -rf ~ (home directory)
    r"rm\s+-rf?\s+\$HOME",     # rm -rf $HOME
    r"rm\s+-rf?\s+\.(?:/)?(?=\s|$)",  # rm -rf . or rm -rf ./ only
    r":\s*\(\)\s*\{.*\}",      # fork-bomb pattern :(){:|:&};:
]

COMPILED = [re.compile(p) for p in BLOCKED_PATTERNS]


def main() -> None:
    try:
        data = json.load(sys.stdin)
    except (json.JSONDecodeError, EOFError):
        return

    command: str = data.get("tool_input", {}).get("command", "")
    if not command:
        return

    for pattern in COMPILED:
        if pattern.search(command):
            print(
                f"[prevent_rm_rf] Blocked dangerous command: {command!r}",
                file=sys.stderr,
            )
            sys.exit(1)


if __name__ == "__main__":
    main()
