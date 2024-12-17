answer = []
list_q = []

while True:
    a, b, c = map(int, input().split())
    if (a == 0) and (b == 0) and (c == 0):
        break
    list_q.append((a, b, c))
    
for q in list_q:
    a, b, c = q
    max_v = max([a, b, c])
    if (a*a + b*b +c*c) == (2*max_v*max_v):
        answer.append('right')
    else:
        answer.append('wrong')
        
for i in answer:
    print(i)