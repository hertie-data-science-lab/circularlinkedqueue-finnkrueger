# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:48:01 2023

@author: Hannah
"""

from cq import CircularQueue

cq = CircularQueue()
print("Starting Size", len(cq) )
cq.enqueue("a")
cq.enqueue("b")
cq.enqueue("c")
print("Current Size", len(cq) )
print("Current Head", cq.first())
cq.rotate()
print("Current Head after rotating", cq.first())
