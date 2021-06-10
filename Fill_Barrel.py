'''
Problem Statement

You have n barrels lined up in a row, numbered from left to right from one. Initially, the i-th
barrel contains ai liters of water.
You can pour water from one barrel to another. In one act of pouring, you can choose two
different barrels x and y (the x-th barrel shouldn't be empty) and pour any possible amount of
water from barrel x to barrel y (possibly, all water). You may assume that barrels have infinite
capacity, so you can pour any amount of water in each of them.
Calculate the maximum possible difference between the maximum and the minimum amount
of water in the barrels, if you can pour water at most k times.

Input Format

The first line contains one integer t— the number of test cases.
The first line of each test case contains two integers n and k — the number of barrels and the
number of pourings you can make.
The second line contains n integers a1,a2,…,an , where ai is the initial amount of water the i-th
barrel has.
It's guaranteed that the total sum of n over test cases doesn't exceed

Constraints

(1≤t≤1000)
(1≤k
(0≤ai≤10^9)
2⋅(10^5).

Output Format

For each test case, print the maximum possible difference between the maximum and the
minimum amount of water in the barrels, if you can pour water at most k times

'''
t = int(input())
for i in range(t):
    n, k = map(int, input().split())
    lit = list(map(int, input().split()))
    lit.sort()
    for i in range(k):
        if(lit[-1]!=0 and lit[-2]!=0):
            res=lit[-1]+lit[-2]
            lit=lit[:-2]
            lit.append(res)
    if(k>0):
        print(lit[-1])
    else:
        print(lit[-1]-lit[0])
