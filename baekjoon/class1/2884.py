h, m = map(int, input().split())
minutes = h * 60 + m
wake_minutes = minutes - 45

if wake_minutes < 0:
    wake_minutes = wake_minutes + 60*24

new_h = wake_minutes // 60
new_m = wake_minutes % 60
print(f'{new_h} {new_m}')