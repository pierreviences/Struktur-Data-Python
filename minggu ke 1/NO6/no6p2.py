'''
============TUGAS PRAKTIKUM============
Nama : Muhamad yazid Imani
NIM : J0330211068
Prodi : Manajemen Informatika
'''

capitals = {"Austria":"Vienna", "Germany":"Berlin"}
#membuat dictionary dengan 2 key dan 2 value kemudian dimasukkan kedalam variabel capitals
# yang dimana masing masing key mempunyai value
# key Australia mempunyai value Vienna
# key Germany mempunyai value Berlin

capital = capitals.pop("Austria")
'''
membuat variabel dengan nama capital
dimana dalam variabel ini terdapat method pop, yang berfungsi untuk menghapus item dari dictionary
dalam variabel ini item yang kita hapus merupakan value dari sebuah key = "Austria"
'''

print(capital)
# mencetak value dari item yang tadi dihapus sebelumnya


capital = capitals.pop("Indonesia", "Jakarta")
'''
seperti sebelumnya, kita juga menggunakan method pop
akan tetapi disini itemnya tidak ada di dalam dictionary capitals, dan ternyata program tidak error
dengan demikian method pop tidak harus menghapus item yang ada pada dictionary, item yang tidak ada juga tidak akan membuat 
error program 
'''

print(capital)
# mencetak value dari item yang tadi dihapus sebelumnya

capital = capitals.pop("Malaysia")
'''
seperti sebelumnya, kita juga menggunakan method pop
akan tetapi dalam variabel ini programnya menjadi error
dikarenakan, itemnya tidak ada di dalam dictionary capitals dan dalam method pop ini hanya di ketik keynya saja tanpa mengetik valuenya
'''

print(capital)
#mencetak variabel capital
