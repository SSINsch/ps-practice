n, m = map(int, input().split())

matrixA = []
matrixB = []
for i in range(n):
    temp = list(map(int, input().split()))
    matrixA.append(temp)

for i in range(n):
    temp = list(map(int, input().split()))
    matrixB.append(temp)

matrixAns = []
for i in range(n):
    matrixA[i] + matrixB[i]
    temp = [sum(x) for x in zip(matrixA[i], matrixB[i])]
    matrixAns.append([str(x) for x in temp])
    
for i in range(n):
    print(' '.join(matrixAns[i]))