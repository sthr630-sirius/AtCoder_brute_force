a, b, k = map(int, input().split())
ans_list = []
for i in range(a+1, 0, -1):
    if a%i == 0 and b%i == 0:
        ans_list.append(i)
print(ans_list[k-1])