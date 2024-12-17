n, x = map(int, input().split())
list_n = list(map(int, input().split()))

items = []
for i in list_n:
    if i < x:
        items.append(str(i))

print(' '.join(items))