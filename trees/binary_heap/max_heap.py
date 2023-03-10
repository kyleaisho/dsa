def build(items):
    n = len(items)
    for i in range(n // 2, -1, -1):
        max_heapify_down(items, i)
    return items


def max_heapify_up(heap, i):
    p_idx = parent_index(i)
    if heap[p_idx] < heap[i]:
        swap(heap, i, p_idx)
        max_heapify_up(heap, p_idx)


def delete_max(heap):
    return delete(heap, 0)


def delete(heap, i):
    if i >= len(heap):
        return

    swap(heap, i, -1)
    item = heap.pop()
    max_heapify_down(heap, i)
    return item


def max_heapify_down(heap, i):
    left = left_child_index(i, len(heap))
    right = right_child_index(i, len(heap))

    if heap[i] >= heap[left] and heap[i] >= heap[right]:
        return

    max_child = left if heap[left] >= heap[right] else right
    swap(heap, i, max_child)
    max_heapify_down(heap, max_child)


def swap(heap, i, j):
    tmp = heap[i]
    heap[i] = heap[j]
    heap[j] = tmp


def parent_index(i):
    p = (i - 1) // 2
    return p if i > 0 else i


def left_child_index(i, n):
    l = 2 * i + 1
    return l if l < n else i


def right_child_index(i, n):
    r = 2 * i + 2
    return r if r < n else i
