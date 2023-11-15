import itertools

n = int(input())
seq =  list(itertools.permutations([i for i in range(1, n+1)]))

a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

a_idx = seq.index(a)
b_idx = seq.index(b)

print(abs(a_idx-b_idx))