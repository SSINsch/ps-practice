n = int(input())
list_num = list(map(int, input().split()))
max_v = max(list_num)

tot = 0
for num in list_num:
    x = (num / max_v) * 100
    tot = tot + x

print(tot/n)