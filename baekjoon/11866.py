import sys

N, K = map(int, sys.stdin.readline().split())
numbers = [i for i in range(1, N+1)]

answer = []
idx = 0
while len(numbers) > 0:
    idx = idx + (K - 1)
    if idx >= len(numbers):
        idx = idx % len(numbers)
    answer.append(str(numbers.pop(idx)))

answer = ', '.join(answer)
print(f'<{answer}>')