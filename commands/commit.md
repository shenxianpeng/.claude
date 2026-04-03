Generate a concise, conventional commit message for the staged changes.

Follow the Conventional Commits specification (https://www.conventionalcommits.org):
- Format: `<type>(<scope>): <description>`
- Types: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`, `perf`, `ci`, `build`, `revert`
- Keep the subject line under 72 characters
- Use the imperative mood ("add" not "added")
- Do not end the subject line with a period

After the subject line, add a blank line followed by a short body if the change needs more context.

Review the current diff with `git diff --staged` and suggest the commit message.
