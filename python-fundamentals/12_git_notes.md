# Basic Git Notes

Git tracks changes in your project.

Do not run commands unless you understand what they do.

## `git clone`

Copies a remote repository to your computer.

```bash
git clone <repository-url>
```

Use this when you want to download a project for the first time.

## `git status`

Shows what changed in your working folder.

```bash
git status
```

Use this often. It is safe and helpful.

## `git add`

Moves changes into the staging area.

```bash
git add file_name.py
```

The staging area means: "I want these changes in my next commit."

To stage all current changes:

```bash
git add .
```

## `git commit`

Saves staged changes into Git history.

```bash
git commit -m "Add my feature"
```

A commit message should explain what changed.

## `git push`

Uploads your local commits to GitHub or another remote.

```bash
git push
```

Use this after committing when you want your work online.

## `git pull`

Downloads new changes from the remote repository and applies them locally.

```bash
git pull
```

Use this before starting work so your local project is up to date.

## `git branch`

Shows branches in your repository.

```bash
git branch
```

A branch is a separate line of work.

## `git switch`

Switches from one branch to another.

```bash
git switch main
```

Create and switch to a new branch:

```bash
git switch -c feature/my-feature
```

## Feature Branches

A feature branch lets you work on one task separately.

This keeps the main branch cleaner.

Example branch names:

```text
feature/login-api
feature/task-validation
fix/error-message
```

## Realistic Internship Workflow

```bash
git status
git switch -c feature/my-feature
git add .
git commit -m "Add my feature"
git push -u origin feature/my-feature
```

Explanation:

`git status` checks your current changes.

`git switch -c feature/my-feature` creates a new branch and switches to it.

`git add .` stages all changed files.

`git commit -m "Add my feature"` saves the staged changes in Git history.

`git push -u origin feature/my-feature` uploads your branch to the remote repository and links your local branch to it.

## Practice Workflow

1. Create or edit one practice file.
2. Run `git status`.
3. Stage only the file you changed.
4. Commit with a clear message.
5. Push your branch.

Practice commands:

```bash
git status
git switch -c feature/python-practice
git add python-fundamentals/01_lists.py
git commit -m "Practice Python lists"
git push -u origin feature/python-practice
```
