#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  8 14:54:07 2023

@author: prateekgoswami
"""

N= int(input("Enter a number: "))
Sum= 0
while N>0:
    Sum= Sum + (N%10) 
    N= N//10
print(Sum)