from collections import Counter
k=int(input())
n=list(map(int, input().split()))
counts =Counter(n)

for n, count in counts.items():
    if count == 1:
        print(n)
        break