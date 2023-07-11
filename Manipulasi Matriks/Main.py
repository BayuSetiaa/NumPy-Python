import numpy as np

a = np.array(([1, 2, 3],
              [4, 5, 6]))

print(f'Matrik a dengan ukuran {a.shape}') #Shape mengambil ukuran matriks
print(a)
print()
#Transpose Matriks (Mengubah Baris Jadi kolom)
print(a.transpose()) #Cara Pertama
print()
print(np.transpose(a)) #Cara Kedua
print()
print(a.T) #Cara menggunkan getter setter

#Flatten array ,vektor baris
print()
print(a.flatten()) #Cara Pertama
print()
print(a.ravel()) #Cara Kedua
print()
print(np.ravel(a)) #Cara Ketiga

#Reshape Matriks
print()
print(a.reshape(3,2))
print()
print(a.reshape(6,1)) 
print()

#Resize Matriks
a.resize(3,2)
print(a)
print(f'Matrik a dengan ukuran {a.shape}')

#Ada banyak lagi tools2 kayak gitu tinggal bukak lagi aja dokumentasi di numpy

