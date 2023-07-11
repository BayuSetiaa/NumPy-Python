import numpy as np

A = np.array(([2,3],[1,2]))
Y = np.array([23,14])

print(A)
print(Y)
print()

A_inv = np.linalg.inv(A)

#Menyelesaikan persamaan linear
X1 = np.dot(A_inv,Y)
print(X1)
print()

#Cara lain -> intinya baca aja dokumentasi numpy supaya tau tools2 lain seperti solve
X2 = np.linalg.solve(A,Y)
print(X2)

