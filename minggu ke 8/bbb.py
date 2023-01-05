def bublesort(data):
	awal = 0
	for j in range(len(data)-1):
		for i in range(len(data)-1-j):
			if data[i]>data[i+1]:
				data[i],data[i+1]=data[i+1],data[i]
		awal+=1
		print("urutan ke", awal,":",data)
	return data
data = [5, -3, 2, 0, -6, 8]
print("Urutan langkah buble sort : ")
bublesort(data)
print("Hasil akhir : ", data) 		


