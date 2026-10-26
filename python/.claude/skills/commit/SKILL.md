---
name: commit
description: Commit the currently staged git changes using this repo's conventional-commit style (type(scope): summary). Use when the user asks to commit, make a commit, or commit staged changes.
---

# Commit staged changes

1. Inspect what is staged:
   - `git status --short`
   - `git diff --cached`
   If nothing is staged, stop and tell the user. Never run `git add` unless the user asks for it.

2. Write the message in the repo's style:
   - Format: `type(scope): summary`. Use lowercase and the imperative mood, with no trailing period.
   - Types: `feat`, `fix`, `refactor`, `chore`, `docs`.
   - Scope: the project folder, e.g. `python` for this folder, `react-fetch` or `redux-demo` for others.
   - Keep the subject line to 72 characters or fewer. Add a body only when the "why" isn't obvious from the diff.
   - Examples from history:
     - `feat(python): add json file reader`
     - `feat(python): use typed data in file_reader and add readme`

3. Commit only what is staged, passing the message through a HEREDOC and ending it with the attribution line:
   ```
   git commit -m "$(cat <<'MSG'
   type(scope): summary

   Co-Authored-By: Claude <noreply@anthropic.com>
   MSG
   )"
   ```

4. Rules:
   - Do not amend, rebase, or push unless asked.
   - Confirm with the user before committing directly on `master`.
   - If a pre-commit hook fails, fix the issue and make a new commit; don't use `--no-verify`.

5. Afterwards, show the result with `git log -1 --stat`.
