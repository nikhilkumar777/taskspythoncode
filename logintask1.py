# -*- coding: utf-8 -*-
"""
Created on Thu Oct 22 17:28:40 2020

@author: user
"""
class Stack:
    def __init__(self):
        self.items = []
 
    def is_empty(self):
        return self.items == []
 
    def push(self, data):
        self.items.append(data)
 
    def pop(self):
        return self.items.pop()
 
 
s = Stack()
exp = input('Please enter the expression: ')
 
for c in exp:
    if c == '(':
        s.push(1)
    elif c == ')':
        if s.is_empty():
            bal = False
            break
        s.pop()
else:
    if s.is_empty():
        bal = True
    else:
        bal = False
 
if bal:
    print('syntax is correctly parenthesized.')
else:
    print('syntax is not correctly parenthesized.')
    
if bal == True:
    stack=[]
    z=0
    for i in exp:
        if i == '(':
            stack.append(i)
        elif i == ')':
           stack.append(i)
        
        else:
            stack.append(i)
        z=z+1
        if z==3:
            l=i
        if z==5:
            m=i
        if z==10:
            n=i        
        if z==12:
            o=i
        if z==19:
            p=i
        if z==21:
            q=i           
        if z==26:
            r=i            
        if z==28:
            s=i            
            
        if (z==24) :
            dc=i
            if dc in '&' :
                ad="and"
            else:
                ad="or"
        if (z==7) :
            f=i
            if f in '&' :
                fd="and"
            else:
                fd="or"
                
        if z==15:
            ec=i
            if ec == '|':
                ed="or"
            else:
                ed="and"
    print("{\n" '"query":{ \n "'+ed+'":[\n  {')
    print('   "' +fd+ '":{ \n' '    "'+l+'":'+m+',\n' '    "'+n+'":'+o+',\n' "   } \n  },")
    print("  {\n" '   "' +ad+ '":{ \n' '    "'+p+'":'+q+',\n' '    "'+r+'":'+s+',\n' "    } \n   }\n  ]\n }\n}")

            
else:
    print("syntax invalid")

