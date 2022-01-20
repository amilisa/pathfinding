from turtle import distance
import pygame
import heapdict
import drawing_tools
from constants.sizes import CELL_SIZE, ROWS_NUMBER, COLUMNS_NUMBER
from constants.colors import *


def sort_by_distance(element,array):
    if element in array:
        array.remove(element)
        
    array.append(element)
    array.sort(key=lambda x: x.distance, reverse=False)
    return array

def sort_by_score(element,array):
    if element in array:
        array.remove(element)
        
    array.append(element)
    array.sort(key=lambda x: x.c_score, reverse=False)
    return array


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
        if current_node.cost == 1:
            current_node.draw_cell(grid_wrapper, CELL_SIZE, LIGHT_GREY)
        if current_node.cost == 2:
            current_node.draw_cell(grid_wrapper, CELL_SIZE, Weight1T)
        if current_node.cost == 3:
            current_node.draw_cell(grid_wrapper, CELL_SIZE, Weight2T)
        if current_node.cost == 5:
            current_node.draw_cell(grid_wrapper, CELL_SIZE, Weight3T)
        
    for node in nodes_list:
        if node is not goal_node:
            if node.cost == 1:
                node.draw_cell(grid_wrapper, CELL_SIZE, ORANGE)
            if node.cost == 2:
                node.draw_cell(grid_wrapper, CELL_SIZE, Weight1B)
            if node.cost == 3:
                node.draw_cell(grid_wrapper, CELL_SIZE, Weight2B)
            if node.cost == 5:
                node.draw_cell(grid_wrapper, CELL_SIZE, Weight3B)
    pygame.event.pump() 
            

    pygame.time.delay(5)
    drawing_tools.draw_grid(grid_wrapper, grid, ROWS_NUMBER, COLUMNS_NUMBER, CELL_SIZE, SGILIGHTGRAY) 


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

def depth_first_search(root_node, goal_node, grid, grid_wrapper):
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
            queue.insert(0,neighbor)
            neighbor.is_visited = True
            neighbor.previous = current_node

    return []


def dijkstra(root_node, goal_node, grid, grid_wrapper):
    root_node.distance = 0
    root_node.is_visited = True
    # priority_queue = heapdict.heapdict()
    # priority_queue[root_node] = root_node.distance
    
    queue = []
    queue = sort_by_distance(root_node,queue)

    while queue:
        # current_node = priority_queue.popitem()[0]
        current_node = queue.pop(0)
        
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
                # priority_queue[neighbor] = new_distance
                queue = sort_by_distance(neighbor,queue)
                neighbor.previous = current_node

    return []

def A_star(root_node, goal_node, grid, grid_wrapper):
    # calculating score
    end_x = goal_node.column_ind
    end_y = goal_node.row_ind
    
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            grid[i][j].score = ((end_x - grid[i][j].column_ind)**2 + (end_y-grid[i][j].row_ind)**2)**0.5
    
    
    root_node.distance = 0
    root_node.is_visited = True
    
    queue = []
    queue = sort_by_distance(root_node,queue)

    while queue:
        current_node = queue.pop(0)
        
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
                neighbor.c_score = new_distance + neighbor.score
                queue = sort_by_score(neighbor,queue)
                neighbor.previous = current_node

    return []


