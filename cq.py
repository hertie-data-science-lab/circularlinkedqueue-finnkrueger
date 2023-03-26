# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:53 2023


@author: Hannah
"""

class Empty(Exception):
  pass


class CircularQueue:
    """Queue implementation using circularly linked list for storage"""""
    
    class _Node:
        __slots__ = '_element', '_next'
        
        def __init__(self, element, nxt):
            self._element = element
            self._next = nxt

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
       pass

    def dequeue(self):
        pass
    
    def enqueue(self, e):
        pass
    
    def rotate(self):
       pass