# my git CMD

```git

# GOPATH:~/go/      by default
# GOBIN: ~/go/bin/  by default

# Set go env in bash
export GOPATH=~/go/src
export GOBIN=~/go/bin/

# Set go env in csh
setenv GOPATH ~/go/src
setenv GOBIN  ~/go/bin/

cd ~/dev/learngo
go install             # gen binary into GOBIN.
go build               # gen binary in current folder
go run main.go         # gen binary in a temp location, and run it
go run --work          # gen binary in a temp, and run it. Shows location as well.

### go packages ###
# create a module first. 
go mod init <module_name>   # module_name is root folder name

# create pkg_name folder and pkg_name.go
mkdir <pkg_name>
touch <pkg_name>/<pkg_name>.go

# import the pkg by
import <module_name>/<pkg_name>


### build static files along with binarys ###
# following installs package and its dependencies
# into  GOPATH/pkg/mod/github.com/
go get -u github.com/gobuffalo/packr/v2/...   # packr

$GOBIN/packr2     # this gens 2 files: main-packr.go  packrd
go install

$GOBIN/packr2     # this cleans up generated files

# remove the static file and run binary should be OK now


```