#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 15:43:50 2023

@author: prateekgoswami
"""

n= int(input("Enter a positive number: "))
i=1
fact=1 
while i<=n:
    fact= fact*i
    i=i+1
print(fact)