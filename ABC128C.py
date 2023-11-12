import numpy as np

n, m = map(int, input().split())
connect_switch = np.full((m, n), 0)
light = np.full((m, n+2), 0)

for i in range(m):
    for j, sw_num in enumerate(list(map(int, input().split()[1:]))):
        connect_switch[i][j] = sw_num

for i, p in enumerate(list(map(int, input().split()))):
    light[i][n+1] = p

ans = 0

for bit in range(1<<n):
    is_on_switch = [False]*n
    is_all_on = True

    for i in range(n):
        if 1 & bit >> i:
            is_on_switch[i] = True

    is_on_switch.insert(0, False)

    for i in range(m):
        for j in range(n):
            light[i][j] = is_on_switch[connect_switch[i][j]]

    for i in range(m):
        light[i][n] = sum(light[i][:n])%2

    for i in range(m):
        if not light[i][n] == light[i][n+1]:
            is_all_on = False

    if is_all_on:
        ans += 1
print(ans)