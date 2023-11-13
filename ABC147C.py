n = int(input())
statement = []

for i in range(n):
    m = int(input())
    a = []
    for j in range(m):
        x, y = map(int, input().split())
        a.append([x, y])
    statement.append(a)

ans = 0

for bit in range(1<<n):
    is_ok = True
    person = [-1] * n
    for i in range(n):
        if 1 & bit>>i:
            person[i] = 1
        else:
            person[i] = 0

    #print(person)
    for i in range(n):
        if 1 & bit>>i:
            for x, y in statement[i]:
                #print(x, y)
                if person[x-1] == -1:
                    person[x-1] = y
                elif person[x-1] == y:
                    pass
                elif person[x-1] != y:
                    is_ok = False
    if is_ok:
        #print(person)
        ans = max(ans, person.count(1))
        #print("ans:", ans)
    #else:
        #print("no")
    #print("--------------------")
print(ans)
