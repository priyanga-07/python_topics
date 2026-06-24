!pip install collections
from collections import Counter


number_of_shoes = int(input())
shoe_size = list(map(int, input().split()))
number_of_customer = int(input())
shoe_size_dict = Counter(shoe_size)
total = 0
for n in range(number_of_customer):
    shoe_size_price = list(map(int, input().split()))
    if shoe_size_price[0] in shoe_size_dict and  shoe_size_dict[shoe_size_price[0]]> 0:
        shoe_size_dict[shoe_size_price[0]] -= 1
        total += shoe_size_price[1]
print(total)