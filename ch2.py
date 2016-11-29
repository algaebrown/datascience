# -*- coding: utf-8 -*-
"""
Created on Tue Nov 29 23:12:12 2016
Chap 2 finger exercise: 
Write a program that asks the user to input 10 integers, and
then prints the largest odd number that was entered. If no odd number was
entered, it should print a message to that effect.

@author: Charl
"""

#ask the user to input 10 integers, and save the input number if its odd and larger than previous ones
save = 0
for i in range(1,10):
    integer = int(input('enter an integer:'))
    if (integer%2 == 1)and(integer > save):
        save = integer

#now check if there is no odd input
if save == 0:
    print('no odd input')
else:
    print (save)
        
    
