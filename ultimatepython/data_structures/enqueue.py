from collections import deque

def enqueue(queue, element):
    """
    Enqueues an element into the deque (queue).

    Parameters:
    queue (deque): The deque to which the element will be enqueued.
    element: The element to enqueue.

    Returns:
    None
    """
    queue.append(element)

def main():
    # Create a deque (queue)
    dq = deque()

    for i in range(1, 5):
        # Enqueue elements into the deque
        enqueue(dq, i)
        enqueue(dq, i * 2)

    # Iterate over the deque
    assert [el for el in dq] == [1, 2, 2, 3, 3, 4, 4, 8]

    # Dequeue elements from the deque (using it as a stack)
    assert dq.pop() == 8
    assert dq.pop() == 4

    # Dequeue elements from the deque (using it as a queue)
    assert dq.popleft() == 1
    assert dq.popleft() == 2

if __name__ == "__main__":
    main()
