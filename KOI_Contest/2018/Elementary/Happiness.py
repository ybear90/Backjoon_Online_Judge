N = int(input())
alist = []

while N < 2 or N > 1000:
    N = int(input())

happ = input().split()

while len(happ) != N:
    happ = input().split()

alist = list(map(int, happ))

# Find max, min

max_value = max(alist)
min_value = min(alist)

print(max_value - min_value)
