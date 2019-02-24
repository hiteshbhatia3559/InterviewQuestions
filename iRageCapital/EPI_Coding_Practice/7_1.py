# 7.1

# Write a program that takes two lists, assumed to be sorted, and returns their merge. The only field
# your program can change in a node is its next field.


class ListNode:
    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node


def search_list(l, key):
    while l and l.data != key:
        l = l.next
    return l


def insert_after(node, new_node):
    new_node.next = node.next
    node.next = new_node


def delete_after(node):
    node.next = node.next.next


l1 = ListNode(1)

def merged_two_sorted_lists(l1,l2):
