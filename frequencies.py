"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""
from collections import Counter

def frequencies(items):

 frequencies={} 
 for item in items:
    frequencies[item] = frequencies.get(item, 0) + 1
 
 for key, value in frequencies.items():
    print(key, value)
 
 return frequencies