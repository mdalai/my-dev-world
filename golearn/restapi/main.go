package main

import (
	"fmt"
	"io/ioutil"
	"log"
	"net/http"
)

func main() {
	http.HandleFunc("/", func(rw http.ResponseWriter, r *http.Request) {
		log.Println("Learning GO")

		d, err := ioutil.ReadAll(r.Body)
		if err != nil {
			rw.WriteHeader(http.StatusBadRequest)
			rw.Write([]byte("ooops"))
			return
		}
		log.Printf("Hello %s\n", d)
		fmt.Fprintf(rw, "Hello %s\n", d)
	})

	http.HandleFunc("/goodbye", func(rw http.ResponseWriter, r *http.Request) {
		d, err := ioutil.ReadAll(r.Body)
		if err != nil {
			http.Error(rw, "OOOPS", http.StatusBadRequest)
			return
		}
		fmt.Fprintf(rw, "Goodbye %s\n", d)
	})

	http.ListenAndServe(":9090", nil)
}
