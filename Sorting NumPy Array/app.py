import numpy as np

a = np.floor(np.random.randn(1,6)*10) #Memunculkan array random dikalikan 10, floor artinya membulatkan kebawah

print(a)

print(f'Nilai Maksimum dari a = {a.max()}')
print(f'Posisi Maksimum dari a = {a.argmax()}') #Note : indexs dimulai dari 0

print(f'Nilai Minimum dari a = {a.min()}')
print(f'Posisi Minimum dari a = {a.argmin()}') 

#Mengurutkan Nilai
print('Mengurutkan nilai a')
print(np.sort(a))
#Mengurutkan berdasarkan argument atau indexs yang tadinya belum terurut menjadi urut indexs nya ex : 2 indexs awal di nomor 1 terus di hasil argsort diletakan di indexs awal kalu nilainya paling kecil
print(np.argsort(a))

