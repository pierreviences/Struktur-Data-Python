print("NIM : J0330211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")
def binarysearch(data, x, kiri, kanan):
	if kiri <= kanan:
		tengah = (kiri+kanan)//2
		if data[tengah] == x:
			return tengah
		elif data[tengah]>x:
			return binarysearch(data,x,kiri,tengah-1)
		else:
			return binarysearch(data,x,tengah+1,kanan)
	else:
		return -1

data = [1,3,4,6,7,8,10,13,14,18,19,21,24,37,40,45,71]
target = 7
print("Data ",target, "ditemukan di index ke ",binarysearch(data,target,0,len(data)-1))
