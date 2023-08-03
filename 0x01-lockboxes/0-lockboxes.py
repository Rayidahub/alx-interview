def canUnlockAll(boxes):
    if not boxes:
        return False

    num_boxes = len(boxes)
    visited = set()
    
    def dfs(box):
        if box in visited:
            return
        visited.add(box)

        # Check if all boxes are unlocked
        if len(visited) == num_boxes:
            return True

        # Explore keys of the current box recursively
        for key in boxes[box]:
            if 0 <= key < num_boxes:
                dfs(key)

    dfs(0)  # Start DFS from the first box (box 0)
    return len(visited) == num_boxes

# Example usage:
boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # Output: True

boxes = [[1, 2], [3], [4], [], []]
print(canUnlockAll(boxes))  # Output: False
