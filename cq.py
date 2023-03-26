# -*- coding: utf-8 -*-
"""
Created on Tue Mar 14 15:42:53 2023


@author: Hannah
"""

class Empty(Exception):
  pass

class CircularQueue:
    """Implementation of a circular queue using a singly linked list."""
    
    class Node:
        """A node that holds an element of the queue."""
        def __init__(self, element, next_node=None):
            self.element = element
            self.next = next_node
    
    def __init__(self):
        """Create an empty queue."""
        self.tail = None  # pointer to the tail of the queue
        self.num_elements = 0  # the number of elements in the queue

    def __len__(self):
        """Return the number of elements in the queue."""
        return self.num_elements

    def is_empty(self):
        """Return True if the queue is empty."""
        return self.num_elements == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.
        
        Raise an IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        head = self.tail.next
        return head.element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e., FIFO).
        
        Raise an IndexError if the queue is empty.
        """
        if self.is_empty():
            raise IndexError("Queue is empty")
        old_head = self.tail.next
        if self.num_elements == 1:  # removing the only element
            self.tail = None  # queue becomes empty
        else:
            self.tail.next = old_head.next  # bypass the old head
        self.num_elements -= 1
        return old_head.element

    def enqueue(self, element):
        """Add an element to the back of the queue."""
        new_node = self.Node(element)
        if self.is_empty():
            new_node.next = new_node  # initialize circularly
        else:
            new_node.next = self.tail.next  # new node points to head
            self.tail.next = new_node  # old tail points to new node
        self.tail = new_node  # new node becomes the tail
        self.num_elements += 1

    def rotate(self):
        """Rotate the front element to the back of the queue."""
        if self.num_elements > 0:
            self.tail = self.tail.next  # old head becomes new tail