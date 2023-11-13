n = int(input())
s = input()
ans = 0

for i in range(1000):
    lucky_num = s
    pass_word = "00" + str(i)
    pass_word = pass_word[-3:]
    a = pass_word[0]
    b = pass_word[1]
    c = pass_word[2]
    if a in lucky_num:
        idx_a = lucky_num.index(a)
    else:
        continue
    if b in lucky_num[idx_a+1:]:
        idx_b = lucky_num[idx_a+1:].index(b)
    else:
        continue
    if c in lucky_num[idx_a+idx_b+2:]:
        ans += 1
    else:
        continue
print(ans)