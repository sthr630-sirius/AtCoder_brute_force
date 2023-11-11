n = int(input())
input_line = input()
ans = 0
for i in range(n-2):
    if input_line[i:i+3] == "ABC":
        ans += 1
print(ans)