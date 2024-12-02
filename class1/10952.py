added = []
while True:
    a, b = map(int, input().split())
    if (a == 0) and (b == 0):
        break
    added.append(a+b)
    
for i in added:
    print(i)