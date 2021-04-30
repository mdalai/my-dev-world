package main

import "fmt"

// define node
type Node struct {
	data int   //value of node
	next *Node //pointer of next node, OR memory address of next node
}

// define linked_list
type LinkedList struct {
	head   *Node
	length int
}

// insert node to LinkedList in the beginning
// pointer reciever
func (l *LinkedList) insertNode(n *Node) {
	currentNode := l.head
	l.head = n
	l.head.next = currentNode
	l.length++
}

// remove node from LinkedList
func (l *LinkedList) removeNode(data int) {
	// if empty LinkedList
	if l.length == 0 {
		return
	}

	toDel := l.head
	if toDel.data == data {
		l.head = toDel.next
		l.length--
		return
	}

	var beforeDel *Node
	// unfortantly go doesn't have WHILE loop
	for toDel.next != nil {
		beforeDel = toDel
		toDel = toDel.next
		if toDel.data == data {
			beforeDel.next = toDel.next
			l.length--
			return
		}
	}

	// for toDel.next.data != data {
	// 	toDel = toDel.next
	// }
	// toDel.next = toDel.next.next
	// l.length--
}

// print data
// value reciever
func (l LinkedList) printLinkedList() {
	toPrint := l.head
	for l.length != 0 {
		fmt.Printf("%d ", toPrint.data)
		toPrint = toPrint.next
		l.length--
	}
	fmt.Println()
}

func main() {
	myLinkedList := LinkedList{}
	node1 := &Node{data: 2}
	node2 := &Node{data: 3}
	node3 := &Node{data: 32}
	node4 := &Node{data: 73}
	node5 := &Node{data: 23}
	node6 := &Node{data: 13}
	myLinkedList.insertNode(node1)
	myLinkedList.insertNode(node2)
	myLinkedList.insertNode(node3)
	myLinkedList.insertNode(node4)
	myLinkedList.insertNode(node5)
	myLinkedList.insertNode(node6)
	fmt.Println(myLinkedList)
	myLinkedList.printLinkedList()
	myLinkedList.removeNode(3)
	myLinkedList.removeNode(100)
	myLinkedList.removeNode(73)
	myLinkedList.printLinkedList()
}
