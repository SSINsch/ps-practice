n, k = map(int, input().split())

result = 1
for i in range(n-k+1, n+1):
    result = result * i
    
for i in range(1, k+1):
    result = result // i

print(result)