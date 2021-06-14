'''

Problem Statement

Kumar is back and this time he wants to make a list of all the groceries he needs to buy .He writes the list as
a text file in his computer and saves it and goes to sleep.However there is a problem here. Due to random
electrical fluctuations the computer’s memory gets shuffled and all the words in Kumar’s grocery list get
reversed . When he wakes up the next day he notices that some items in the changed list were also present
in the unchanged list For example let’s assume kumar stores the list as: abcd efgh hgfe Overnight the list
becomes: dcba hgfe efgh In this case the grocery items hgfe and efgh were both present in the second list
Given a list of N groceries you must report to kumar how many groceries were preserved after the list
undergoes modification due to the electrical fluctuation

Input Format

The first line contains a single integer N denoting the number of items in his grocery list The next N lines
contain a single string per line denoting an item in the list

Constraints

1<=N<=100000
Length of each string is atmost 20

Output Format

The output must consist of a single integer denoting how many items in the original list were preserved

'''

n=int(input())
groc1=[]
for i in range(n):
  groc1.append(input())
c=0
for i in groc1:
  if(i[::-1] in groc1):
    c+=1
print(c)
