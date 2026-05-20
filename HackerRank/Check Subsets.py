for each in range(int(input())):
        set1_length = int(input())
        set1 = set(map(int, input().split()))
        set2_length = int(input())
        set2 = set(map(int,input().split()))

        print(set1==set1.intersection(set2))
