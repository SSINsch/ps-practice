list_n = []
for i in range(9):
    n = input()
    list_n.append(int(n))
    
# index start from 0
print(max(list_n))
print(list_n.index(max(list_n)) + 1)