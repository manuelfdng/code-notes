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

# Fixing mistakes

Before committing and pushing, reset a file
```bash
git checkout <filename>
git status
```

Modifying the last commit message
```bash
git commit --amend -m <revised-message>
```

Adding a file to the last commit. Just skip the git commit message modification.
```bash
git commit --amend 
```

Made commit to the wrong branch so you need to move the commits to another branch and return the wrong branch to initial state
```bash
git log #get hash
git checkout <target-branch>
git cherry-pick <hash>
```

Removing a commit
```bash
git reset --soft <hash> #undo add but keep changes in files
git reset <hash> #does not undo add
git reset --hard <hash> #undo add and removes changes in files. DANGEROUS.
```

Deleting all untracked files and directories
```bash
git clean -df
```

Undoing a hard reset (only available for ~30 days depending on git garbage configuration)
```bash
git reflog #get hash
git checkout <hash> #detached head state
git branch <new-branch-name> #so save to a branch
```

Revert is a reset when other users have already pulled the commit. i.e. you don't want to overwrite history
```bash
git revert <hash>
```

```bash
```

```bash
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