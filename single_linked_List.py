class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    def insert(self, newNode):
        if self.head == None:
            self.head = newNode
        else:
            lastNode = self.head
            while True:
                if lastNode.next is None:
                    break
                lastNode = lastNode.next
            lastNode.next = newNode

    def printlist(self):
        currrentNode = self.head
        while True:
            if currentNode is None:
                break
            print(currentNode.data)
            currentNode = currentNode.next


firstNode = Node("John")
linked_list = LinkedList()
linked_list.insert(firstNode)
secondNode = Node("Ben")
linked_list.insert(secondNode)
thirdNode = Node("Mathew")
linked_list.insert(thirdNode)
linked_list.printlist()
