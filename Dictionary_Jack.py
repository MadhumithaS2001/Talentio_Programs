'''

Problem Statement

Jack is bored in english class and decides to play a game with you. He will ask you Q questions and in each
question he will give you a string S Such that it has length at most 500. You have to tell him if the string can
be partitioned into two substrings s1 and s2 such that s1 is present in the dictionary s2 is present in the
dictionary s1+s2 is equal to S Note that s1 could be equal to s2. They need not be distinct strings. The list of
words in the dictionary will be given to you initially and using this answer Jack's questions.

Input Format

The first line contains a single integer N, denoting the number of strings in the dictionary The next N lines
contains a single string each denoting the words in the dictionary The next line contains a single integer Q :
the number of questions you will be asked The next Q line contains a single string each which will be given
to you

Constraints

1<=n<=100

Output Format

Your output must consist of Q lines , each of which you must answer with “Yes” if the string can be
partitioned into two strings s1 and s2 as given in the problem statement Or “No” if the string cannot be
partitioned

'''

n = int(input())
dictword = {}
for i in range(n):
    x = input()
    dictword[x] = len(x)
print(dictword)
lenset=list(set(list(dictword.values())))
q = int(input())
for j in range(q):
    s = input()
    s1 = len(s)
    f = 1
    while (len(s) and f == 1):
        for i in lenset:
            if (i <= len(s) and s[:i] in dictword):
                f = 1
                s = s[i:]
            elif (i > len(s)):
                f = 0
                continue
        if (len(s) == s1):
            f = 0

    if (f == 1):
        print("Yes")
    else:
        print("No")
