print("Nama : Muhamad yazid Imani ")
print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")

class Node:
	#membuat clas Node
	def __init__ (self, dataval = None) :
	#membuat fungsi __init__ yang merupakan fungsi construktor dengan 1 parameter yaitu dataval dan bernilai None sebagai nilai default
		self.dataval = dataval
		self.nextval = None
class SlinkedList:
	#membuat class Slinkedlist
	def __init__(self):
	#Membuat fungsi __init__ yang merupakan fungsi konstruktor dengan parameter self
		self.headval = None
		self.size = 0
	
	def listprint(self):
	#membuat fungsi listprint untuk menampilkan output
		printval = self.headval
		#membuat variabel printval yang isinya headval
		while printval != None:
		#melakukan perulangan sampai printval bernilai None
			print (printval.dataval, "-->", end=" ")
			#menampilkan ke output
			printval = printval.nextval
			#memindahkan daata ke next selanjutnya
		print("NULL")
		
	
	def update(self, index, data):
	#membuat fungsi update dengan 2 parameter
		currentNode = self.headval
		#membuat variabel currentNode yang isinya headval
		newNode = Node(data)
		#membuat node baru sesuai yg diinput user
		counter = 0
		# memasukikan angka 0 kedalam variabel counter
		while counter < index-1:
			#melakukan perulangan sampai nilai input yg tadi dimasukkan user
			counter += 1
			prevNode = currentNode
			currentNode = currentNode.nextval
		prevNode.nextval = currentNode.nextval
		prevNode.nextval = newNode
		newNode.nextval = currentNode.nextval
	
list1 = SlinkedList()
#membuat object list1
n1 = Node(1)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 1 kedalam dataval
n2 = Node(2)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 2 kedalam dataval
n3 = Node(3)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 3 kedalam dataval
n4 = Node(4)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 4 kedalam dataval
list1.headval = n1
#menjadikan variabel n1 yg tadi berisi nilai 1 menjadi head dalam node
n1.nextval = n2
#menghubungkan n1 dengan n2(Node ke-2) melalui nextval
n2.nextval = n3
#menghubungkan n2 dengan n3(Node ke-3) melalui nextval
n3.nextval = n4
#menghubungkan n3 dengan n4(Node ke-4) melalui nextval

list1.listprint()
x = int(input("\nMasukkan urutan yang ingin di update : "))
y = int(input("Masukkan data baru : "))
print()
list1.update(x,y)
#manggil fungsi update
list1.listprint()
#Memanggil fungsi listprint() yang ada di dalam clas SlinkedList() untuk menampilkan semua nilai yang telah disimpan ke layar
