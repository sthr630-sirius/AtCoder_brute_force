a, b, c, x, y = map(int, input().split())
upper_num_ab = max(2*(x+1), 2*(y+1))
ans = 10**16
for num_ab in range(0, upper_num_ab, 2):
    #print(num_ab)
    num_a = max(x - num_ab//2, 0)
    num_b = max(y - num_ab//2, 0)
    #print(num_a, num_b, num_ab)
    #print(a*num_a, b*num_b, c*num_ab, a*num_a+b*num_b+c*num_ab)
    #print("---------------------------")
    ans = min(ans, a*num_a+b*num_b+c*num_ab)
print(ans)

