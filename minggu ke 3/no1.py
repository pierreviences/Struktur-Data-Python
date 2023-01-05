class Node:
	def __init__ (self, dataval = None) :
		self.dataval = dataval
		self.nextval = None

class SlinkedList:
	def __init__(self):
		self.headval = None
		self.size = 0
	def listprint(self):
		printval = self.headval
		while printval != None:
			print (printval.dataval, "-->", end=" ")
			printval = printval.nextval
		print("NULL")
	def insertdepan(self, newdata):
		newNode = Node(newdata)
		newNode.nextval = self.headval
		self.headval = newNode
	def inserttengah(self,middle_node,newdata):
		if middle_node is None:
			print("Nilai tidak ada isinya")
			return
		newNode = Node(newdata)
		newNode.nextval = middle_node.nextval
		middle_node.nextval = newNode
		
	def insertbelakang(self, newData):
		newnode = Node(newData)
		if self.headval is None:
			self.headval = newnode
		else:
			tail = self.headval
			while tail.nextval != None:
				tail = tail.nextval
			tail.nextval = newnode
	def hapusdepan(self):
		target = self.headval
		if self.headval!=None:
			self.headval = self.headval.nextval
			target = None
			
	def hapusbelakang(self):
		target = self.headval
		if (self.headval is None):
			print("Data masih kosong")
		else:
			while target.nextval.nextval != None:
				target = target.nextval
			target.nextval = None
	def nambahtengah(self, index, data):
		newNode = Node(data)
		self.size += 1
		currentNode = self.headval
		counter = 0
		if currentNode is None:
			self.headval = newNode
		else:
			while counter < index:
				prevNode = currentNode
				currentNode = currentNode.nextval
				counter += 1
			prevNode.nextval = newNode
			newNode.nextval = currentNode

		
list1 = SlinkedList()
n1 = Node(1)
n2 = Node(3)
n3 = Node(4)

list1.headval = n1
n1.nextval = n2
n2.nextval = n3

list1.insertdepan(0)
list1.inserttengah(list1.headval.nextval,"2")
list1.insertbelakang(5)
list1.insertbelakang(6)
list1.nambahtengah(7,7)
list1.insertbelakang(8)
list1.insertbelakang(9)
list1.hapusdepan()
list1.hapusbelakang()

list1.listprint()
