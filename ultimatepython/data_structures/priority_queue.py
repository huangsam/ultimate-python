import heapq


def main():
    """
    Demonstrates the usage of the heapq module in Python.
    """

    # Step 1: Creating a Min Heap
    # Initialize a list with some elements
    heap = [3, 1, 4, 1, 5, 9, 2]

    # Convert the list into a min heap using heapq.heapify()
    heapq.heapify(heap)

    # Assert that the heap is in min heap order
    assert heap == [1, 1, 2, 3, 5, 9, 4]

    # Step 2: Pushing onto the Heap
    # Add a new element to the heap using heapq.heappush()
    heapq.heappush(heap, 0)

    # Assert that the heap is still in min heap order
    assert heap == [0, 1, 2, 1, 5, 9, 4, 3]

    # Step 3: Popping from the Heap
    # Remove and get the smallest element from the heap using heapq.heappop()
    min_element = heapq.heappop(heap)

    # Assert that the smallest element is 0
    assert min_element == 0

    # Assert that the heap is still in min heap order
    assert heap == [1, 1, 2, 3, 5, 9, 4]

    # Step 4: Heap Replacement
    # Replace the smallest element with a new value using heapq.heapreplace()
    heapq.heapreplace(heap, 6)

    # Assert that the smallest element is now 1
    assert heap[0] == 1

    # Assert that the heap is still in min heap order
    assert heap == [1, 3, 2, 6, 5, 9, 4]


if __name__ == "__main__":
    main()


# Creating a Min Heap (heapify):

# Use heapq.heapify() to convert a regular list into a min heap.
# This ensures that the smallest element is at the root of the heap.
# Pushing onto the Heap (heappush):

# Add a new element to the heap using heapq.heappush().
# The function maintains the heap property, ensuring the smallest element remains at the root.
# Popping from the Heap (heappop):

# Remove and retrieve the smallest element from the heap using heapq.heappop().
# The heap is automatically adjusted to maintain the heap property.
# Heap Replacement (heapreplace):

# Replace the smallest element with a new value using heapq.heapreplace().
# This operation efficiently maintains the heap property by removing and adding elements.
# By following these steps, you can effectively create, modify, and work with min heaps using the heapq module in Python.
