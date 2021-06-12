'''
Problem Statement
You are given with an array of numbers, Your task is to print the difference of indices of largest
and smallest number. All number are unique.
Input Format
First line contains a number ‘n’. Then next line contains n space separated numbers.
Constraints
1<=n<=100 1<=elements in array<=1000
Output Format
Print the difference of indices of largest and smallest array
'''
n = int(input())
arr = list(map(int, input().split()))
print(arr.index(max(arr))-arr.index(min(arr)))
