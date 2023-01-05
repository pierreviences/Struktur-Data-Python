print("Nama : Muhamad Yazid Imani")
print("NIM : J0303211068 ")
print("Prodi : Manajemen Informatika ")
print("============TUGAS PRAKTIKUM=================== \n")

def bubblesort(alist):
    awal = 0
    for j in range(len(alist)-1):
        for i in range(len(alist)-1-j):
            if alist[i]>alist[i+1]:
                alist[i],alist[i+1]=alist[i+1],alist[i]
        awal+=1
        print("urutan ke ",awal,":",alist)
    return alist
 
alist = [5, -3, 2, 0, -6, 8]
print("Urutan langkah buble sort : ")
bubblesort(alist)

print("hasil akhir : ", alist)
