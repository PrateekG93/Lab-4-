#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 23:24:30 2023

@author: prateekgoswami
"""
n= int(input("Enter a number: "))
x=0
y=1
z= 0
fib= 0
while x<n:
    fib= y+z
    y=z
    z= fib
    x= x+1
    print(fib)