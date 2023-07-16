import sys

l_len = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))
target = int(sys.stdin.readline())
total = 0

l.sort()
first = 0
second = l_len-1
while first != second:
    s = l[first]+l[second]
    if s == target:
        total += 1
        second -= 1
    elif s < target:
        first += 1
    else:
        second -= 1
print(total)