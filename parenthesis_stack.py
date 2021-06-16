'''
Problem Statement

Given an expression string x. Examine whether the pairs and the orders of “{“,”}”,”(“,”)”,”“,”” are correct in exp.

Input Format

A single string s containing the parenthesis.

Constraints

1<=length of string<=1000

Output Format

Print "1" if brackets are balanced else print "0".


'''


class Stack:
  def __init__(self):
    self.s=[]  
  def pop_ele(self,c):
    if(self.s[-1]=='{' and c=='}'):
      self.s.pop()
      return 1
    elif(self.s[-1]=='[' and c==']'):
      self.s.pop()
      return 1
    elif(self.s[-1]=='(' and c==')'):
      self.s.pop()
      return 1
    else:
      return 0
  
  def push(self,ele):
    self.s.append(ele)
    
  def length(self):
    return len(self.s )
    
    
brac=list(input().strip())
s=Stack()
for i in brac:
  if(i=='{' or i=='[' or i=='('):
    s.push(i)
  else:
    if(s.pop_ele(i)):
      continue
    else:
      break
if(s.length()==0):
  print('1')
else:
  print('0')


#end
