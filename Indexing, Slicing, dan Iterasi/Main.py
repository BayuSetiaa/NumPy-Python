import numpy as np

a = np.arange(10)**2
print(a)

#Mengambil Nilai
print(f'Elemen ke 1 adalah = {a[0]}')
print(f'Elemen ke 7 adalah = {a[6]}')
print(f'Elemen ke akhir adalah = {a[-1]}')

#Slicing
print(f'Elemen dari 1-6 adalah = {a[0:6]}') # [start, end]
print(f'Elemen dari 4 sampai akhir adalah = {a[3:]}')
print(f'Elemen dari awal sampai 5 adalah = {a[:5]}')

#Iterasi
for i in a:
  print(f'Value = {i}')
