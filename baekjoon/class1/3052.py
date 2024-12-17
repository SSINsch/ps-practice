list_n = []

for i in range(10):
    n = int(input())
    list_n.append(n)

reminder = []
for n in list_n:
    reminder.append(str(n % 42))
    
num = len(set(reminder))
print(num)