class hash:
	def __init__(self,n):
		self.size = n
		self.bnykIsi = 0
		self.data = []
		for i in range(self.size):
			self.data.append(None)
		self.d = 1 #untuk probing	
	
	def isfull(self):
		if self.bnykIsi == self.size:
			return True
		else:
			return False
		
	def method_hash(self,key):
		inisial = key[0]
		idx = (ord(inisial)-ord("A")+1) % self.size	
		return idx
	
	def insert(self, key):
		print("\n>>Prosedur insert dilakukan")
		print("Data:",key)							
		if self.isfull():
			print("- Tabel Hash penuh,",key,"gagal diinsert")
			return False
		else:
			nilai_hash = self.method_hash(key)
			print("- Inisial:",key[0])
			print("- Nilai hash",key,":",nilai_hash)
			if self.data[nilai_hash] == None or self.data[nilai_hash] == "D":
				self.data[nilai_hash] = key
				print("- Posisi slot id",nilai_hash,"kosong")
				print("-",key,"menempati posisi index",nilai_hash,"pada Tabel")
			else: #collision
				print("- Posisi id",nilai_hash,"telah terisi:",self.data[nilai_hash])
				id_alt = nilai_hash
				id_alt += self.d
				i = 1
				while(self.data[id_alt]!= None and self.data[id_alt]!= "D"):
					print("--> probe",i,": posisi id",id_alt,"telah terisi:",self.data[id_alt])
					id_alt = (id_alt + self.d) % self.size
					if id_alt < 0:
						id_alt += self.size
					i += 1
				self.data[id_alt] = key
				print("--> probe",i,": posisi id",id_alt,"kosong");
				print(key,"menempati posisi index",id_alt,"pada Tabel")
			
			self.bnykIsi +=1 #ada yang masuk 1		
					
	def visualisasi(self):
		print("")
		for i in range(self.size):
			if(self.data[i] == None or self.data[i]=="D"):
				print("[%2d]| %15s |"%(i,''))
			else:
				print("[%2d]| %15s |"%(i,self.data[i]))
		print("     -----------------")	
							
	def search(self, key):
		print("\n>>Prosedur search dilakukan")
		print("Data:",key)
		if self.bnykIsi == 0:
			print("Tabel Hash masih kosong")
			return -1
		else:
			nilai_hash = self.method_hash(key)
			print("- Inisial:",key[0])
			print("- Nilai hash",key,":",nilai_hash)
			
			idx_yg_dicek = nilai_hash
			i = 1
			while self.data[idx_yg_dicek] != key and self.data[idx_yg_dicek]!= None:
				if self.data[idx_yg_dicek]=="D":
					print("-- Probe",i,"- posisi id:",idx_yg_dicek,"pernah berisi data lain")
				else:	
					print("-- Probe",i,"- posisi id:",idx_yg_dicek,"berisi data lain")
				idx_yg_dicek = (idx_yg_dicek + self.d) % self.size
				if idx_yg_dicek < 0:
					idx_yg_dicek += self.size
				i+=1
			
			if	self.data[idx_yg_dicek] == key:
				print("-- Probe",i,"- posisi id:",idx_yg_dicek,"berisi data",key)
				print("Data",key, "ditemukan pada posisi:",idx_yg_dicek)
				return idx_yg_dicek
			else:
				print("-- Probe",i,"- posisi id:",idx_yg_dicek,"KOSONG")
				print("Data",key, "tidak ada pada hash",idx_yg_dicek)
				return -1	 
				
	def delete(self, key):
		print("\n>>Prosedur Delete dilakukan")
		print("Data target:",key)
		idx_data = self.search(key)
		if idx_data== -1:
			print("Prosedur delete gagal dilakukan")
		else:
			self.data[idx_data] ="D"
			self.bnykIsi = self.bnykIsi - 1			
		
T = hash(10)
print(T.data)
T.insert("BOGOR") #2
print(T.data)
T.insert("BEKASI")
print(T.data)
#T.insert("BANDUNG")
#T.insert("BANYUWANGI")
#T.insert("BANJARMASIN")
T.insert("GRESIK")
print(T.data)	
print(T.bnykIsi)
#T.search("BANYUWANGI")
T.insert("CIREBON")
T.insert("CIAMIS")
T.insert("CILEGON")
hasil = T.search("CIANJUR")
print(hasil)
hasil = T.search("CIAMIS")
print(hasil)

T.visualisasi()

T.delete("CIAMIS")
T.visualisasi()		
print(T.data)
T.insert("ENDE")
T.visualisasi()


