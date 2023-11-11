input_line = input()
target_list = []
use_possible_char = ["A", "C", "G", "T"]
ans = 0
for i in range(1, len(input_line)+1):
    for j in range(len(input_line)-i+1):
        target_list.append(input_line[j:j+i])

for s in target_list:
    is_ACGT = True
    for i in range(len(s)):
        if not s[i] in  use_possible_char:
            is_ACGT = False
    if is_ACGT:
        ans = max(ans, len(s))

print(ans)