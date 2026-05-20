#Union from both sets
n=int(input())
eng=set(input().split())
m=int(input())
fre=set(input().split())
at_one=eng.union(fre)
print(len(at_one))

#INtersection from both sets
n=int(input())
eng=set(input().split())
m=int(input())
fre=set(input().split())
at_one=eng & fre
print(len(at_one))

#Difference from both sets
n=int(input())
eng=set(input().split())
m=int(input())
fre=set(input().split())
at_one=eng - fre
print(len(at_one))

# Students of District College have subscriptions to English
# and French newspapers. Some students have subscribed to
# English only, some have subscribed to French only, and some
# have subscribed to both newspapers.
# You are given two sets of student roll numbers. One
# set has subscribed to the English newspaper, and one set
# has subscribed to the French newspaper. Your task is to
# find the total number of students who have subscribed to either
# the English or the French newspaper but not both.
#symmetric difference
n=int(input())
eng=set(input().split())
m=int(input())
fre=set(input().split())
at_one=eng ^ fre
print(len(at_one))