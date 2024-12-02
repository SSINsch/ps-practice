from collections import Counter

a = int(input())
b = int(input())
c = int(input())
num = a * b * c
str_num = str(num)
dict_num = Counter(str_num)

numbers = [str(i) for i in range(10)]
for i in numbers:
    if i in dict_num.keys():
        print(dict_num[i])
    else:
        print(0)