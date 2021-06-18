'''
Problem Statement

A prime number is a natural number greater than 1 and has exactly 2 divisors which are 1 and the number
itself.
You are given a prime number n, find any 2 prime numbers a and b such that a+b=n or state that no such pair
of primes exists.

Input Format

The input contains a single prime number n.

Constraints

(2≤n≤10^7)

Output Format

If there doesn't exist any 2 primes such that their summation is equal to n then print -1, 
otherwise print the 2 primes on a single line separated by a space the smaller number should preceed the larger number

'''
from math import sqrt
from itertools import combinations
def isprime(n):
    if(n<=1):
        return False
    if(n>=4 and (n%2==0 or n%3==0)):
        return False
    k=1
    a,b=6*k-1,6*k+1
    sqr=int(sqrt(n))
    while(a<= sqr or b<=sqr):
        if(n%a==0 or n%b==0):
            return False
        k+=1
        a, b = 6 * k - 1, 6 * k + 1
    return True
n=int(input())
l=[]
for i in range(2,n):
    if(isprime(i)==True):
        l.append(i)
c=list(combinations(l,2))
x=0
for i in c:
    if(sum(i)==n):
        x=i[0]
        break

if(x==0):
    print('-1')
else:
    print(x,n-x)
