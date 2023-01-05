'''
print("Nama : Muhamad yazid Imani ")
print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
'''

class stack:
	# membuat class stack
	def __init__(self, n):
		# membuat method constructor dengan 2 parameter yaitu self dan n
		self.kapasitas = n
		# parameter n dimasukkan kedalam variabel self.kapasitas
		self.top = -1
		# membuat nilai default yaitu -1 kemudian dimasukkan kedalam variabel self.top
		self.data = []
		# membuat list kosong kemudian dimasukkan kedalam variabel self.data
		
	def info(self):
		# membuat method info
		print()
		print("-----------------------------")
		print("\tINFO STACK")
		print("-----------------------------")
		print("Kapasitas\t\t:",self.kapasitas)
		# mencetak jumlah kapasitas 
		print("Jumlah item pada stack\t:",len(self.data))
		# mencetak jumlah item pada stack
		if self.top == -1:
			# ngecek apakah nilai top == -1, artinya nilai top apakah kosong
			print("Top saat ini\t\t: N/A")
			# jika iya maka cetak ini
		else:	
			# jika tidak
			print("Top saat ini\t\t:",self.top,"(",self.data[self.top],")")
			# cetak nilai top kelayar dengan memanggil self.top dan juga mencetak nama data sesuai top saat ini
		self.printStack()
		# memanggil method printStack()
		print()
		# membuat baris baru
	
	def isFull(self):
		# membuat method isFull
		if self.kapasitas == len(self.data):
			#cek apakah jumlah kapasitas sama dengan jumlah data
			return True
			#jika iya maka return true
		else:
			return False	
			# jika tidak maka return false
			
	def push(self, x):
		# membuat method push dengan 2 parameter yaitu self dan x sebagai data yg akan di push
		if self.isFull():
		# cek apakah jumlah kapasitas full
			print(x,"tidak dapat di-push, Stack Full (Overflow)")
		else:
			self.data.append(x)
			# jika tidak maka nilai paramter x dimasukkan kedalam list yg ada di dalam variabel self.data
			self.top = 	len(self.data) - 1
			#jumlah banyaknya data dikurang 1 kemudian dimasukkan kedalam variabel self.top
			print("*",x,"di-push pada stack")
	
	def printStack(self):
		# membuat method printStack
		print("")
		for i in range(self.kapasitas-1, -1, -1):
			#lakukan perulangan dengan range sesuai jumlah kapasitas
			if i <= self.top: 
				# apakah index lebih kecil sama dengan nilai top
				print("%2d | %10s |"%(i,self.data[i]),end="")
				# cetak data ke layar sesuai index
				if i ==  self.top:
					# apakah nilai top sama dengan index
					print("<--- TOP",end="")
					# cetak <--- TOP ke layar
				print("")	
			else:
				#jika tidak
				print("%2d | %10s |"%(i,""))
				# cetak string kosong
		print("    ------------")		
	
	def isEmpty(self):
		# membuat method isEmpty
		if len(self.data)==0:
			#cek apakah jumlah data sama dengan 0
			return True
			# jika iya maka return True
		else:
			return False
			# jika tidak return false	
	
	def pop(self):
		# membuat method pop 
		if self.isEmpty():
			# cek apakah kapasitas kosong
			print("Stack kosong! Underflow")
			# jika iya maka cetak stack kosong ke layar
			return None
		else:
			# jika tidak
			hasil = self.data.pop()
			# hapus data yang paling diatas/diakhir
			self.top = self.top - 1
			#nilai top dikurang 1
			print("-----------------------------")
			print("*",hasil,"di-pop dari Stack")
			print("* Berhasil di pop")
			print("-----------------------------")
			#cetak ke layar
			return hasil 
			# return hasil
				
						
		
stacks = stack(6)
# membuat object stacks dengan memanggil kelas stack yang berisi argument angka 6		
stacks.info()
stacks.push("Rusia") 
stacks.push("Ukraina") 
# menambah data rusia dan ukraina ke dalam stack dengan method push
stacks.info()
# memanggil method info yang ada di dalam objec stacks
stacks.push("Korut")
stacks.push("Korsel")
# menambah data korut dan korsel ke dalam stack dengan method push
stacks.info()
# memanggil method info yang ada di dalam objec stacks
stacks.push("China")
stacks.push("Taiwan")
# menambah data china dan taiwan ke dalam stack dengan method push
stacks.info()
# memanggil method info yang ada di dalam objec stacks
stacks.pop()
#memanggil method pop untuk menghapus data yang paling atas
stacks.info()
# memanggil method info yang ada di dalam objec stacks


