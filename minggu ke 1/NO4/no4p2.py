'''
============TUGAS PRAKTIKUM============
Nama : Muhamad yazid Imani
NIM : J0330211068
Prodi : Manajemen Informatika
'''

stok = {'mangga':100, 'jeruk':200, 'apel':600}
#membuat dictionary dengan 3 key dan 3 value kemudian dimasukkan kedalam variabel stok
# yang dimana masing masing key mempunyai value
# key mangga mempunyai value 100
# key jeruk mempunyai value 200
# key apel mempunyai value 600


for akey in stok.keys():
# melakukan perulangan dengan for  yang dimana program akan melakukan perulangan pengembalian daftar key dalam dictionary stok kedalam variabel akey
	
	print("Key", akey, "bernilai", stok[akey])
	#mencetak key dengan variabel akey dan valuenya yang dipanggil melalui variabel stok sesuai key satu persatu sampai habis dan tidak tersisa
	
for k in stok:
# melakukan perulangan dengan for yang dimana program akan melakukan perulangan pengembalian daftar key dalam dictionary stok kedalam variabel k 
	print(k, "bernilai", stok[k])
	#mencetak key dengan variabel k dan valuenya yang dipanggil melalui variabel stok sesuai key satu persatu sampai habis dan tidak tersisa

ks = list(stok.keys())
# membuat variabel ks, kemudian didalemnya dimasukkan variabel stok yang bertype data dictionary 
# namun hanya melakukan pengembalian seluruh daftar key setelah itu variabel tersebut diubah menjadi list 

print(ks)
# mencetak variabel ks yang bertype data list
