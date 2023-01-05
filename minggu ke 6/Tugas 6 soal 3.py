print("Nama : Cut Yasmin Zafira ")
print("NIM : J0303211047 ")
print("INF A - Manajemen Informatika ")
print("============TUGAS PRAKTIKUM================== \n")

class queue: #membuat class
	def __init__(self, n): #membuat kontruktor dengan parameter self itu sendiri
		self.kapasitas = n #membuat variabel self.kapasitas dengan parameter n
		self.data = [] #list kosong

	def info(self): #memmbuat fungsi info dari queue
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
		print ("Visualisasi Queue")
		self.cetakQueue()
		
	def cetakQueue(self):
		for i in range(self.kapasitas-1,-1,-1):
			print("   [%2d]   "%(i+1),end="  ")
		print("")	
		for i in range(self.kapasitas):
			print("----------",end="  ")	
		print("")
		#mencetak isi setiap posisi pada antrian
		for i in range(self.kapasitas-1,-1,-1):
			if i<len(self.data):
				print("%9s "%(self.data[i]),end="  ")
			else:	
				print("%10s"%(""),end="  ")
		print("[DEPAN]")	
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
			self.data = self.data + [x]	
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
			hasil  = self.data.pop(0) 
			print(hasil,"di-dequeue dari antrian")
			return hasil
						
			
Q = queue(5)
Q.info()#1
Q.enqueue("Matahari")
Q.enqueue("Bulan")
Q.enqueue("Bintang")
Q.info()#2
Q.dequeue()		
Q.info()#2

#ini tu kalau dipanggil dequeuenya error
