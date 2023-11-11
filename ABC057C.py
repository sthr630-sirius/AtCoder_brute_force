import math
n = int(input())
limit_loop = int(math.sqrt(n))
ans = 12
for i in range(1, limit_loop+1):
    if n%i == 0:
        a = len(str(i))
        b = len(str(n//i))
        ans = min(ans, max(a, b))

print(ans)