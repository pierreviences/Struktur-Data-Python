print("Nama : Muhamad yazid Imani ")
print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
print("Menambah data ditengah Node")
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
	def sisipken(self, x, n):
		nodeBaru = Node(x)
		self.size += 1
		nodeLama = self.headval
		L = 0
		if nodeLama is None:
			self.headval = nodeBaru
		else:
			while L < n:
				sebelum = nodeLama
				nodeLama = nodeLama.nextval
				L += 1
			sebelum.nextval = nodeBaru
			nodeBaru.nextval = nodeLama	
list1 = SlinkedList()
n1 = Node(1)
n2 = Node(3)
n3 = Node(4)
n4 = Node(5)
list1.headval = n1
n1.nextval = n2
n2.nextval = n3
n3.nextval = n4
list1.sisipken(2,1)

list1.listprint()
