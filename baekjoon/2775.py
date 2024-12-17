import sys

rooms = []
rooms.append([i for i in range(15)])
for _floor in range(1, 15):
    now = 0 
    temp = []
    for _number in range(15):
        now = now + rooms[_floor-1][_number]
        temp.append(now)
    rooms.append(temp)
    
T = int(sys.stdin.readline())
cases = []
for i in range(T):
    k = int(sys.stdin.readline())
    n = int(sys.stdin.readline())
    cases.append([k, n])

for i in range(len(cases)):
    k = cases[i][0]
    n = cases[i][1]
    print(rooms[k][n])