import sys

N = int(sys.stdin.readline().strip())
a_numbers = set(map(int, input().split()))

M = int(sys.stdin.readline().strip())
b_numbers = list(map(int, input().split()))

for b in b_numbers:
    if b in a_numbers:
        print(1)
    else:
        print(0)