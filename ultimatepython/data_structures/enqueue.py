from collections import deque


class Queue:
    def __init__(self):
        """
        Initializes an empty queue using a deque.
        """
        self.queue = deque()

    def enqueue(self, item):
        """
        Adds an item to the end of the queue (enqueue operation).
        In a deque, adding an element to the right side is done using `append()`.
        """
        self.queue.append(item)

    def dequeue(self):
        """
        Removes and returns the item from the front of the queue (dequeue operation).
        In a deque, removing an element from the left side is done using `popleft()`.
        """
        if not self.is_empty():
            return self.queue.popleft()
        else:
            raise IndexError("Queue is empty")

    def is_empty(self):
        """
        Checks if the queue is empty.
        """
        return len(self.queue) == 0

    def size(self):
        """
        Returns the size of the queue.
        """
        return len(self.queue)


def main():
    # Create a new queue
    my_queue = Queue()

    # Enqueue elements into the queue
    my_queue.enqueue(1)
    my_queue.enqueue(2)
    my_queue.enqueue(3)

    # Dequeue elements from the queue
    assert my_queue.dequeue() == 1
    assert my_queue.dequeue() == 2

    # Check if the queue is empty
    assert not my_queue.is_empty()

    # Get the size of the queue
    assert my_queue.size() == 1


if __name__ == "__main__":
    main()
