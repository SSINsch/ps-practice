list_num = []
while True:
    a = input()
    if a == '0':
        break
    list_num.append(a)

for item in list_num:
    flag = True
    for i in range((len(item))//2):
        if item[i] != item[len(item) - 1 - i]:
            flag = False
            break
    if flag is True:
        print('yes')
    else:
        print('no')