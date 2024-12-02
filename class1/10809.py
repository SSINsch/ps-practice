sentence = input()
sentence = sentence[::-1]

answer = ['-1'] * 26
for i, char in enumerate(sentence):
    answer[ord(char)-97] = str(len(sentence)-(i+1))

print(' '.join(answer))