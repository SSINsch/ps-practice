from collections import Counter

word = input()
word = word.upper()
word_dict = Counter(word)
max_k = max(word_dict, key=word_dict.get)

flag = False
for k in word_dict:
    if (word_dict[max_k] == word_dict[k]) and (k != max_k):
        flag = True        

if flag is True:
    print('?')
else:
    print(max_k)
