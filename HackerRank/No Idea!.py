input()
n = list(map(int, input().split()))

set_a = set(map(int, input().split()))
set_b = set(map(int, input().split()))

# Alternative (longer version)
# happiness_count = 0 

# for i in n:
#     if i in set_a:
#         happiness_count += 1
#     elif i in set_b:
#         happiness_count -= 1

# print(happiness_count)

# Shorter version
print(sum((i in set_a) - (i in set_b) for i in n))