#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 23:06:21 2023

@author: prateekgoswami
"""

n = int(input("Enter N: "))
x = int(input("Enter a number(Enter -999 to stop): "))
count1 = 0
count2 = 0
while x != -999:
    if x % n == 0:
        count1 += 1
    else:
        count2 += 1

    x = int(input("Enter a number(Enter -999 to stop): "))

print("Number of integers divisible by n:", count1)
print("Number of integers not divisible by n:",  count2)