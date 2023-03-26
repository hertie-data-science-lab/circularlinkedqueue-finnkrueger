# CircularLinkedList

Implement a queue as a Circular Linked List. Your CircularQueue should use an inner class ```Node```.
Your queue should keep track of its size.
Your queue should implement the following methods:

```first(self)```
returns the element that is currently at the head of the queue. Raises an exception if the queue is empty.

```dequeue(self)```
Removes the first element of the queue.

```dequeue(self)```
Adds an element to the back of the queue. Raises an exception if the queue is empty.

```def rotate(self):```
Rotate the queue: effectively transfer the item at the head of the list to the tail of the list

You may use the template provided, or start your own implementation from scratch.

This is a sample output from my test:

```Starting Size 0
Current Size 3
Current Head a
Current Head after rotating b
```
