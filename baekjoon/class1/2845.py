l, p = map(int, input().split())
nPeople = l * p

answer = []
list_paper = list(map(int, input().split()))
for i in list_paper:
    answer.append(str(i-nPeople))
    
print(' '.join(answer))