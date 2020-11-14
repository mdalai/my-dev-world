package main

import (
	"fmt"
)

type student struct {
	fname string
	lname string
	grade string
	country string 
}

func filter(s []student, f func(student) bool) []student {
	var r []student
	for _, v := range s {
		if f(v) == true {
			r = append(r, v)
		}
	}
	return r
}

func main() {
	s1 := student{
		fname: "Elon",
		lname: "Musk",
		grade: "A",
		country: "USA",
	}

	s2 := student {
		fname: "John",
		lname: "Simon",
		grade: "B",
		country: "India",
	}

	s := []student{s1, s2}
	f := filter(s, func(s student) bool {
		if s.grade == "B" {
			return true
		}
		return false
	})
	fmt.Println("Grade B students: ", f)

	c := filter(s, func(s student) bool {
		if s.country == "USA" {
			return true
		}
		return false
	})
	fmt.Println("USA students: ", c)
}