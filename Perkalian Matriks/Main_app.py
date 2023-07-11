import numpy as np

a = np.array(([1,2],
              [3,4]))

b = np.ones([2,2])

#Perkalian Matriks
c1 = np.dot(a, b) #cara pertama
c2 = a.dot(b) #cara kedua


print(f'Matriks Pertama')
print(a)
print(f'Matriks Kedua ')
print(b)

print('Hasil Perkalian Matriks a dengan b')
print(c1)
print()
print(c2)
