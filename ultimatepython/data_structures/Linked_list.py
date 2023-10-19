'''

A linked list is a data structure used for organizing and storing a collection
of elements, where each element (node) contains a value and a reference to
the next element in the sequence. Linked lists are particularly useful when
you need dynamic sizing and efficient insertions and deletions at the cost
of slower random access. In this tutorial, we'll create a basic linked list
and demonstrate how to append elements and display its contents.

'''


# Node class to represent individual elements of the linked list
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# LinkedList class to manage the linked list


class LinkedList:
    def __init__(self):
        self.head = None

    # Method to append a new element to the end of the linked list
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    # Method to display the linked list
    def display(self):
        current = self.head
        result = ""
        while current:
            result += str(current.data) + " -> "
            current = current.next
        result += "None"
        return result


if __name__ == "__main__":
    # Create a linked list
    linked_list = LinkedList()

    # Append elements to the linked list
    linked_list.append(1)
    linked_list.append(2)
    linked_list.append(3)
    linked_list.append(4)

    # Display the linked list
    linked_list.display()

