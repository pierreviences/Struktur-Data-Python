'''
============TUGAS PRAKTIKUM============
Nama : Muhamad yazid Imani
NIM : J0330211068
Prodi : Manajemen Informatika
'''

dishes = ["pizza", "sauerkraut", "paella", "hamburger"]
#membuat list dengan item pizzaa, sauerkraut, paella, hamburger kemudian dimasukkan kedalam variabel dishes
countries = ["Italy", "Germany", "Spain", "USA"]
#membuat list dengan item Italy, Germany, Spain, USA kemudian dimasukkan kedalam variabel countries
country_specialities = list(zip(countries, dishes))

'''
Menzip iterator countries dan dishes, dimana item yang ada pada setiap iterator digabungkan/dipasangkan sesuai dengan indexnya
iterator countries dan dhises yang sudah dizip  dikembalikan dalam bentuk tupel, kemudian diubah menjadi list dan di masukkan
kedalam variabel country_specialities
'''

print(country_specialities)
#mencetak variabel country_specialities dengan type data list

country_specialities_dict = dict(country_specialities)
#mengubah variabel country_specialities menjadi dictionary dan dimasukkan kedalam variabel country_specialities_dict

print(country_specialities_dict)
#mencetak variabel country_specialities_dict dengan type data dictionary
