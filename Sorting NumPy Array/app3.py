import numpy as np

tipe = [('nama','S10'),('tinggi',int)]

data = [('freya',170),
        ('ashel',150),
        ('adel',160)]

a = np.array(data, dtype=tipe)
print(a)
print()

#Mengurutkan data
print(np.sort(a,order='tinggi')) #Order artinya mengurutkan berdasarkan apa
print()
print(np.sort(a,order='nama')) #Ini mengurutkan berdasarkan nama
