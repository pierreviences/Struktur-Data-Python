print("Nama : Muhamad yazid Imani ")
print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
class Node: 
#membuat class Node
	def __init__(self, nim, nama, jurusan): 
		#membuat fungsi __init__ yang merupakan fungsi construktor dengan 3 parameter yaitu nim nama jurusan
		self.data = Mahasiswa(nim, nama, jurusan)
		#self.data menyimpan kelas mahasiswa yang berisi data nim nama dan jurusan
		self.next = None
		self.prev = None

class DLinkedlist: 
#membuat class DLinkedlist
	def __init__(self): 
		#Membuat fungsi __init__ yang merupakan fungsi konstruktor dengan parameter self
		self.head = None
		self.tail = None
	
	def add(self, nim, nama, jurusan): 
		#membuat method add, untuk menambah data mahasiswa
		nodebaru = Node(nim, nama, jurusan) 
		#memasukkan data nim nama jurusan ke dalam class Node kemudian dimasukkan kedalam variabel nodebaru
		if self.head == None: 
			#cek apakah head node ada atau tidak
			self.head = self.tail = nodebaru 
		else: 
			nodebaru.prev = self.tail
			nodebaru.next = None
			self.tail.next = nodebaru
			self.tail = nodebaru	
	
	def cetak(self): 
		#method cetak untuk mencetak semua node ke layar
		node = self.head 
		print("------------------------------------")
		print("    NIM ","   |   Nama", " |  Jurusan")
		print("------------------------------------")
		while node != None: 
			#mengecek apakah head ada atau tidak jika ada lakukan perulangan sampai Node habis
			print(node.data.nim,"| ",node.data.nama," |  ",node.data.jurusan) 
			node = node.next
		
class Mahasiswa: 
	#membuat class mahasiswa
	def __init__(self, nim, nama, jurusan): 
		#membuat fungsi __init__ yang merupakan fungsi construktor dengan 3 parameter yaitu nim nama jurusan
		self.nim = nim
		self.nama = nama
		self.jurusan = jurusan

		
Linked1 = DLinkedlist() 
#membuat objek linked1
Linked1.add("J0303211068","Yazid","INF")
#menambah data mahasiswa 
Linked1.add("J0303211098","Dizay","INF")
Linked1.add("J0303211342","Abdul","KMN")
print("          Data Mahasiswa \n")
Linked1.cetak() 
#mencetak node kelayar
