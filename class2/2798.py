n, m = map(int, input().split())
list_card = list(map(int, input().split()))

result = 0
for i in range(n):
    for j in range(i+1, n):
        for k in range(j+1, n):
            if list_card[i] + list_card[j] + list_card[k] > m:
                continue
            else:
                result = max(result, list_card[i] + list_card[j] + list_card[k])
                
print(result)