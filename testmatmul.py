from matmul import readm, matmul

# 1. read matrix A from 'A.csv'
A = readm('A.csv')
# 2. read matrix b from 'b.csv'
b = readm('b.csv')
# 3. find the result of C = A x b
# 4. print C
C = matmul(A, b)
print('----')
for row in C:
    print(row)
print('----')
# import numpy as np
# D = np.dot(np.array(A), np.array(b))
# print(D)