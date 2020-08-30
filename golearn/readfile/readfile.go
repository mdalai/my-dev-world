package main

import (
	"flag" //// for func: read_cmd_arg
	"fmt"

	//"io/ioutil"

	"github.com/gobuffalo/packr/v2" // for func: build_text_file_along_with_binary
)

const FILEPATH = "/home/dalai/dev/my-dev-world/golearn/readfile/data.txt"

func read_abs_path(p_filepath string) string {
	fpath := p_filepath
	return fpath
}

func read_cmd_arg() string {
	fptr := flag.String("fpath", "data.txt", "file path to read from")
	flag.Parse()
	fmt.Println("Val of fpath: ", *fptr)
	return *fptr
}

// shall use 3rd package:  packr
// go get -u github.com/gobuffalo/packr/v2/...
func build_text_file_along_with_binary() {
	//box := packr.New("fileBox", "../readfile")
	//data, err := box.FindString("data.txt")
}

func main() {
	// read file into a byte slice, data
	//filepath := read_abs_path(FILEPATH)
	//filepath := read_cmd_arg() // readfile -fpath=`pwd`/data.txt
	//data, err := ioutil.ReadFile(filepath)

	box := packr.New("fileBox", "../readfile")
	data, err := box.FindString("data.txt")

	if err != nil {
		fmt.Println("File reading error", err)
		return
	}
	fmt.Println("Content===>: \n", string(data))
}
