#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec 25 23:55:52 2018
@author: toothlesswonder
"""

f = open("advent/puzzle_input_day5.txt", "r")
data = f.read()
f.close()


def check_reactivity(a,b):
    if a.lower() == b.lower() and a != b:
        reactive = True
    else:
        reactive = False
    return reactive


def destroy_reactive_units(polymer):
    # list of units to destroy
    destroy = []
    
    for i, char in enumerate(polymer):
        if i == len(polymer)-1 or i < 0:
            pass
        elif i in destroy:
            pass
        else:
            char2 = polymer[i+1]
            if check_reactivity(char, char2):
                destroy.extend((i, i+1))
            else:
                pass
        
    for i in sorted(destroy, reverse=True):
        del polymer[i]
    
    return polymer


''' part 2 '''

shortest_polymer = {}
    
for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
    print('removing', char, 'and', char.lower())
    polymer = list(data)
    polymer = list(filter(lambda a: a != char, polymer))
    polymer = list(filter(lambda a: a != char.lower(), polymer))
    
    more_to_destroy = True
    loop = 1
    
    while more_to_destroy == True:
        current_len = len(polymer)
        polymer = destroy_reactive_units(polymer)
        # print ('pass number %s: list is now %s long' % (loop, len(polymer)))
        loop += 1
        if current_len == len(polymer):
            more_to_destroy = False

    shortest_polymer[char] = len(polymer)
    print('list length is now', len(polymer))
    

min(shortest_polymer, key=shortest_polymer.get)
