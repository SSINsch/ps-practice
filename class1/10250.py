t = int(input())

pairs = []

for i in range(t):
    h, w, n = map(int, input().split())
    pairs.append((h, w, n))

for p in pairs:
    h, w, n = p    
    # 나머지와 몫은 딱 떨어지는 경우가 있어서
    # 숫자 하나 빼서 계산하고 나중에 더하는 식으로
    distance = (n - 1) // h + 1
    floor = (n - 1) % h + 1
    print(f'{floor}{distance:02d}')