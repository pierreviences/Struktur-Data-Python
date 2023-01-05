print("Nama 	: Muhamad yazid Imani ")
print("NIM 	: J0303211068 ")
print("Prodi 	: Manajemen Informatika ")


class CBT:
	def __init__(self,N):	
		self.maxsize = N
		self.data = []
	
	def add(self, x):
		self.data.append(x)
		
	def visual(self):
		print(" ____________________________________________")
		print("|                                            |")
		print("|            COMPLETE BINARY TREE            |")
		print("|____________________________________________|")
		print(" ")
		print(" -> Kapasitas Data : ", self.maxsize)	
		print(" -> Jumlah Data    : ", len(self.data))
		print(" -> Isi Data	   : ", self.data)
		
		
	def getCurrSize(self):
		return len(self.data)
		
	def getRoot(self):
		if self.getCurrSize() == 0:
			return None
		else:
			return self.data[0]
	
	def getNode_i(self,i):
		if self.getCurrSize() < i:
			return None
		else:
			return self.data[i]
	
	def getLeftChildNode_i(self,i):
		iKiri = 2*i+1
		bne = self.getCurrSize() 
		if  bne <= i:
			print("Node ke-",i,"tidak ada")
			return None
		elif bne <= iKiri:
			print("Node ke-",i,"tidak memiliki anak kiri")
			return None	
		else:
			return self.data[iKiri]
	
	def getRightChildNode_i(self,i):
		iKanan = 2*i+2
		bne = self.getCurrSize()
		print("debug KANAN>> Nilai BNE",bne,iKanan) 
		if  bne <= i:
			print("Node ke-",i,"tidak ada")
			return None
		elif bne <= iKanan:
			print("Node ke-",i,"tidak memiliki anak kanan")
			return None	
		else:
			return self.data[iKanan]
	
	def getParentNode_i(self,i):
		i_parent = (i-1)//2
		if i != 0:
			return self.data[i_parent]
		else:
			print("node adalah root dan tidak memiliki parent")
			return None	
	
	def getAllData(self):
		return self.data										

class HeapTree:
	def __init__(self, n, A):
		print(" ____________________________________________")
		print("|                                            |")
		print("|          PROSEDUR CBT TO HEAPTREE          |")
		print("|____________________________________________|")
		print(" ")
		print(" -> Kapasitas Data : ", n)	
		print(" -> Jumlah Data    : ", len(A))
		print(" -> Isi Data	   : ", A)
		print(" * Sebuah Heaptree dibuat, namun data masih berupa CBT dan belum pasti Heaptree")
		print()
		self.kap = n
		self.data = A
	
	def get_parent_index(self,i):
		if i== 0:
			return None
		else:	
			return (i-1)//2 	
	
	def heap_kan(self):
		bne = len(self.data)
		imax = bne - 1
		iparent_max = self.get_parent_index(imax)
		print(" -> Inisiasi Prosedur  ")
		print("    * Data			 :", self.data)
		print("    * Jumlah Data		 :", len(self.data))
		print("    * Index Terakhir	 	 :", imax)
		print("    * Data Index Terakhir	 :", self.data[imax])
		print("    * Index Parent Terakhir 	 :", iparent_max)
		print("    * Data Index Terakhir	 :", self.data[iparent_max])
		print("\n -> Prosedur dijalankan")
		for i in range(iparent_max,-1,-1):
			print("    * Rapihkan node index parent ke -",i)
			self.heapify(i)
			print("        -------------------------------------\n      ",self.data, "\n        -------------------------------------\n")
	
	def get_left_index(self,i):
		return 2*i+1
	
	def get_right_index(self,i):
		return 2*i+2	
		
	def heapify(self,i):
		max_idx = len(self.data) - 1
		i_q = self.get_left_index(i)
		i_k = self.get_right_index(i)
		if 	i_q <= max_idx and self.data[i_q]>self.data[i]:
			i_max = i_q 
		else:
			i_max = i
		
		if i_k <= max_idx and self.data[i_k]>self.data[i_max]:
			i_max = i_k
		
		if i_max != i:
			self.data[i],self.data[i_max] = self.data[i_max],self.data[i]
			self.heapify(i_max)	
	
	def remove(self, i):
		print(" ____________________________________________")
		print("|                                            |")
		print("|       REMOVE HEAPTREE SESUAI INDEX         |")
		print("|____________________________________________|")
		print(" ")
		print(" -> Target Index yang ingin dihapus : ", i)
		print(" -> Isi data yang ingin dihapus     : ", self.data[i])
		print(" \n -> Prosedur dijalankan")
		print("    Data Awal")
		print("   ",self.data,"\n")
		bne = len(self.data)
		imax = bne - 1
		iparent_max = self.get_parent_index(imax)
		if i == 0:
			self.data[0], self.data[-1] = self.data[-1], self.data[0]
			del self.data[-1]
			for i in range(iparent_max,-1,-1):
				print("    * Rapihkan node index parent ke -",i)
				self.heapify(i)
				
		else : 
			del self.data[i]
			for i in range(iparent_max,-1,-1):
				print("    * Rapihkan node index parent ke -",i)
				self.heapify(i)
		print(" \n -> Prosedur Berhasil di jalankan")		
				
		

# CBT
T1 =  CBT(10);
T1.add(19);T1.add(10);T1.add(20);T1.add(33);T1.add(8)
T1.add(57);T1.add(11);T1.add(16);T1.add(52);T1.add(7)
T1.visual()
datanya = T1.getAllData()
		 	
# HEAPTREE
T2=HeapTree(15,datanya)
T2.heap_kan()
print(" ____________________________________________")
print("|                                            |")
print("|                  HEAPTREE                  |")
print("|____________________________________________|")
print(" ")
print(" -> Kapasitas Data : ", T2.kap)	
print(" -> Jumlah Data    : ", len(T2.data))
print(" -> Isi Data	   : ", T2.data)
print(" * Sebuah Heaptree telah dibuat dan prosedur sukses dijalankan")
print(" \n Data Terakhir")
print("",T2.data,"\n\n\n")

# REMOVE HEAPTRE SESUAI INDEX
T2.remove(1)
print("    Data Terakhir")
print("   ",T2.data,"\n\n")

print(" ____________________________________________")
print("|                                            |")
print("|                  HEAPTREE                  |")
print("|____________________________________________|")
print(" ")
print(" -> Kapasitas Data : ", T2.kap)	
print(" -> Jumlah Data    : ", len(T2.data))
print(" -> Isi Data	   : ", T2.data)
print(" * Sebuah Heaptree telah dibuat dan prosedur sukses dijalankan")
print(" \n Data Terakhir")
print("",T2.data,"\n\n\n")

