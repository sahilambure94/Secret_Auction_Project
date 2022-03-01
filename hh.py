n = int(input())
# inp = list(map(int, input().split()))
inp = []
while len(inp) < n:
    inp = list(map(int, input().split()))
print(sorted(list(set(inp)))[-2])
