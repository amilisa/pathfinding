import pygame
import heapdict
import drawing_tools
from constants.sizes import CELL_SIZE, ROWS_NUMBER, COLUMNS_NUMBER
from constants.colors import *


def trace_path(root_node, goal_node):
    path = []
    current_node = goal_node
    while current_node is not root_node:
        path.append(current_node)
        current_node = current_node.previous
    path.reverse()
    return path


def visualise_steps(current_node, root_node, goal_node, nodes_list, grid_wrapper, grid):
    if current_node is not root_node:
        current_node.draw_cell(grid_wrapper, CELL_SIZE, LIGHT_GREY)

    for node in nodes_list:
        if node is not goal_node:
            node.draw_cell(grid_wrapper, CELL_SIZE, LIGHT_YELLOW)

    pygame.time.delay(5)
    drawing_tools.draw_grid(grid_wrapper, grid, ROWS_NUMBER, COLUMNS_NUMBER, CELL_SIZE, GREY)


def breadth_first_search(root_node, goal_node, grid, grid_wrapper):
    queue = [root_node]
    root_node.is_visited = True
    while queue:
        current_node = queue.pop(0)
        if current_node is goal_node:
            path = trace_path(root_node, goal_node)
            return path

        current_node.add_unvisited_neighbors(grid)
        neighbors_list = current_node.neighbors
        visualise_steps(current_node, root_node, goal_node, neighbors_list, grid_wrapper, grid)

        for neighbor in neighbors_list:
            queue.append(neighbor)
            neighbor.is_visited = True
            neighbor.previous = current_node

    return []


def dijkstra(root_node, goal_node, grid, grid_wrapper):
    root_node.distance = 0
    root_node.is_visited = True
    priority_queue = heapdict.heapdict()
    priority_queue[root_node] = root_node.distance

    while priority_queue:
        current_node = priority_queue.popitem()[0]
        current_node.is_visited = True
        if current_node is goal_node:
            path = trace_path(root_node, goal_node)
            return path

        current_node.add_unvisited_neighbors(grid)
        neighbors_list = current_node.neighbors
        visualise_steps(current_node, root_node, goal_node, neighbors_list, grid_wrapper, grid)

        for neighbor in neighbors_list:
            new_distance = current_node.distance + neighbor.cost
            if new_distance < neighbor.distance:
                neighbor.distance = new_distance
                priority_queue[neighbor] = new_distance
                neighbor.previous = current_node

    return []
