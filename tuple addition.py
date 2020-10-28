# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 15:33:30 2020

@author: matam
"""

a=(1,2,3,4,5)
b=(6,7,8,9,10)
print(a+b)
c=a*3
print(c)
for i in a:
    print(i)
    
for i in a:
    print(i*3)
"""
negative indexing
"""
print(a[-3])

print(a[:])
print(a[2:])


for i in ('kiran','adarsh','siddharth','jashvi'):
    print(i)
    
d=(1,2,3,4,1,2,3)
print(d)
#print(d.count['4'])


my_tuple=('a','b','c','d','a')
print(my_tuple)
print(my_tuple.index('a'))
print('c' in my_tuple)
print(len(a))
print(min(a))
