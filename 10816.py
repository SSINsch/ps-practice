import sys
from collections import Counter

N = int(sys.stdin.readline().strip())
n_numbers = list(map(int, input().split()))
set_n_numbers = set(n_numbers)

M = int(sys.stdin.readline().strip())
m_numbers = list(map(int, input().split()))

counter = Counter(n_numbers)

for num in m_numbers:
    if num in set_n_numbers:
        print(counter[num], end=' ')
    else:
        print(0, end=' ')