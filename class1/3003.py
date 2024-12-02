list_chess = list(map(int, input().split()))
white_chess = [1, 1, 2, 2, 2, 8]
answer = []

for i in range(len(list_chess)):
    answer.append(white_chess[i] - list_chess[i])

for i in answer:
    print(i, end=' ')