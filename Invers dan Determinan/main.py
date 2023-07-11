import numpy as np

a = np.array(([1,-1],[1,1]))

print(a)
print()

#Invers matriks
a_inv = np.linalg.inv(a)
print(a_inv)
print()

#Pembuktian invers matriks -> kalau dikalikan hasilnya matriks satuan / identitas
print(np.dot(a, a_inv)) #Note : perkalian matriks itu pakai dot
print()

#Determinan matriks
det_a = np.linalg.det(a)
det_a_inv = np.linalg.det(a_inv)

print(det_a)
print()
print(det_a_inv)


