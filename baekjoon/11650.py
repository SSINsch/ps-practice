import sys

n = int(sys.stdin.readline())

matrix = []
for i in range(n):
    x, y = map(int, input().split())
    matrix.append((x, y))
    
matrix.sort()

for i,j in matrix:
    print(f"{i} {j}")