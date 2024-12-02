n = int(input())

user = []

for i in range(n):
    age, name = map(str, input().split())
    user.append([int(age),name])

for i in sorted(user,key=lambda x : x[0]):
    print(f'{i[0]} {i[1]}')