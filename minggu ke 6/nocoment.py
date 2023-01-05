'''
print("Nama : Muhamad yazid Imani ")
print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
'''

class queue:
	# membuat class queue
	def __init__(self, n):
		# membuat method construktor dengan 2 parameter yaitu self dan n
		self.kapasitas = n
		# membuat variabel self.kapasitas yang berisi n parameter n
		self.data = []
		# membuat list kosong kemudian dimasukkan kedalam variabel self.data
		
	def visualisasiQueue(self):
		# membuat method info untuk menampilkan info dari queue tersebut
		print("\n _________________________________________________________")
		print("|                                                         |")
		print("|                        INFO QUEUE                       |")
		print("|_________________________________________________________|")
		print("|Kapasitas Antrian	:",self.kapasitas,"				  |")
		# menampilkan total kapasitas antrian dengan memanggil variabel self.kapasitas
		print("|Banyak Item Terisi	:",len(self.data),"				  |")
		# menampilkan jumlah data yang sudah terisi dengan method len
		if len(self.data)>0:
			# cek apakah jumlah data lebih dari 0
			print("|Data Paling Depan	:",self.data[0],"			  |")
			# cetak data yanhg paling depan dengan memangil index 0
			print("|Data Paling Belakang	:",self.data[-1],"			  |")
			# cetak data yang paling belakang  dengan memanggil index -1
		else:
			# jika tidak
			print("|Data Paling Depan	: N/A				  |")
			print("|Data Paling Belakang	: N/A				  |")	
		print("|_________________________________________________________|")
		print("\n Visualisasi Queue\n")
		for i in range(self.kapasitas-1,-1,-1):
			# melakukan perulangan dengan maksimal nilai kapasitas yang diawali dengan index dari terakhir sampai awal
			print("    [%2d]   "%(i+1),end="  ")
			# cetak angka urutan ke layar dengan memanggil variabel i+1
		print("")	
		for i in range(self.kapasitas):
			# melakukan perulangan sampai kapasitas terakhir
			print(" ----------",end="  ")	
		print("")
		#mencetak isi setiap posisi pada antrian
		for i in range(self.kapasitas-1,-1,-1):
			# melakukan perulangan dengan maksimal nilai kapasitas yang diawali dengan index dari belakang sampai depan
			if i<len(self.data):
				#cek apakah jumlah data lebih kecil dari variabel i
				print(" %9s "%(self.data[i]),end=">>")
				# cetak data sesuai index
			else:	
				# jika tidak
				print(" %10s"%(""),end=">>")
				# hanya mencetak 10 string kosong 
		print(" [Depan]")
		for i in range(self.kapasitas):
			# melakukan perulangan sampai kapasitas terakhir
			print(" ----------",end="  ")
		print("\n\n")			
		
	def isfull(self):
		# membuat method isfull untuk mengecek apakah data tersebut penuh atau tidak
		if len(self.data)==self.kapasitas:
			# cek apakah jumlah data sama dengan kapasitas
			return True
		else:
			return False
					
	def enqueue(self,x):
		# membuat method enqueue dengan 2 parameter yaitu self dan x untuk memasukkan data baru
		if self.isfull():
			# cek apakah isfull true or false
			print(x,"gagal di-enqueue (Queue Penuh, Overflow)")
			# jika true cetak gagal ke layar
		else:
			# jika tidak
			self.data = self.data + [x]	
			# data x yang dari parameter dimasukkan kedalam list kemudian di tambah dengan list yang ada di variabel self.data 	
			print(" *Enqueue: ",x,"di-enqueue kedalam antrian")

	
	def isempty(self):
		# membuat method isempty untuk mengecek apakah data tersebut kosong atau tidak
		if len(self.data)== 0:
			# cek apakah jumlah data sama dengan 0
			return True
		else:
			return False	
	
	def dequeue(self):
		#membuat method dequeue untuk mengeluarkan/menghapus data yang paling depan
		if self.isempty():
			# cek apakah isempty true or false
			print("Proses dequeue gagal dilakukan, Queue kosong Underflow")
			# jika true cetak gagal ke layar
			return None
			# mengembalikan nilai none
		else:
			datailang = self.data[0] 
			# index ke 0 dari variabel self.data dimasukkan kedalam variabel datailang
			self.data[:] = self.data[1:]
			# index ke 1 sampai terakhir dari variabel self.data diubah ke variabel self.data yang index ke 0 sampai terakhir
			print(" *Dequeue: ",datailang,"di-dequeue dari antrian")
			return datailang
			#mengembalikan nilai datailang
						
			
Q1 = queue(5)
# membuat objek Q1 dengan nilai argumen 5 
Q1.visualisasiQueue()
# memanggil method visualisasiQueue yg ada di objek Q1
Q1.enqueue("RUSIA")
Q1.enqueue("UKRAINA")
Q1.enqueue("KORUT")	
# menambahkan 3 data ke queue yaitu rusia,ukraina, korut			
Q1.visualisasiQueue()
# memanggil method visualisasiQueue
Q1.dequeue()
Q1.dequeue()
# memanggil 2 method dequeue untuk menghapus 2 data yang paling depan
Q1.visualisasiQueue()
# memanggil method visualisasiQueue


