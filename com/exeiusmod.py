def heapify_up(heap, index):
    parent_index = (index - 1) // 2
    if parent_index >= 0 and heap[index] < heap[parent_index]:
        heap[index], heap[parent_index] = heap[parent_index], heap[index]
        heapify_up(heap, parent_index)

def insert(heap, item):
    heap.append(item)
    heapify_up(heap, len(heap) - 1)

# Example usage:
heap = []
insert(heap, 10)
insert(heap, 5)
insert(heap, 15)
insert(heap, 2)

print("Heap:", heap)
