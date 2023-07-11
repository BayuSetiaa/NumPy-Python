import numpy as np

# Membuat Vektor 
a = np.array([1,2,3,4,5])
b = np.array([1.5,2.5,3.2,4,5])#vektor dengan koma 

#Membuat Vektor dengan range
c = np.arange(1,10,2)# 1 -> batas bawah , 2 -> batas atas , 2 -> stepnya / loncatnya ke bilangan berikutnya berapa bilangan

#Membuat linespace
d = np.linspace(1,10,4) # Menampilkan 4 angka diantara range 1-10 sama rata

#Array Multidimensi atau Matriks
e = np.array([ (1,2,3) , (4,5,6)]) # 123 -> baris pertama , 456 -> baris kedua

#Matriks dengan nilai 0
f = np.zeros((2,2)) # 2,2 -> berarti matriks 2x2

#Matriks dengan nilai 1
g = np.ones((2,2)) # 2,2 -> berati matriks 2x2

#Matriks Identitas
h1 = np.identity(3) # 3 -> artinya jumlah baris dan kolomnya 
h2 = np.eye(4) # 4 -> artinya jumlah baris dan kolom



#Display
print(a)
print(b)
print(c)
print(d)
print('---MATRIKS---')
print(e)
print('---MATRIKS NOL---')
print(f)
print('---MATRIKS NILAI 1---')
print(g)
print('---MATRIKS IDENTITAS---')
print(h1)
print()
print(h2)





