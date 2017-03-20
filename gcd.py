# -*- coding: utf-8 -*-
"""
Created on Wed Feb 22 17:29:37 2017

@author: Charl
"""

def gcd(big,small):
    if big % small == 0:
        return(small)
    else:
        gcd (small, big % small)
        