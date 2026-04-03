Generate a clear and informative pull request description for the current branch.

Steps:
1. Run `git log main..HEAD --oneline` (or `git log origin/main..HEAD --oneline`) to list the commits in this branch
2. Run `git diff main...HEAD --stat` to see which files changed
3. Review key diffs with `git diff main...HEAD` to understand the substance of the changes

Then write a PR description containing:

## Summary
A concise 2–3 sentence explanation of **what** changed and **why**.

## Changes
A bullet list of the notable changes grouped by area (e.g. feature, fix, refactor, tests, docs).

## Testing
Describe how the changes were tested or how a reviewer can verify them.

## Notes (optional)
Any follow-up work, known limitations, or context a reviewer should be aware of.

Keep the tone professional and the length appropriate — a focused PR needs only a short description; a large one warrants more detail.
