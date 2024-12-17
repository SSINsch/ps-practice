import sys

n = int(sys.stdin.readline())

tot = 1
round = 1

while n > tot:
    tot = tot  + 6*round
    round = round + 1
    
print(round)