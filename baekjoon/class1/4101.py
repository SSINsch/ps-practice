q = []

while True:
    a, b = map(int, input().split())
    if (a == 0) and (b == 0):
        break
    q.append([a, b])

for i in range(len(q)):
    if q[i][0] > q[i][1]:
        print('Yes')
    else:
        print('No')