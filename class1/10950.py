n = int(input())
list_num = []
for i in range(n):
    a, b = list(map(int, input().split()))
    list_num.append(a+b)

for i in list_num:
    print(i)