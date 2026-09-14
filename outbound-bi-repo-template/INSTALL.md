# Add to an existing repository

## GitHub Desktop or local Git
1. Extract this ZIP. It contains a folder named `outbound-bi-repo-template`.
2. Open your existing repository locally and create a branch, such as `chore/bi-repo-template`.
3. Copy the **contents** of the extracted folder into the existing repository root. Include `.github`, `.gitignore`, and `.editorconfig`. On macOS, Command+Shift+Period reveals hidden files.
4. Merge files with matching names deliberately. Keep existing README content, ignore rules, workflows, and team standards that still apply. Do not replace the existing `.git` directory; this template contains none.
5. Run the two commands in README.md. Review the changes, commit, push the branch, and open a PR against your existing default branch.

From a terminal already inside your existing checkout, before copying:

```bash
git status
git switch -c chore/bi-repo-template
```

After copying, merging conflicts, and running validation:

```bash
git diff --check
git status --short
git add README.md INSTALL.md CONTRIBUTING.md .gitignore .editorconfig .github config data docs projects python sql tableau templates tests
git diff --cached --stat
git diff --cached
git commit -m "Add Outbound Planning BI repository template"
git push -u origin chore/bi-repo-template
```

These commands assume the listed template paths were copied into the root. Inspect staged changes before committing, especially if your checkout already contained unrelated changes.

## Browser upload
Extract the ZIP first; uploading the ZIP alone does not install the repository structure. In the existing repo, choose **Add file → Upload files**, select the extracted contents, and commit to a new branch. Verify the `.github` folder and dotfiles were included. Use a local checkout if your browser omits them.

## Customize after import
- Replace proposed owners and dashboard links in `docs/dashboard-catalog.md`.
- Reconcile scenario assumptions in `docs/source-findings.md`.
- Register approved source tables and production SQL in `docs/source-catalog.md`.
- Configure reviewer requirements and required status checks in repository settings if desired; template files do not change branch protection.
- The included workflow validates Python only. Keep your existing deployment workflow and do not interpret this check as warehouse validation.

References: [GitHub file upload](https://docs.github.com/en/repositories/working-with-files/managing-files/adding-a-file-to-a-repository), [setup-python](https://github.com/actions/setup-python).
