import sys

n = int(sys.stdin.readline())
target = sys.stdin.readline()
alphabet_mapping = {chr(i): i - ord('a') + 1 for i in range(ord('a'), ord('z') + 1)}

r = 31
M = 1234567891

H = 0
for i in range(n):
    H = H + alphabet_mapping[target[i]] * pow(r, i)
    H = H % M
    
print(H)