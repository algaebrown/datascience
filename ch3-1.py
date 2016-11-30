# -*- coding: utf-8 -*-
"""
Created on Wed Nov 30 15:11:43 2016
ch3-2 exercise
Finger exercise: Write a program that asks the user to enter an integer and
prints two integers, root and pwr, such that 0 < pwr < 6 and root**pwr is equal
to the integer entered by the user. If no such pair of integers exists, it should
print a message to that effect.
@author: Charl
"""
userInput = int(input('input an integer'))

integerpair=[]
for pwr in range(1,5):
    root = userInput**(1/pwr)
    if root%1==0:
        integerpair.append(pwr)
        integerpair.append(root)

if len(integerpair)==0:
    print("no such pair")
else: 
    print(integerpair)
