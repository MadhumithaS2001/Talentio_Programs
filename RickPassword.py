'''

Rick lost the password of his super locker. He remembers the number of digits N as well as the sum S

of all the digits of his password. He know that his password is the largest number of N digits that can be

made with given sum S. As he is busy doing his homework, help him retrieving his password.

Input Format:
Two space separated integers N and S.

Constraints:

1 ≤ N ≤ 10^4

0 ≤ S ≤ 10^4

Output Format:
Print the password in the form of string, else return "-1" in the form of string


Input:
3 29

Output:
-1

Input:
5 12

Output:
93000


'''

n,m=map(int,input().split())
if(9*n<m):
    print(-1)
else:
    for i in range(n):
        x=9
        if(m>=9):
            print(x,end='')
        else:
            x=m
            print(x,end='')
        m-=x
        
        
        
#end        
