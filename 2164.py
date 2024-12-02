import sys

N = int(sys.stdin.readline().strip())

# 규칙
# (1), (2), (2, 4), (2, 4, 6), (2, 4, 6, 8), ..., (2, 4, ...2k)
answer = [1, 2]
k = 1
while len(answer) <= (N+1):    
    for i in range(1, pow(2, k)+1):
        x = 2 * i
        answer.append(x)
    k = k + 1

print(answer[N-1])