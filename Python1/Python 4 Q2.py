#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:46:12 2023

@author: prateekgoswami
"""
#Take 3 variables
X= int(input("Enter X: "))
Y= int(input("Enter Y: "))
N = int(input("Enter N: "))
while X<Y: #Work till X is less than Y
    X= X+1
    if X%N==0:   #check if X is divisible by N
        print(X)
