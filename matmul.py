def readm(fname='A.csv'):
    f = open(fname, 'r') # w, b
    A = []
    for line in f.readlines():
        A.append( [ float(x) for x in line.strip().split(',') ] )
    f.close()
    return A

def matmul(A, b):
    m, n = len(A), len(b[0])
    J = len(A[0]) # A ~ mxJ   # b ~ Jxn
    if len(A[0]) == len(b):
        C = [ [0]*n for i in range(m) ]
        for r in range(m):
            for c in range(n):
                C[r][c] = sum([ A[r][j]*b[j][c] for j in range(J) ])
        return C
    return [] # ไม่สามารถคูณได้
