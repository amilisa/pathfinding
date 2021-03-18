import pygame
from constants.sizes import CELL_SIZE
from constants.colors import *


def trace_path(root_node, goal_node):
    path = []
    current_node = goal_node
    while current_node is not root_node:
        path.append(current_node)
        current_node = current_node.previous
    path.reverse()
    return path


def visualise_steps(current_node, root_node, goal_node, array, grid_wrapper):
    if current_node is not root_node:
        current_node.draw_cell(grid_wrapper, CELL_SIZE, LIGHT_GREY)

    for node in array:
        if node is not goal_node:
            node.draw_cell(grid_wrapper, CELL_SIZE, LIGHT_YELLOW)
    pygame.display.update()


def breadth_first_search(root_node, goal_node, grid, grid_wrapper):
    queue = [root_node]
    root_node.is_observed = True
    while queue:
        current_node = queue.pop(0)
        if current_node is goal_node:
            path = trace_path(root_node, goal_node)
            return path

        current_node.add_neighbors(grid)
        for neighbor in current_node.neighbors:
            if not neighbor.is_observed:
                neighbor.is_observed = True
                queue.append(neighbor)
                neighbor.previous = current_node

        visualise_steps(current_node, root_node, goal_node, queue, grid_wrapper)

    return []





