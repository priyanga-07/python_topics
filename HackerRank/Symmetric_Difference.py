n = int(input())
arr = set(list(map(int, input().split()))) #remove space from the input
m=int(input())
arr_1=set(list(map(int, input().split())))
print(arr)
print(arr_1)
result=arr.symmetric_difference(arr_1) #eliminate same number from both the sets
#print line by line
for i in sorted(result):  #order by asc
    print(i)
# print(result)