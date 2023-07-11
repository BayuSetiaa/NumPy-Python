import numpy as np

a = np.floor(np.random.randn(2,2)*10) #Memunculkan nilai matriks 2x2 random
print(a)

print(f'Nilai Maksimum dari a = {a.max()}')
print(f'Posisi Maksimum dari a = {a.argmax()}') 
print(f'Nilai Minimum dari a = {a.min()}')
print(f'Posisi Minimum dari a = {a.argmin()}') 

print('Mengurutkan nilai a')
print(np.sort(a))
print(np.argsort(a))

