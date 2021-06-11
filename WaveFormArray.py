'''
Problem Statement
Given a sorted array arr[] of distinct integers. Sort the array into a wave-like array and return it.
In other words, arrange the elements into a sequence such that a1 >= a2 <= a3 >= a4 <= a5.....
(considering the increasing lexicographical order).

Input Format

First line of input contains n-the size of array. Next line of input contains n integers-the
elements of array.

Constraints

1 ≤ n ≤ 10^6
0 ≤ Ai ≤10^7

Output Format

Print the array which should be sorted in wave like pattern.
'''

n=int(input())
arr = list(set(map(int,input().split())))
for i in range(0,n-1,2):
    arr[i], arr[i+1] = arr[i+1], arr[i]
print(*arr)
