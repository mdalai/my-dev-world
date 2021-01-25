# my git CMD

```git

# list global configs
git config --list

# clone with proxy
git clone https://github.com/mdalai/my-dev-world.git --config "http://your_proxy.com:80"
# OR
git config --global http.proxy http://your_proxy.com:80
git clone https://github.com/mdalai/my-dev-world.git

# merge previous commits
git reset --soft #commit_id
git add . && git commit -m 'xxx'
git push origin master --force-with-lease

```

```git
git checkout -t origin/my-awesome-feature    # checkout remote branch
git push <remote> -d <branch>       # delete remote branch
git remote set-url <remote> <newurl>  # change remote URL
git stash push -- src/index.js README.md  # Stach specific files
git stash show -p stash@{0}  # show content of most recent stash
git diff <commit-a> <commit-b> -- <path(s)>  # compare files between two commits
git checkout -- README.md  # reset a file to most recent commit

```

```git
git reset   # unstash after "git add ."
git push origin local-branch:remote-branch  # push to remote branch
git branch -r   # list remote branches

# Remote local dev machine sync
git init --bare bare_repos/my_repo.git   # remote machine: create a bare repo
git clone bare_repos/my_repo.git repos/my_repo  # remote machine: clone bare repo as a workspace; commit and push in this WS.
git clone dev@remote-machine:~/bare_repos/my_repo.git local_repos/my_repo # local machine: clone bare repo; pull,commit, push in this location.

```



