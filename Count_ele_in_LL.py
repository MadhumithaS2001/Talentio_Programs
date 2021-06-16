'''

Problem Statement

Given a singly linked list and a key, count the number of occurrences of given key in the linked list.

Input Format

First line of input contains n the size of linked list. Next line of input contains n integers the elements of
linked list Next line of input contains x whose occurence is needed to be count.

Constraints

0 ≤ N ≤ 10^4

Output Format

Print the number of occurrences of given key in the linked list.

'''

class Node:
    def __init__(self,data,next):
        self.data=data
        self.next=next
class LL:
    def __init__(self):
        self.head=None
    def add_at_end(self,data):
        if (not self.head):
            self.head=Node(data,None)
            return
        curr=self.head
        while curr.next:
            curr=curr.next
        curr.next=Node(data,None)
    def countele(self,key):
        self.key=key
        curr = self.head
        count=0
        while curr.next:
            if(curr.data==self.key):
                count+=1
            curr=curr.next
        if(curr.data==self.key):
            count+=1
        return count
ll=LL()
n=int(input())
arr=list(map(int,input().split()))
for i in arr:
    ll.add_at_end(i)
key=int(input())
print(ll.countele(key))

#end Of Program 
