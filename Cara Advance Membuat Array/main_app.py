import numpy as np

#Membuat Matriks dengan tipe data tertentu
a = np.array(([1, 2, 3],[4, 5, 6]), dtype = float)

#Membuat array dengan menggunakan function
def kuadrat(baris,kolom):
  return kolom**2

def jumlah(baris,kolom):
  return kolom + baris

# b = np.fromfunction(fungsi,ukuran matriks ,tipe)
b = np.fromfunction(kuadrat,(1,10),dtype=int)
c = np.fromfunction(jumlah,(4,4),dtype=int)

#Membuat array atau matriks dengan menggunakan iterable 
iterable1 = (x*x for x in range(5))
iterable2 = (x*2 for x in range(5))

d = np.fromiter(iterable1,dtype=int)
e = np.fromiter(iterable2,dtype=int)

#Multitype array
dtipe = [('nama','S255'),('tinggi',int)]
data = [('freya',150),
        ('ashel',160),
        ('adel',180)]

f = np.array(data,dtype=dtipe)

print(f)
print()
print(f[0]) #Cara mengambil membernya 