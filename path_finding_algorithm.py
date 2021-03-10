def trace_path(root_node, goal_node):
    path = []
    current_node = goal_node.previous
    while current_node is not root_node:
        path.append(current_node)
        current_node = current_node.previous
    path.reverse()
    return path


def breadth_first_search(root_node, goal_node):
    queue = [root_node]
    root_node.observed = True
    while queue:
        current_node = queue.pop(0)
        if current_node is goal_node:
            path = trace_path(root_node, goal_node)
            return path
        for neighbor in current_node.neighbors:
            if not neighbor.observed:
                neighbor.observed = True
                queue.append(neighbor)
                if neighbor.previous is None:
                    neighbor.previous = current_node
                # neighbor.previous = current_node
    return []





