import numpy as np

a = np.array([1,2,3])
b = np.array([4,5,6])

aMat = np.zeros((2,3))
bMat = np.ones((2,3))

#Stacking Matriks atau Menumpuk Matriks
c = np.hstack((a, b)) # hstack -> h artinya horizontal , a,b -> artinya urutanya terlebih dahulu
d = np.vstack((b, a)) # vstack -> v artinya vertikal , b,a -> v artinya urutanya terlebih dahulu

cMat = np.hstack((aMat,bMat))
dMat = np.vstack((aMat,bMat))

print(c)
print()
print(d)
print()
print(cMat)
print()
print(dMat)
