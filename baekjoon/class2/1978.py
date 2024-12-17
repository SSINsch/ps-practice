import math

def is_prime(n):
    m = int(math.sqrt(n))
    num_divisor = 1
    for i in range(2, m+1):
        if n % i == 0:
            num_divisor = num_divisor + 1
    if (num_divisor == 1) and (n != 1):
        return True
    else:
        return False

n = int(input())
list_n = list(map(int, input().split()))

num = 0
for i in list_n:
    flag_prime = is_prime(i)
    if flag_prime is True:
        num = num + 1
        
print(num)