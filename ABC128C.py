n, m = map(int, input().split())
connect_switch = [[] for _ in range(m)]
on_switch = [[] for _ in range(m)]
for i in range(m):
    connect_switch[i] = list(map(int, input().split()[1:]))
    on_switch[i] = connect_switch[i]

condition = list(map(int, input().split()))

for bit in range(1<<n):
    is_switch_on = [False] * m
    is_light_on = [False] * n
    for i in range(m):
        if 1 & (bit>>i):
            is_switch_on[i] = True

    for i in range(n):
        for j in range(len(connect_switch[i])):
            if is_switch_on[connect_switch[i][j]-1]:
                on_switch[i][j] = 1
            else:
                on_switch[i][j] = 0
    print(is_switch_on)
    print(on_switch)

#print(connect_switch)
#print(condition)