'''
============TUGAS PRAKTIKUM============
Nama : Muhamad yazid Imani
NIM : J0330211068
Prodi : Manajemen Informatika
'''

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
#membuat dictionary dengan 4 key dan 4 value kemudian dimasukkan kedalam variabel mydict
# yang dimana masing masing key mempunyai value
# key cat mempunyai value 12
# key dog mempunyai value 6
# key elephant mempunyai value 23
# key bear mempunyai value 20

answer = mydict.get("cat") // mydict.get("dog")
# mengambil value dari key "cat" dan key "dog" didalam dictionary mydict setelah itu dilakukan operator floor division antara value tersebut kemudian dimasukkan kedalam answer

print(answer)
# mencetak variabel answer dengan type data int 

print("===================")
# mencetak garis 

mydict = {"cat":12, "dog":6, "elephant":23, "bear":20}
#membuat dictionary dengan 4 key dan 4 value kemudian dimasukkan kedalam variabel mydict
print(23 in mydict)
# mencari nilai kebeneran apakah 23 merupakan key yang ada pada dictionary mydict
# apabila benar, maka program akan mencetak true, dan namun jika tidak program akan mencetak false.
