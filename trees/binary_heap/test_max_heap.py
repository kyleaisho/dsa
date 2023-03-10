from .max_heap import (
    delete_max,
    left_child_index,
    right_child_index,
    max_heapify_up,
    max_heapify_down,
    build,
    delete,
)


def test_left_child_index():
    assert left_child_index(0, 5) == 1
    assert left_child_index(1, 5) == 3
    assert left_child_index(2, 5) == 2


def test_right_child_index():
    assert right_child_index(0, 5) == 2
    assert right_child_index(1, 5) == 4
    assert right_child_index(2, 5) == 2


def test_max_heapify_up():
    items = [1, 2, 3, 4]
    max_heapify_up(items, 3)
    assert items[0] == 4
    assert items[3] == 2
    assert items[2] == 3

    max_heapify_up(items, 2)
    assert items[1] == 1
    assert items[2] == 3


def test_max_heapify_down():
    items = [1, 2, 3, 4]
    max_heapify_down(items, 0)
    assert items[2] == 1

    max_heapify_down(items, 1)
    assert items[1] == 4
    assert items[3] == 2


def test_build():
    items = [1, 2, 3, 4, 5, 6, 7, 21, 9, 45]
    build(items)
    assert items[0] == 45


def test_delete():
    items = [1, 2, 3]
    delete(items, 0)
    assert items[0] == 3
    assert items[1] == 2
    assert len(items) == 2

    items = build([1, 2, 3, 4, 5, 6, 7, 21, 9, 45])
    delete(items, 0)
    assert items[0] == 21
    assert items[-1] == 1


# def test_delete_max():
#     heap = build([1, 2, 3, 4, 5, 6, 7, 21, 9, 45])
#     sorted_items = [45, 21, 9, 7, 6, 5, 4, 3, 2, 1]

#     for item in sorted_items:
#         assert item == delete_max(heap)
