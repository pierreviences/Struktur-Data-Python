class Node(object):
	def __init__(self, data):
		self.data = data
        self.nextNode = None
class SinglyLinkedList(object):
def __init__(self):
        self.head = None
        self.size = 0
def insertAtEnd(self, data):
        newNode = Node(data)
        self.size += 1
if self.head is None:
            self.head = newNode
        else:
            currentNode = self.head
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
        
            currentNode.nextNode = newNode
def insertAtStart(self, data):
        newNode = Node(data)
        self.size += 1
if self.head is None:
            self.head = newNode
        else:
            newNode.nextNode = self.head
            self.head = newNode
        
  def removeAtStart(self):
        currentNode = self.head
if currentNode is not None:
            self.size -= 1
            self.head = currentNode.nextNode
        else:
            print("Linked list is empty")
def removeAtEnd(self):
        currentNode = self.head
if currentNode is None:
            print("linked List is empty")
        else:
            while currentNode.nextNode is not None:
                prevNode = currentNode
                currentNode = currentNode.nextNode
        
            prevNode.nextNode = None
            self.size -= 1
def insertAtIndex(self, index, data):
        newNode = Node(data)
        self.size += 1
currentNode = self.head
        counter = 0
if currentNode is None:
            self.head = newNode
        else:
            while counter < index:
                prevNode = currentNode
                currentNode = currentNode.nextNode
                counter += 1
            
            prevNode.nextNode = newNode
            newNode.nextNode = currentNode
def removeAtIndex(self, index):
        currentNode = self.head
        counter = 0
while counter < index:
            counter += 1
            prevNode = currentNode
            currentNode = currentNode.nextNode
prevNode.nextNode = currentNode.nextNode 
        self.size -= 1
def removeData(self, data):
        currentNode = self.head
while currentNode.data is not data:
            prevNode = currentNode
            currentNode = currentNode.nextNode
if currentNode is self.head:
            self.head = currentNode.nextNode
        else:
            prevNode.nextNode = currentNode.nextNode
        self.size -= 1
def traverse(self):
        currentNode = self.head
if currentNode is None:
            print("Linkedlist is empty")
        else:
            print(currentNode.data)
            while currentNode.nextNode is not None:
                currentNode = currentNode.nextNode
                print(currentNode.data)
singly = SinglyLinkedList()
