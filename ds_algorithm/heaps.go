package main

import (
	"fmt"
	"strings"
)

// MaxHeap struct has a slice that holds the array
type MaxHeap struct {
	array []int
}

// Insert an element to the heap
func (h *MaxHeap) Insert(key int) {
	// add it into the end
	h.array = append(h.array, key)
	// restructure array
	h.maxHeapifyUp(len(h.array) - 1)
}

// Extract the largest key, and removes it from the heap
func (h *MaxHeap) Extract() int {
	// remove the 1st item in the array
	extracted := h.array[0]

	// handle empty array
	if len(h.array) == 0 {
		fmt.Println(("Empty array cannot extract"))
		return -1
	}

	// get the last index
	lastIndex := len(h.array) - 1
	// move last item to first
	h.array[0] = h.array[lastIndex]
	// get rid of last item from array
	h.array = h.array[:lastIndex]

	h.maxHeapifyDown(0)

	return extracted
}

// maxHeapifyUp heapify from bottom top
func (h *MaxHeap) maxHeapifyUp(index int) {
	for h.array[parent(index)] < h.array[index] {
		h.swap(parent(index), index)
		index = parent(index)
	}
}

// maxHeapfyDown heapify top to bottom
func (h *MaxHeap) maxHeapifyDown(index int) {

	lastIndex := len(h.array) - 1
	leftIndex, rightIndex := left(index), right(index)
	childToCompare := 0

	// loop while index has at least one child
	for leftIndex <= lastIndex {
		if leftIndex == lastIndex { //when left child is the only child
			childToCompare = leftIndex
		} else if h.array[leftIndex] > h.array[rightIndex] { //when left child is larger
			childToCompare = leftIndex
		} else { //when right child is larger
			childToCompare = rightIndex
		}

		// compare array value of current index to larger child and swap if smaller
		if h.array[index] < h.array[childToCompare] {
			h.swap(index, childToCompare)
			index = childToCompare
			leftIndex, rightIndex = left(index), right(index)
		} else {
			return
		}
	}
}

// get parent index
func parent(i int) int {
	return (i - 1) / 2
}

// get the left child index
func left(i int) int {
	return 2*i + 1
}

// get the right child index
func right(i int) int {
	return 2*i + 2
}

// swap keys in array
func (h *MaxHeap) swap(i1, i2 int) {
	h.array[i1], h.array[i2] = h.array[i2], h.array[i1]
}

func main() {
	m := &MaxHeap{}
	fmt.Println(m)

	buildHeap := []int{10, 20, 30, 40, 5, 6, 8, 9, 13, 16, 19}
	for _, v := range buildHeap {
		m.Insert(v)
		fmt.Println(m)
	}

	fmt.Println(strings.Repeat("-", 30))

	for i := 0; i < 5; i++ {
		m.Extract()
		fmt.Println(m)
	}

}
