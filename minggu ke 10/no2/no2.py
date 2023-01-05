'''
print("Nama 	: Muhamad yazid Imani ")
print("NIM 	: J0303211068 ")
print("Prodi 	: Manajemen Informatika ")
'''

class AVLNode: # membuat class AVLNode
    def __init__(self, nilai): #membuat method init
        self.nilai = nilai # variabel self.nilai berisi nilai parameter nilai
        self.kiri = None # variabel self.kiri berisi none
        self.kanan = None # variabel self.kanan berisi none
        self.tinggi = 1 # variabel self.tinggi berisi nilai 1

class AVLTree: #membuat class AVLTree
    def singleRightRotate(self, root): # membuat method single Rotation
		#simpan kedalam variabel
        data = root.kiri 
        data2 = data.kanan
        data.kanan = root
        root.kiri = data2
        root.tinggi = 1 + max(self.tinggi(root.kiri), self.tinggi(root.kanan))
        data.tinggi = 1 + max(self.tinggi(data.kiri), self.tinggi(data.kanan))
        return data #mengembalikan nilai data

    def doubleRotation(self, root):  # membuat method Double Rotation
		#simpan kedalam variabel
        data = root.kanan
        data2 = data.kiri
        data.kiri = root
        root.kanan = data2
        root.tinggi = 1 + max(self.tinggi(root.kiri), self.tinggi(root.kanan))
        data.tinggi = 1 + max(self.tinggi(data.kiri), self.tinggi(data.kanan))
        return data #mengembalikan nilai data
    
    def tinggi(self, root): #membuat method tinggi
        if root is None: # di cek jika root none, maka
            return 0 #kembalikan nilai 0
        else: #jika tidak
            return root.tinggi # kembalikan nilai root tertinggi
    def recInsertAVL(self, val, root): # membuat method insert
        if root is None: # cek dulu apakah rootnya none atau tidak
            return AVLNode(val) # jika iya, kembalikan nilai Node sesuai value yang diberikan
        elif val <= root.nilai: # cek lagi apakah nilai value lebih kecil samadengan dari nilai root
            root.kiri = self.recInsertAVL(val, root.kiri) #jika iya maka tambahkan data nilai tersebut ke sebelah kiri root
        elif val > root.nilai: # jika lebih besar
            root.kanan = self.recInsertAVL(val, root.kanan) #tambahkan data nilai tersebut ke sebelah kanan root
        root.tinggi = 1 + max(self.tinggi(root.kiri), self.tinggi(root.kanan))
        balanceFactor = self.balanceFactor(root)
        if balanceFactor > 1 and root.kiri.nilai > val: 
            return self.singleRightRotate(root)
        if balanceFactor < -1 and val > root.kanan.nilai:
            return self.doubleRotation(root)
        if balanceFactor > 1 and val > root.kiri.nilai:
            root.kiri = self.doubleRotation(root.kiri)
            return self.singleRightRotate(root)
        if balanceFactor < -1 and val < root.kanan.nilai:
            root.kanan = self.singleRightRotate(root.kanan)
            return self.doubleRotation(root)
        return root
    
    def balanceFactor(self, root): # membuat method balanceFactor
        if root is None: # di cek apakah root bernilai none, jika iya
            return 0 #kemabalikan nilai 0
        else: #jkta tidak
            return self.tinggi(root.kiri) - self.tinggi(root.kanan)
    def nilaiMinimum(self, root): # membuat method nilaiminimum
        if root is None or root.kiri is None:
            return root
        else:
            return self.nilaiMinimum(root.kiri)
    


    def recInOrder(self, root):
        if root is None:
            return
        print(root.nilai, end=" ")
        self.recInOrder(root.kiri)
        self.recInOrder(root.kanan)

avl = AVLTree() #membubat object avl
data = None # variabel data yang berisikan data None

# menambahkan nilai ke AVL TREE
data = avl.recInsertAVL(56, data) 
data = avl.recInsertAVL(42, data)
data = avl.recInsertAVL(81, data)
data = avl.recInsertAVL(24, data)
data = avl.recInsertAVL(45, data)
data = avl.recInsertAVL(62, data)
data = avl.recInsertAVL(99, data)
data = avl.recInsertAVL(15, data)
data = avl.recInsertAVL(30, data)
data = avl.recInsertAVL(43, data)
data = avl.recInsertAVL(55, data)
data = avl.recInsertAVL(58, data)
data = avl.recInsertAVL(69, data)
data = avl.recInsertAVL(94, data)
data = avl.recInsertAVL(100, data)
data = avl.recInsertAVL(10, data)
data = avl.recInsertAVL(21, data)
data = avl.recInsertAVL(28, data)
data = avl.recInsertAVL(32, data)
data = avl.recInsertAVL(46, data)

print(" ___________________________")
print("|                           |")
print("|          AVL TREE         |")
print("|___________________________|")
print(" ")
print(" -> ", end="")
#memanggil fungsi recinorder untuk menampilkan visualisasi avl tree ke layar
avl.recInOrder(data)
print("\n\n\n * Melakukan operasi Insert AVL nilai 26")
print(" ___________________________")
print("|                           |")
print("|          AVL TREE         |")
print("|___________________________|")
print(" ")
print(" -> ", end="")
# menambahkan nilai 26 ke avl tree
data = avl.recInsertAVL(26, data)
avl.recInOrder(data)
