#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 10:30:43 2024

@author: wezi
"""

import pandas as pd

# Load up amino acid dictionary; 22 amino acids including Sec and Pyl
aadict = pd.read_csv("aadict.txt", sep = "\t")
peptide_digits = list(aadict.iloc[:,2])

# Function for converting numbers to different bases
def numberToBase(n, b):
    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]

# Epitopes presented by MHC are 8 to 18aa long.
#
# If you want an 8aa string of alanine, then you should provide the function
# with 54875873536 (ie. 22^8) which gives you 100000000 in base 22, and you can
# ignore the first digit to call for a string of eight zeroes. Work up from
# there, and for a 17aa string of pyrrolysine you would ask for
# 32064977213018365645815807 (ie. 22^19 - 1)


for i in range(22**8, 22**19-1):
    base22number = numberToBase(i, 22)
    digitcall = base22number[1:len(base22number)]
    
    peptide = ""

    for digit in digitcall:
        letter = peptide_digits[digit]
        peptide = peptide + letter
    
    print(peptide)
