#Nama : Daffala Viro HIdayat
#NIM : J0303211148

class queue:
	def __init__(self, n): #inisialisasi di awal instansialasi objek queue
		self.kapasitas = n #Menentukan kapasitas queue
		self.data = [] #Menyimpan data queue dalam sebuah list
		
	def visual_queue(self): #Method untuk visualisasi Queue (Mencetak dari kanan)
		for i in range(self.kapasitas,0,-1): 
			print("   [%2d]   "%(i),end="  ") 
		print("")
		
		#Untuk menampilkan batas berupa garis ------- di atas pada setiap urutan queue
		for i in range(self.kapasitas): 
			print("----------",end="  ")	
		print("")
		
		#Mencetak isi setiap posisi pada antrian
		jml_pos_terisi = len(self.data) #Jumlah posisi yang terisi berdasarkan jumlah data yang berada di queue 
		for i in range(self.kapasitas,0,-1):
			if i>jml_pos_terisi: #Jika i lebih dari jumlah Jumlah posisi yang terisi, maka
				print("%10s  "%(""),end="") #maka akan mencetak string kosong 
			else:	#Selain itu,
				print("%9s  "%(self.data[i-1]),end="") #Akan mencetak isi data dan ditempatkan paling kanan pada queue
		print(">> [DEPAN]",end="") #Menunjukkan bahwa elemen tersebut merupakan paling depan
		print("")	
		
		#Untuk menampilkan batas berupa garis ------- di bawah pada setiap urutan queue
		for i in range(self.kapasitas):
			print("----------",end="  ")
		print("")	
		
Q = queue(5) #Instansiasi objek queue dengan kapasitasnya berjumlah 5
Q.visual_queue() #Mencetak visualisasi 
