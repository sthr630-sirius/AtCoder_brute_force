n = int(input())
is_product = False
for i in range(1, 10):
    if n%i == 0 and n//i <= 9:
        is_product = True
if is_product:
    print("Yes")
else:
    print("No")