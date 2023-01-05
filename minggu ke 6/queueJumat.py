'''
Queue antrian
 - mengantri vaksin
 - mengantri membeli minyak goreng
 - mengantri tiket bioskop
 
 merah, biru, hijau
 - enqueue: memasukan item ke antrian
    di belakang selama tempat tersedia
    selainnya akan overflow
    
 merah, biru, hijau   
 - dequeue:  mengeluarkan item dari queue  
 selama masih ada item pada antrian
 underflow: kosong tapi ada dequeue
 
 FIFO: First In First Out
'''

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
						
			
Q = queue(5)
Q.info()#1
Q.enqueue("MERAH")
Q.enqueue("BIRU")
Q.enqueue("HIJAU")				
Q.info()#2
Q.enqueue("KUNING")
Q.enqueue("HITAM")
Q.enqueue("UNGU")
Q.info()#3
y = Q.dequeue()
z = Q.dequeue()
Q.info()#4

