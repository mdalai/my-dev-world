package main

import (
	"bufio"
	"flag"
	"fmt"
	"log"
	"os"
)

func readFileInChunks(p_buffer int) {
	fptr := flag.String("fpath", "data.txt", "filepath to read from")
	flag.Parse()
	f, err := os.Open(*fptr)
	if err != nil {
		log.Fatal(err)
	}

	defer func() {
		if err = f.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	r := bufio.NewReader(f)
	b := make([]byte, p_buffer) // only chunks of 3 bytes a time
	for {
		n, err := r.Read(b)
		if err != nil {
			fmt.Println("Error reading file: ", err)
			break
		}
		fmt.Println(string(b[0:n]))
	}

}

func readFileLineByLine() {
	fptr := flag.String("fpath", "data.txt", "filepath to read from")
	flag.Parse()
	f, err := os.Open(*fptr)
	if err != nil {
		log.Fatal(err)
	}

	defer func() {
		if err = f.Close(); err != nil {
			log.Fatal(err)
		}
	}()

	s := bufio.NewScanner(f)
	for s.Scan() {
		fmt.Println(s.Text())
	}
	err = s.Err()
	if err != nil {
		log.Fatal(err)
	}

}

func main() {

	readFileInChunks(3)
	//readFileLineByLine()

}
