"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):

 frequencies={}

 list = [str(n) for n in items ]

 for i in list:
    if i in frequencies:
     frequencies[i] += 1
    else:
     frequencies[i]=1

 return frequencies