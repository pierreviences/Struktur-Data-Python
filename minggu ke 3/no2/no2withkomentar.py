print("Nama : Muhamad yazid Imani ")
print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
print("Menambah data ditengah Node")
print("Disini saya menambahkan node dengan angka 2 diantara angka 1 dan 3")



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
		
	
	def sisipken(self, x, n):
		#membuat fungsi sisipken dengan 2 parameter yaitu n sebagai titik sisip dan x sebagai node baru yg akan diberikan 
		#yang berfungsi untuk menyisipkan data ditengah
		nodeBaru = Node(x)
		#membuat nodebaru dengan memanggil class Node yang berisi variabel x
		self.size += 1
		nodeLama = self.headval
		#membaut variabel nodelama yang berisi headval
		L = 0
		if nodeLama is None:
		#jika head dari si node tidak ada
			self.headval = nodeBaru
			#maka head akan diisikan oleh nodebaru
		else:
		#jika tidak
			while L < n:
			#lakukan perulangan sampai index yang diberikan oleh user
				sebelum = nodeLama
				nodeLama = nodeLama.nextval
				L += 1
			sebelum.nextval = nodeBaru
			nodeBaru.nextval = nodeLama	

list1 = SlinkedList()
#membuat object list1
n1 = Node(1)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 1 kedalam dataval
n2 = Node(3)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 3 kedalam dataval
n3 = Node(4)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 4 kedalam dataval
n4 = Node(5)
#membuat sebuah variabel n1 yang berisi class Node yang bertujuan untuk menyimpan nilai 5 kedalam dataval
list1.headval = n1
#menjadikan variabel n1 yg tadi berisi nilai 1 menjadi head dalam node
n1.nextval = n2
#menghubungkan n1 dengan n2(Node ke-2) melalui nextval
n2.nextval = n3
#menghubungkan n2 dengan n3(Node ke-3) melalui nextval
n3.nextval = n4
#menghubungkan n3 dengan n4(Node ke-4) melalui nextval

list1.sisipken(2,1)
#Memanggil fungsi sisipken() yang ada di dalam clas SlinkedList() untuk menyisipkan nilai di tengah sesuai titik sisip yg diberikan
#disini saya menambahkan angka 2 di tengah2 angka 1 dan 3
list1.listprint()
#Memanggil fungsi listprint() yang ada di dalam clas SlinkedList() untuk menampilkan semua nilai yang telah disimpan ke layar
