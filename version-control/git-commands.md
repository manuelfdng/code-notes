IMPORTANT: `git pull origin main` before pushing

Setting initial configuration
```bash
git config --global user.name <username>
git config --global user.email <email>
```

Remove files from staging area
```bash
git reset
```

See commits
```bash
git log
```

Cloning a remote repo
```bash
git clone <url> <target-dir>
```

Viewing information about the repote repository
```bash
git remote -v
git branch -a
```

Creating a branch and then entering ("checking out") the branch
```bash
git branch <branch-name>
git checkout <branch-name>
```

See all branches and which branch you are on
```bash
git branch
```

Merging a branch to main
```bash
git checkout main
git pull origin main
git branch --merged
git merged <branch-to-merge>
git push origin main
```

Deleting a branch first locally and then in the remote repo
```bash
git branch --merged
git branch -d <branch-to-delete>
git push origin --delete <branch-to-delete>
```

```bash
```

```bash
```

```bash
```

```bash
```

The differences among `git add -A` `git add -u` `git add .` `git add *`