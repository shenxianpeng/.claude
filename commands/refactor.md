Refactor the following code to improve its quality without changing its behaviour: $ARGUMENTS

Focus areas (apply what is relevant):
1. **Readability** – clearer variable/function names, simpler expressions, reduced nesting
2. **Duplication** – extract repeated logic into shared helpers or abstractions
3. **Single Responsibility** – split functions or classes that do too many things
4. **Error handling** – make error paths explicit and consistent
5. **Performance** – remove unnecessary work (only if there is a clear win)
6. **Style** – align with the project conventions in CLAUDE.md

Rules:
- Do **not** change observable behaviour or public interfaces
- Keep the diff as small as possible — prefer many small improvements over a full rewrite
- Add a brief comment explaining any non-obvious refactoring decision
- After refactoring, confirm existing tests still pass (run them if a test suite exists)
