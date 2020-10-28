# -*- coding: utf-8 -*-
"""
Created on Wed Oct 14 18:51:58 2020

@author: matam

1. Set in python - distinct elements 
2. Adding two sets 
3. difference b/w two sets 
4. methods in set 
5. frozen set 
6. how to declare empty set 

"""
a={1,2,3,4,5,6,1,2,3}
print(a)
#Distinct elements 
a.add(100)
print(a)
print(a.pop())
print(a.pop())
a.remove(6)
print(a)

b={3,4,5,7,8,9}

c=a.difference(b)
print(c)

c=b.difference(a)
print(c)

d=a.union(b)
print(d)

c= a&b
print(c)

c= a|b
print(c)
"""
c= frozenset({3,4,5,6,75,6,5,7,89})
print(c)
c.add(100)
"""

c={}
print(type(c))

c=set()
print(type(c))

b.clear()
print(b)


