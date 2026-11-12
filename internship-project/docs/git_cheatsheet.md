# Git and GitHub – Step by Step

## One-time setup
```bash
git config --global user.name "Your Name"
git config --global user.email "your-email@example.com"
git config --global init.defaultBranch main
```

## Publish this project
1. On github.com click **New repository**. Name it `internship-project`.
   Do NOT add a README there (you already have one).
2. In your project folder:
```bash
git init
git add .
git commit -m "Initial commit: hello world project with tests and docs"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/internship-project.git
git push -u origin main
```

## Daily commands
| Command | What it does |
| --- | --- |
| `git status` | Shows what changed |
| `git add .` | Stages all changes |
| `git commit -m "msg"` | Saves a snapshot |
| `git log --oneline` | Shows history |
| `git branch` | Lists branches |
| `git push` | Uploads commits |
| `git pull` | Downloads new commits |
| `git clone URL` | Copies a repo |

## Good commit messages
- Good: `Add input check to build_greeting`
- Bad: `changes`, `final`, `asdf`

## Common problems
- **Push rejected / asks for password:** GitHub no longer accepts account passwords. Use a Personal Access Token or GitHub CLI (`gh auth login`).
- **"fatal: not a git repository":** you are in the wrong folder. Run `git init` or `cd` into the project.
- **"remote origin already exists":** run `git remote set-url origin NEW_URL`.
