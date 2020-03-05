# my git CMD

```git

# list global configs
git config --list

# clone with proxy
git clone https://github.com/mdalai/my-dev-world.git --config "http://your_proxy.com:80"
# OR
git config --global http.proxy http://your_proxy.com:80
git clone https://github.com/mdalai/my-dev-world.git

# merge prevous commits
git reset --soft #commit_id
git add . && git commit -m 'xxx'
git push origin master --force-with-lease

```