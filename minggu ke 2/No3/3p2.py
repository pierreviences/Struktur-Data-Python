'''
============TUGAS PRAKTIKUM============
Nama : Muhamad yazid Imani
NIM : J0330211068
Prodi : Manajemen Informatika
'''

fruits = {"apple" , "banana", "cherry"}
#Membuat tupple dengan 3 item yang berisikan apple, banana, cherry kemudian dimasukkan kedalam variabel fruits
fruits_baru = list(fruits)
#Mengubah type data set menjadi list yang ada di dalam variabel fruits kemudian di masukkan kedalam variabels fruits_baru
#Supaya item yang ada di dalam dapat di modifikasi
fruits_baru[1] = "pisang"
#Menganti item ke 2 yang ada di index 1 dalam variabels fruits_baru menjadi pisang
fruits_baru.append("jeruk")
#Menambah item baru yaitu jeruk menggunakan method append
fruits_baru = tuple(fruits_baru)
#Mengubah type data list menjadi tuple yang ada di dalam variabel fruits_baru kemudian di masukkan kedalam variabels fruits_baru lagi

print(fruits)
#mencetak variabel fruits dengan type data set yang merupakan data awal dan belum di modifikasi
print(fruits_baru)
#mencetak variabel fruits_baru dengan type data tuple yang data item awalnya sudah di modifikai
