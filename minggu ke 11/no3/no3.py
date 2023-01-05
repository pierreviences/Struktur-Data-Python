'''
print("Nama : Muhamad Yazid Imani")
print("NIM : J0303211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
'''
class Graph:#membuat class graph
	def __init__(self, n): # membuat fungsi init
		self.size = n	#parameter n disimpan kedalam variabel self.size
		self.AM = []	#list kosong untuk membuat matriks adjacency
		for i in range(n):	
			self.AM.append([ 0 for j in range(n)])
		
	def cetak_AM(self):	#membuat fungsi cetak_AM untuk membuat visualisasi dari graph tsb
		print(" ________________________________________")
		print("|                                        |")
		print("|            VISUALISASI GRAPH           |")
		print("|________________________________________|")
		print()
		print("               ",end="")	
		for i in range(self.size):	
			print("",i,"", sep="",end="   ")
		print("\n             __________________")	
		print("            |                  |")
		for i in range(self.size):
			print("         ",i,"  |", sep="",end="  ")
			for j in range(self.size):
				print(self.AM[i][j],end="   ")
			print("|")
			if i != 3:
				print("            |                  |")
		print("            |__________________|")
		print()
		
	def tambah_edge(self, u, v):#membuat fungsi tambah_edge untuk menambahkan edge 
		print(" -> Menambahkan edge dari verteks",u,v)	
		self.AM[u][v] = 1  #menjadi nilai 1 ketika edge ditambahkan 
		self.AM[v][u] = 1
	
	def hapus_edge(self, u, v):#membuat fungsi hapus_edge untuk menghapus edge 
		if self.AM[u][v] == 0:	#cek apakah edge tersebut bernilai 0 atau tidak, jika iya maka
			print(" -> Edge",u,v,"tidak ada, penghapusan tidak dapat dilakukan")
			return	
		#edge berhasil dihapus dan nilai 1 diubah menjadi 0 
		self.AM[u][v] = 0
		self.AM[v][u] = 0	
		print(" -> Edge",u,v,"dihapus")
	
	def get_all_tetangga_verteks(self, id_vrtx):
		list_tetangga = []	#membuat list kosong kemudian dimasukkan kedalam var list_tetangga
		for j in range(self.size): # melakukan perulangan sampai jumlah size
			if self.AM[id_vrtx][j] == 1:  #jika nilai baris matriks tersebut sama dengan nilai kolom matriks yaitu 1, maka
				list_tetangga.append(j)	#index kolom matriks akan dimasukkan kedalam list list_tetangga
				print(" -> Verteks",j,"tetangga dari verteks",id_vrtx)
		return 	list_tetangga
			
			
G = Graph(4) #membuat objec G dri clash graph yang bersize 4
G.cetak_AM() # memanggil method cetak_Am()
#menambahkan edge
G.tambah_edge(0,1)
G.tambah_edge(1,3)
G.tambah_edge(0,3)
G.tambah_edge(1,2)		
G.cetak_AM()
#menghapus edge
G.hapus_edge(0,1)
G.hapus_edge(1,1)
G.cetak_AM()
V = G.get_all_tetangga_verteks(0)
print("   ",V)
