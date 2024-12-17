n = int(input())

list_q = []
for i in range(n):
    test = input()
    list_q.append(test)
    
for q in list_q:
    tot_score, score = 0, 0
    for x in q:
        if x == 'O':
            score = score + 1
        else:
            score = 0
        tot_score = tot_score + score
    print(tot_score)