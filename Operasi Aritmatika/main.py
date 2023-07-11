import numpy as np

#List python
a = [1,2,3,4,5]
b = [6,7,8,9,10]

#Array Numpy
a_np = np.array([1,2,3,4,5])
b_np = np.array([6,7,8,9,10])

#ELEMENTWISE operation atau Operasi antar elemen bukan operasi matriks
#Penjumlahan
hasil_np1 = a_np + b_np

#Pengurangan 
hasil_np2 = a_np - b_np

#Perkalian
hasil_np3 = a_np * b_np

#Pembagian 
hasil_np4 = a_np / b_np

#Kuadrat
hasil_np5 = a_np **2


#Multidimensi Array Numpy
c = np.array(([1,2,3],[4,5,6]))
d = np.array(([7,8,9],[-1,-2,-3]))

hasil1 = c + d
hasil2 = c * d

print(hasil1)
print()
print(hasil2)


# print('---HASIL ARRAY NUMPY---')
# print('Penjumlahan')
# print(hasil_np1)
# print('Pengurangan')
# print(hasil_np2)
# print('Perkalian')
# print(hasil_np3)
# print('Pembagian')
# print(hasil_np4)
# print('Kuadrat')
# print(hasil_np5)


