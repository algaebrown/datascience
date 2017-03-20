# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 13:05:54 2017

@author: Charl
"""

def fap(n):
    if n < 3:
        return(1)
    else:
        return(fap(n-1)+fap(n-2))
   
def find_fap(x,n):
        
    while x > fap(n):
        n = n+1
    return (n)

   
       