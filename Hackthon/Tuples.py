if __name__ == '__main__':#WIt works version 2
    n = int(input())
    integer_list = map(int, input().split())
    t = tuple(integer_list)
    print(hash(t))

# To put it simply, hash(t) takes an
# object t and turns it into a single,
# unique code number.Think of it like a
# barcode or a digital fingerprint for data.
# 1. What does Python use it for?Python
# uses this number to find things instantly.
# Without hash(t): Python would have to look t
# hrough a dictionary or set line-by-line to find a key. T
# his is slow.With hash(t):
# Python looks at the code number and knows exactly
# where that data is stored in memory. T
# his happens instantly, even if you have millions of items.