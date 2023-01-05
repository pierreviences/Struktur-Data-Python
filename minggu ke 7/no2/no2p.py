'''
print("Nama : Muhamad yazid Imani ")
print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
'''

class hash: 
	# membuat class hash
	def __init__(self,n):
		# membuat method constructor dengan 2 parameter yaitu self dan n
		self.size = n
		#memasukkan parameter n kedalam variabel self.size
		self.bnykIsi = 0
		#membuat variabel self.bnykIsi dengan nilai default yaitu 0
		self.data = []
		#membuat list kosong kemudian dimasukkan kedalam variabel self.data
		for i in range(self.size): 
			#melakukan perulangan dengan range sampai jumlah kapasitas yaitu self.size
			self.data.append(None)
			# memasukkan data kosong
		self.d = 1 
		#untuk probing 	
	
	def isfull(self):
		#membuat method isFull
		if self.bnykIsi == self.size:
			#jika banyak isi sama dengan jumlah kapasitas, maka
			return True
			# mengembalikkan nilai true
		else:
			# jika tidak, maka
			return False
			# mengembalikkan nilai false
		
	def method_hash(self,key):
		# membuat method has untuk merubah elemen awal abjad menjadi angka sesuai urutan abjad
		inisial = key[0]
		# mengambil index paling awal dari key kemudian dimasukkan kedalam variabel inisial
		idx = (ord(inisial)-ord("A")+1) % self.size	
		#inisial diubah menjadi angka kemudian dikurang ord A (nilai A diubah menjadi angka) dan ditambah 1 lalu di modulus sesuai
		#jumlah kapasitas setelah itu dimasukkan kedalam variabel idx
		return idx
		#mengembalikan nilai idx
	
	def insert(self, key):
		# membuat method insert
		print()
		print(" _________________________________________________")
		print("|                                                 |")
		print("|            Prosedur insert dilakukan            |")
		print("|_________________________________________________|")
		print(" ")
		print(" * Data				:",key)							
		if self.isfull():
			# dicek dulu apakah full?, jika iya print dibawah ini kemudian kembalikan nilai false
			print(" - Tabel Hash penuh,",key,"gagal diinsert")
			return False
		else:
			#jika tidak
			nilai_hash = self.method_hash(key)
			#panggil method hash dengan 1 argumen yaitu key yang mau ditambah, kemudian dimasukkan kedalam variabel nilai_hash
			print(" * Inisial			:",key[0])
			print(" * Nilai hash",key,"		:",nilai_hash)
			if self.data[nilai_hash] == None or self.data[nilai_hash] == "D":
				# di cek apakah data yang sesuai key itu None atau bernilai D, jika iya
				self.data[nilai_hash] = key
				# nilai yang di insert (key) kemudian dimasukkan kedalam  data sesuai index yang sudah dihash
				print(" * Posisi slot index ke -",nilai_hash,"kosong")
				print(" *",key,"menempati posisi index",nilai_hash,"pada Tabel")
			else: 
				#jika tidak, maka collision
				print(" * Posisi id",nilai_hash,"telah terisi	:",self.data[nilai_hash])
				id_alt = nilai_hash
				id_alt += self.d
				i = 1
				while(self.data[id_alt]!= None and self.data[id_alt]!= "D"):
					# melakukan perulangan sampai key data sama dengan None dan key data sama dengan D
					print(" --> probe",i,": posisi id",id_alt,"telah terisi:",self.data[id_alt])
					# mencetak ke layar probe ke berapa sesuai index dan posisi id sesuai index key data, dan mencetak data terisi sesuai index key data
					id_alt = (id_alt + self.d) % self.size
					if id_alt < 0:
						id_alt += self.size
					i += 1
				self.data[id_alt] = key
				print(" --> probe",i,": posisi id",id_alt,"kosong");
				print(" -->",key," menempati posisi index",id_alt,"pada Tabel")
			print(" _________________________________________________")
			self.bnykIsi +=1	
					
	def visualisasi(self):
		#membuat method visualisasi
		print("")
		print("     _________________")
		for i in range(self.size):
			# melakukan perulangan dengan range sampai jumlah kapasitas yaitu self.size
			if(self.data[i] == None or self.data[i]=="D"):
				#jika data sesuai index sama dengan None atau bernilai D
				print("[%2d]| %15s |"%(i,''))
				# cetak nomor dan string kosong ke layar
			else:
				# jika tidak
				print("[%2d]| %15s |"%(i,self.data[i]))
				# cetak data sesuai index
		print("    |_________________|")	
							
	def search(self, key):
		# membuat method search untuk melakukan pencarian
		print()
		print("  Prosedur search dijalankan")
		print(" ---------------------------")
		print(" * Data				:",key)
		if self.bnykIsi == 0:
			# jika bnykIsi == 0, maka
			print(" * Tabel Hash masih kosong")
			return -1
			# mengembalikan nilai -1
		else:
			#jika tidak
			nilai_hash = self.method_hash(key)
			#panggil method hash dengan 1 argumen yaitu key yang mau ditambah, kemudian dimasukkan kedalam variabel nilai_hash
			print(" * Inisial			:",key[0])
			print(" * Nilai hash",key,"		:",nilai_hash)
			idx_yg_dicek = nilai_hash
			i = 1
			while self.data[idx_yg_dicek] != key and self.data[idx_yg_dicek]!= None:
				if self.data[idx_yg_dicek]=="D":
					print(" --> Probe",i,"- posisi id	:",idx_yg_dicek,"pernah berisi data lain")
				else:	
					print(" --> Probe",i,"- posisi id	:",idx_yg_dicek,"berisi data lain")
				idx_yg_dicek = (idx_yg_dicek + self.d) % self.size
				if idx_yg_dicek < 0:
					idx_yg_dicek += self.size
				i+=1
			
			if	self.data[idx_yg_dicek] == key:
				print(" --> Probe",i,"- posisi id	:",idx_yg_dicek,"berisi data",key)
				print(" --> Ditemukan pada posisi	:",idx_yg_dicek)
				return idx_yg_dicek
			else:
				print(" --> Probe",i,"- posisi id	:",idx_yg_dicek,"KOSONG")
				print(" --> Data",key, "tidak ada pada hash",idx_yg_dicek)
				return -1	 
				
	def delete(self, key):
		# membuat method delete
		print()
		print(" _________________________________________________")
		print("|                                                 |")
		print("|            Prosedur Delete dilakukan            |")
		print("|_________________________________________________|")
		print()
		print(" * Data target:",key)
		idx_data = self.search(key)
		if idx_data== -1:
			print()
			print("  Prosedur delete dijalankan")
			print(" ---------------------------")
			print(" * Prosedur delete gagal dijalankan")
		else:
			print()
			print("  Prosedur delete dijalankan")
			print(" ---------------------------")
			print(" --> Data",key, "Berhasil di hapus")
			self.data[idx_data] ="D"
			self.bnykIsi = self.bnykIsi - 1		
	def update(self, key, databaru):
		#membuat method update 
		print()
		print(" _________________________________________________")
		print("|                                                 |")
		print("|            Prosedur Update dilakukan            |")
		print("|_________________________________________________|")
		idx_data = self.search(key)
		# memanggil method search dengan nilai argumen yaitu parameter key kemudian dimasukkan kedalma variabel idx_data
		if idx_data== -1:
			# jika idx_data samadengan -1 yang artinya data itu gak ada, maka
			print()
			print("  Prosedur update dijalankan")
			print(" ---------------------------")
			print(" * Prosedur UPDATE gagal dijalankan")
		else:
			# jika tidak, maka
			print()
			print("  Prosedur update dijalankan")
			print(" ---------------------------")
			datalama = self.data[idx_data]
			#data sesuai key dimasukkan kedalam var datalama
			self.data[idx_data] = databaru
			#data sesuai key diubah sesuai parameter databaru
			print(" --> Data",datalama, "Berhasil diupdate menjadi", databaru,"!")
			
		
		
T = hash(5) # Membuat objek T dengan nilai argumen yatu 5
T.insert("BOGOR")
T.insert("BALI")
T.insert("DEPOK")
# menambah data bogor bali depok ke hash
T.visualisasi()
# memanggil method visualisasi 
T.search("BALI")
# search data bali
T.visualisasi()	
T.delete("BALI")
# delete data bali
T.visualisasi()
T.update("DEPOK", "DENPASAR")
# update data depok menjadi denpasar
T.visualisasi()
# memanggil method visualisasi 

