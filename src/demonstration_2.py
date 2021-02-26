"""
Given a reference to the head node of a singly-linked list, write a function
that reverses the linked list in place. The function should return the new head
of the reversed list.

In order to do this in O(1) space (in-place), you cannot make a new list, you
need to use the existing nodes.

In order to do this in O(n) time, you should only have to traverse the list
once.

*Note: If you get stuck, try drawing a picture of a small linked list and
running your function by hand. Does it actually work? Also, don't forget to
consider edge cases (like a list with only 1 or 0 elements).*
"""

def print_list(start_node):
    curr_node = start_node
    while curr_node is not None:
        # print the node value
        print(curr_node.value)
        # move onto the next one
        curr_node = curr_node.next
        
class LinkedListNode():
    def __init__(self, value):
        self.value = value
        self.next  = None

def reverse(head_of_list):
    # need previous node, current node, next node
    curr_node = head_of_list
    prev_node = None
    next_node = head_of_list.next
    
    while curr_node is not None:
        # we need to swap the pointers around
        next_node = curr_node.next
        # reverse the "next" pointer of the current_node
        curr_node.next = prev_node
        
        # update all pointers, to move onto the next node
        prev_node = curr_node
        curr_node = next_node
    
    return prev_node



x = LinkedListNode('X')
y = LinkedListNode('Y')
z = LinkedListNode('Z')

x.next = y
y.next = z

head = x
print("original")
print_list(head)

print("reversed list")
head = reverse(head)
print_list(head)