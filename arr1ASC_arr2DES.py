'''
Problem Statement

You are given with two arrays. Your task is to merge the array such that first array is in
ascending order and second one in descending order.

Input Format

First line contains two integer ‘n’ and ‘m’. ‘n’ denotes length of array 1 and ‘m’ of array 2.
Next line contains n space separated numbers and third line contains ‘m’ space separated
numbers

Constraints

1>=n<=100

Output Format

Print a single array in desired order

'''
n,m = map(int,input().split())
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr1.sort()
arr2.sort(reverse=True)
print(*(arr1+arr2))
