import itertools
import copy

n, m = map(int, input().split())
g = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    g[a].append(b)
    g[b].append(a)

ans = 0

for path in list(itertools.permutations(range(1, n))):
    #print('case')
    #print(path)
    g_temp = copy.deepcopy(g)
    is_visited = [False] * n
    now_p = 0
    is_visited[now_p] = True
    for next_p in path:
        #if next_p in g_temp[now_p] and not is_visited[next_p]:
        if next_p in g_temp[now_p]:
            #print(is_visited[next_p])
            #print("yes")
            #g_temp[now_p].remove(next_p)
            #g_temp[next_p].remove((now_p))
            now_p = next_p
            is_visited[now_p] = True
    #print("----ans---------")
    #print(g_temp)
    #print(is_visited)
    if all(is_visited):
        ans += 1

print(ans)
