import math

a, b = map(int, input().split())

# 유클리드 호제법
def get_gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def get_lcm(a, b):
    result = (a * b ) // get_gcd(a, b)
    return result

print(get_gcd(a, b))
print(get_lcm(a, b))