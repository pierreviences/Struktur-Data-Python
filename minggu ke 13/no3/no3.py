'''
print("Nama 	: Muhamad yazid Imani ")
print("NIM 	: J0303211068 ")
print("Prodi 	: Manajemen Informatika ")
'''
class graph:
	def __init__(self,n,V):
		self.size = n
		self.vertexs = []          #set vertex-vertex
		for i in range(n):
			v = vertex(i,V[i])
			self.vertexs.append(v)
		self.AM = []               #adjacency matrix
		for i in range(n):
			baris = []
			for j in range(n):
				baris.append(0)
			self.AM.append(baris)	
	
	def vertexs_info(self):
		print('\nINFO VERTEXS---------------------------------------------')
		print('id\tlabel\twarna\tdist\tpred')
		print('---------------------------------------------------------')
		for i in range(self.size):
			print(self.vertexs[i].id,end='\t')
			print(self.vertexs[i].label,end='\t')
			print(self.vertexs[i].warna,end='\t')
			print(self.vertexs[i].distance,end='\t')
			if self.vertexs[i].pred == None:
				print(None)
			else:	
				print(self.vertexs[self.vertexs[i].pred].label)
		print('---------------------------------------------------------')
			
			
	def print_AM(self):
		print('\nADJACENCY MATRIX -------------------------')
		print('     ',end='')
		for i in range(self.size):
			print('[',self.vertexs[i].label,']',sep='',end="   ")
		print("")	
		
		for i in range(self.size):
			print('[',self.vertexs[i].label,']',sep='',end="   ")
			for j in range(self.size):
				print(self.AM[i][j],end="     ")
			print("")	
		print('\n------------------------------------------')
	
	def label2id_vertex(self,idx):
		id_hsl = None
		for i in range(self.size):
			if self.vertexs[i].label == idx:
				id_hsl = i
		return id_hsl		
	
	#directed graph
	def add_edge(self,u,v, bobot): #u dan v adalah label vertex
		id_u = self.label2id_vertex(u)
		id_v = self.label2id_vertex(v)
		print("Menambahkan edge (",u,",",v,")")
		if id_u == None:
			print(">> Tidak bisa karena vertex",u,"tidak ada")
			return
		elif id_v==None:
			print(">> Tidak bisa karena vertex",v,"tidak ada")		
			return
		#bisa
		self.AM[id_u][id_v] = bobot
			
	def BFS(self, v_awal):
		id_v_awal = self.label2id_vertex(v_awal)
		if id_v_awal == None:
			print("Vertex awal",v_awal,"tidak ada")
			print("BFS dihentikan.")
			return
		self.vertexs[id_v_awal].warna = 'gray'
		self.vertexs[id_v_awal].distance = 0
		
		Q = queue(self.size)
		Q.enqueue(id_v_awal)
		while  Q.isempty() != True:
			#baik u dan v berupa id dari vertex
			id_u = Q.dequeue()
			for id_v in range(self.size):
				if self.AM[id_u][id_v]==1 and self.vertexs[id_v].warna == 'white':
					self.vertexs[id_v].warna = 'gray'
					self.vertexs[id_v].distance = self.vertexs[id_u].distance+1 
					self.vertexs[id_v].pred = id_u
					Q.enqueue(id_v)
			self.vertexs[id_u].warna = 'black'		
	
	def dijkstra(self,v_awal): #membuat fungsi dijkstra 
		print("\n>> ALGORITMA DIJSKTRA DIJALANKAN")
		id_vawal = self.label2id_vertex(v_awal)
		if id_vawal==None: #kondisi jika id vertek awal tidak ada
			print("Vertex",v_awal,"tidak ada.")
			return
		print("Vertex awal:",v_awal)	
		self.vertexs[id_vawal].distance = 0
		S = []
		Q = []
		for i in range(self.size): #lopping dengan range banyaknya vertek
			Q.append(self.vertexs[i].label)
		print('S:',S)
		print('Q:',Q)
		while len(Q)>0 :
			self.vertexs_info()
			id_v_ekstrak = self.ekstrak_min(Q)
			u = Q.pop(id_v_ekstrak)
			print("Vertex yang diekstrak:",u)
			print('Q setelah ekstrak min :',Q)
			S.append(u)
			print('S:',S)
			id_vert_u = self.label2id_vertex(u)
			self.vertexs[id_vert_u].warna = 'black'
			for id_vert_v in range(self.size):
				if self.AM[id_vert_u][id_vert_v]!= 0 and self.vertexs[id_vert_v].warna != 'black':
					self.Relax(id_vert_u,id_vert_v)
						
	def Relax(self, id_vert_u,id_vert_v):
		#print('-------->',id_vert_u,id_vert_v)
		#print('*',self.vertexs[id_vert_v].distance)
		#print('**',self.vertexs[id_vert_u].distance)
		#print('***',self.AM[id_vert_u][id_vert_v])
		
		if self.vertexs[id_vert_v].distance=='infnt' or self.vertexs[id_vert_v].distance > self.vertexs[id_vert_u].distance + self.AM[id_vert_u][id_vert_v]:
			 self.vertexs[id_vert_v].distance = self.vertexs[id_vert_u].distance + self.AM[id_vert_u][id_vert_v]
			 self.vertexs[id_vert_v].pred = id_vert_u 
		
	# H = ['s', 't', 'x', 'y', 'z']	
	def ekstrak_min(self,H):
		#print('H:',H)
		id_v_dis_min = self.label2id_vertex(H[0])
		posisi_di_himpunan = 0
		if self.vertexs[id_v_dis_min].distance == 'infnt':
			min_distance_current = 1000000
		else:
			min_distance_current = 	self.vertexs[id_v_dis_min].distance
		
		for i in range(1,len(H)):
			#print('min_distance_current:',min_distance_current)	
			id_v_kandidat = self.label2id_vertex(H[i])
			#print(H[i],self.vertexs[id_v_kandidat].distance)
			if self.vertexs[id_v_kandidat].distance == 'infnt':
				continue
			if self.vertexs[id_v_kandidat].distance < min_distance_current: 
				id_v_dis_min = id_v_kandidat
				min_distance_current = self.vertexs[id_v_kandidat].distance
				posisi_di_himpunan = i
		#print('id_v_dis_min:',id_v_dis_min,'-->posisi_di_himpunan',posisi_di_himpunan)
		
		return 	posisi_di_himpunan	
				
class vertex:
	def __init__(self,i,lbl):
		self.id = i
		self.label = lbl
		self.warna = 'white'
		self.distance = 'infnt'
		self.pred = None
		

class queue:
	def __init__(self, n):
		self.kapasitas = n
		self.data = []
		
	def info(self):
		print("\nINFO QUEUE")
		print("------------------------------------------")
		print("Kapasitas:",self.kapasitas)
		print("Banyak item terisi:",len(self.data))
		if len(self.data)>0:
			print("Depan:",self.data[0])
			print("Belakang:",self.data[ len(self.data)-1 ])
		else:
			print("Depan: N/A")
			print("Belakang: N/A")	
		print("------------------------------------------")
		self.cetakQueue()
	
	def cetakQueue(self):
		
		for i in range(self.kapasitas):
			print("   [%2d]   "%(i),end="  ")
		print("")	
		for i in range(self.kapasitas):
			print("----------",end="  ")	
		print("")
		#mencetak isi setiap posisi pada antrian
		jpsti = len(self.data)
		for i in range(self.kapasitas):
			if i<jpsti:
				print("%9s "%(self.data[i]),end="<<")
			else:	
				print("%10s"%(""),end="<<")
		print("")	
		for i in range(self.kapasitas):
			print("----------",end="  ")
		print("")			
		
	def isfull(self):
		if len(self.data)==self.kapasitas:
			return True
		else:
			return False
					
	def enqueue(self,x):
		if self.isfull():
			print(x,"gagal di-enqueue (Queue Penuh, Overflow)")
		else:
			self.data.append(x)			
			print(x,"di-enqueue kedalam antrian")
	
	def isempty(self):
		if len(self.data)== 0:
			return True
		else:
			return False	
	
	def dequeue(self):
		if self.isempty():
			print("Proses dequeue gagal dilakukan, Queue kosong Underflow")
			return None
		else:
			hasil  = self.data.pop(0) #yg depan
			print(hasil,"di-dequeue dari antrian")
			return hasil
						
		

G1 = graph(11,['a','b','c','d','e','f','g','h','i','j','z'])
G1.print_AM()

G1.add_edge('a','b',4)
G1.add_edge('a','e',1)
G1.add_edge('a','h',6)
G1.add_edge('b','a',4)
G1.add_edge('b','c',1)
G1.add_edge('b','e',6)
G1.add_edge('b','f',4)
G1.add_edge('c','b',1)
G1.add_edge('c','d',6)
G1.add_edge('c','f',3)
G1.add_edge('d','c',6)
G1.add_edge('d','g',1)
G1.add_edge('d','z',1)
G1.add_edge('e','a',1)
G1.add_edge('e','b',6)
G1.add_edge('e','f',6)
G1.add_edge('e','h',8)
G1.add_edge('f','b',4)
G1.add_edge('f','c',3)
G1.add_edge('f','e',6)
G1.add_edge('f','g',5)
G1.add_edge('f','i',2)
G1.add_edge('g','d',1)
G1.add_edge('g','f',5)
G1.add_edge('g','z',1)
G1.add_edge('g','i',1)
G1.add_edge('g','j',2)
G1.add_edge('h','a',6)
G1.add_edge('h','e',8)
G1.add_edge('h','i',8)
G1.add_edge('i','f',2)
G1.add_edge('i','g',1)
G1.add_edge('i','h',8)
G1.add_edge('i','j',3)
G1.add_edge('j','g',2)
G1.add_edge('j','i',3)
G1.add_edge('j','z',3)
G1.print_AM()

G1.dijkstra('a')
G1.vertexs_info()
