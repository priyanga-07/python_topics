# Given the participants' score sheet
# for your University Sports Day, you
# are required to find the runner-up score.
# You are given  scores. Store them in a list
# and find the score of the runner-up.
# Input Format
# The first line contains . The second
# line contains an array   of  integers each
# separated by a space.
# Sample Input 0
# 5
# 2 3 6 6 5
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    unique_numbers = list(set(arr)) # Removes duplicates
    unique_numbers.sort()
    print(unique_numbers[-2])
