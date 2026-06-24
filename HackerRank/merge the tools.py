def merge_the_tools(string, k):
    # your code goes here
    u = ""
    for index,s in enumerate(string):
        if index%k==0 and index!=0:
            print(u)
            u=""
        if s not in u:
            u = u+s
    print(u)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)