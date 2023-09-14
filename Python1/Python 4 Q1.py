#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:28:19 2023

@author: prateekgoswami
"""

n= int(input("Enter any number: "))
i=1
if n<0 or n==0:
    print("Input is invalid")
else:
    while i<21:
        print(n,"x",i,"=", i*n)
        i= i+1
    