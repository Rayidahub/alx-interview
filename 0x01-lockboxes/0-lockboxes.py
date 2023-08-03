
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

        # Check if all boxes are unlocked
        if len(visited) == num_boxes:
            return True

        # Add keys of the current box to the queue if not visited
        for key in boxes[current_box]:
            if key not in visited and 0 <= key < num_boxes:
                queue.append(key)
                visited.add(key)

    return len(visited) == num_boxes

if __name__ == "__main__":
    # Example usage:
    boxes1 = [[1], [2], [3], []]
    print(canUnlockAll(boxes1))  # Output: True

    boxes2 = [[1, 2], [3], [4], [], []]
    print(canUnlockAll(boxes2))  # Output: False
