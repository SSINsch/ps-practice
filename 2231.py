import sys

n = int(sys.stdin.readline())

# N이 주어졌을 때, 가장 작은 N의 생성자
# 즉, (각 자리수 + M)을 더해서 N이 되는 수 M
# 전수조사

def sum_of_digits(number):
    digits = [int(digit) for digit in str(number)]
    total = sum(digits)
    return total

for i in range(1, n + 1):
    # 각 자리수 더하기
    num = sum_of_digits(i)
    num_sum = i + num    
    if num_sum == n:
        print(i)
        break
    if i == n:
        print(0)