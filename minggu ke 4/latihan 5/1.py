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
		
	def hapus(self, x):
		#membuat funtion hapus sesuai nilai data yang ingin dihapus dengan 1 parameter
		target = self.headval
		#head dari node dimasukan kedalam variabel target
		while target.dataval is not x:
			#melakukan perulangan
			sebelum = target
			target = target.nextval
		if target is self.headval:
			self.headval = target.nextval
		else:
			sebelum.nextval = target.nextval
 
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
print("Sebelum Dihapus")
list1.listprint()
list1.hapus(3)
print("Sesudah Dihapus")
list1.listprint()

