
#!/usr/bin/python3

from collections import deque

def canUnlockAll(boxes):
    """
    Check if all the boxes can be opened.

    Args:
    boxes (List[List[int]]): A list of lists where each sublist represents a box and contains keys to other boxes.

    Returns:
    bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = set()
    queue = deque([0])  # Start with the first box (box 0)
    visited.add(0)

    while queue:
        current_box = queue.popleft()

    #!/usr/bin/python3

canUnlockAll = __import__('0-lockboxes').canUnlockAll

boxes = [[1], [2], [3], [4], []]
print(canUnlockAll(boxes))

boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
print(canUnlockAll(boxes))

boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
print(canUnlockAll(boxes))
