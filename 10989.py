# 8MB 메모리 제한 + 입력 받는 수의 범위가 매우 좁음
# => 계수정렬에 적합
import sys

#계수정렬 활용
n = int(sys.stdin.readline())

# 입력값이 10000개까지 주어지니 10000 + 1개의 리스트 선언
indices = [0] * (10000 + 1)

# 각 입력값에 해당하는 인덱스의 값 증가
# 배열의 위치는 숫자를 의미하고, 값은 해당 숫자가 몇 개인지
for _ in range(n):
    x = int(sys.stdin.readline())
    indices[x] = indices[x] + 1
  

for i in range(len(indices)):
    if indices[i] != 0:
        for _ in range(indices[i]):
            print(i)