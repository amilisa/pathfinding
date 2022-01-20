import random
import drawing_tools
from constants.sizes import CELL_SIZE, ROWS_NUMBER, COLUMNS_NUMBER
from constants.colors import *
import pygame


def surrounding_cells(rand_wall, grid):
    s_cells = 0
    if grid[rand_wall[0] - 1][rand_wall[1]].is_active == True:
        s_cells += 1
    if grid[rand_wall[0] + 1][rand_wall[1]].is_active == True:
        s_cells += 1
    if grid[rand_wall[0]][rand_wall[1] - 1].is_active == True:
        s_cells += 1
    if grid[rand_wall[0]][rand_wall[1] + 1].is_active == True:
        s_cells += 1

    return s_cells


def draw_white(cell, grid, grid_wrapper):
    # paint it white 
    cell.draw_cell(grid_wrapper, CELL_SIZE, WHITE)
    pygame.time.delay(5)
    drawing_tools.draw_grid(grid_wrapper, grid, ROWS_NUMBER, COLUMNS_NUMBER, CELL_SIZE, SGILIGHTGRAY)
    pygame.event.pump()


def prims_maze(maze_start, grid, grid_wrapper):
    random.seed(1634)
    starting_width = maze_start.column_ind
    starting_height = maze_start.row_ind

    height = len(grid)
    width = len(grid[0])

    # paint everything black
    for i in range(0, height):
        for j in range(0, width):
            drawing_tools.draw_obstacle(i, j, grid_wrapper, grid, CELL_SIZE, IVORYBLACK)

    # paint it white 

    if starting_height == 0:
        starting_height += 1
    if starting_height == height - 1:
        starting_height -= 1
    if starting_width == 0:
        starting_width += 1
    if starting_width == width - 1:
        starting_width -= 1

    maze_start = grid[starting_height][starting_width]

    cell = maze_start
    draw_white(cell, grid, grid_wrapper)
    grid[starting_width][starting_height].is_active = True

    # Mark it as cell and add surrounding walls to the list
    # Denote walls in maze
    grid[starting_height][starting_width].is_active = True
    walls = []
    walls.append([starting_height - 1, starting_width])
    grid[starting_height - 1][starting_width].is_active = False
    walls.append([starting_height, starting_width - 1])
    grid[starting_height][starting_width - 1].is_active = False
    walls.append([starting_height, starting_width + 1])
    grid[starting_height][starting_width + 1].is_active = False
    walls.append([starting_height + 1, starting_width])
    grid[starting_height + 1][starting_width].is_active = False

    while walls:
        # Pick a random wall
        rand_wall = walls[int(random.random() * len(walls)) - 1]
        # print(rand_wall,"rand_wall")
        # print(len(grid),len(grid[0]),"grid_shape")

        # Check if it is a left wall
        if rand_wall[1] != 0 and rand_wall[1] != width - 1:
            if grid[rand_wall[0]][rand_wall[1] - 1].is_visited == False and grid[rand_wall[0]][
                rand_wall[1] + 1].is_active == True:  #
                # Find the number of surrounding cells
                s_cells = surrounding_cells(rand_wall, grid)

                if s_cells < 2:
                    # Denote the new path
                    grid[rand_wall[0]][rand_wall[1]].is_active = True  #
                    grid[rand_wall[0]][rand_wall[1]].is_visited = True  #

                    cell = grid[rand_wall[0]][rand_wall[1]]
                    draw_white(cell, grid, grid_wrapper)

                    # Mark the new walls
                    # Upper cell
                    if rand_wall[0] != 0:
                        if grid[rand_wall[0] - 1][rand_wall[1]].is_active != True or grid[rand_wall[0] - 1][
                            rand_wall[1]].is_visited == False:  #
                            grid[rand_wall[0] - 1][rand_wall[1]].is_active = False  #
                            grid[rand_wall[0] - 1][rand_wall[1]].is_visited = True  #
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Bottom cell
                    if rand_wall[0] != height - 1:
                        if grid[rand_wall[0] + 1][rand_wall[1]].is_active != True or grid[rand_wall[0] + 1][
                            rand_wall[1]].is_visited == False:  #
                            grid[rand_wall[0] + 1][rand_wall[1]].is_active = False  #
                            grid[rand_wall[0] + 1][rand_wall[1]].is_visited = True  #
                        if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                            walls.append([rand_wall[0] + 1, rand_wall[1]])

                    # Leftmost cell
                    if rand_wall[1] != 0:
                        if grid[rand_wall[0]][rand_wall[1] - 1].is_active != True or grid[rand_wall[0]][
                            rand_wall[1] - 1].is_visited == False:  #
                            grid[rand_wall[0]][rand_wall[1] - 1].is_active = False  #
                            grid[rand_wall[0]][rand_wall[1] - 1].is_visited = True  #
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Check if it is an upper wall
        if rand_wall[0] != 0 and rand_wall[0] != height - 1:
            if grid[rand_wall[0] - 1][rand_wall[1]].is_visited == False and grid[rand_wall[0] + 1][
                rand_wall[1]].is_active == True:

                s_cells = surrounding_cells(rand_wall, grid)
                if s_cells < 2:
                    # Denote the new path
                    grid[rand_wall[0]][rand_wall[1]].is_active = True
                    grid[rand_wall[0]][rand_wall[1]].is_visited = True

                    cell = grid[rand_wall[0]][rand_wall[1]]
                    draw_white(cell, grid, grid_wrapper)

                    # Mark the new walls
                    # Upper cell
                    if rand_wall[0] != 0:
                        if grid[rand_wall[0] - 1][rand_wall[1]].is_active == False or grid[rand_wall[0] - 1][
                            rand_wall[1]].is_visited == False:
                            grid[rand_wall[0] - 1][rand_wall[1]].is_active = False
                            grid[rand_wall[0] - 1][rand_wall[1]].is_visited = True
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                    # Leftmost cell
                    if rand_wall[1] != 0:
                        if grid[rand_wall[0]][rand_wall[1] - 1].is_active == False or grid[rand_wall[0]][
                            rand_wall[1] - 1].is_visited == False:
                            grid[rand_wall[0]][rand_wall[1] - 1].is_active = False
                            grid[rand_wall[0]][rand_wall[1] - 1].is_visited = True
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])

                    # Rightmost cell
                    if rand_wall[1] != width - 1:
                        if grid[rand_wall[0]][rand_wall[1] + 1].is_active == False or grid[rand_wall[0]][
                            rand_wall[1] + 1].is_visited == False:
                            grid[rand_wall[0]][rand_wall[1] + 1].is_active = False
                            grid[rand_wall[0]][rand_wall[1] + 1].is_visited = True
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Check the bottom wall
        if rand_wall[0] != height - 1:
            if grid[rand_wall[0] + 1][rand_wall[1]].is_visited == False and grid[rand_wall[0] - 1][
                rand_wall[1]].is_active == True:

                s_cells = surrounding_cells(rand_wall, grid)
                if s_cells < 2:
                    # Denote the new path
                    grid[rand_wall[0]][rand_wall[1]].is_active = True
                    grid[rand_wall[0]][rand_wall[1]].is_visited = True

                    cell = grid[rand_wall[0]][rand_wall[1]]
                    draw_white(cell, grid, grid_wrapper)

                    # Mark the new walls
                    if rand_wall[0] != height - 1:
                        if grid[rand_wall[0] + 1][rand_wall[1]].is_active == False or grid[rand_wall[0] + 1][
                            rand_wall[1]].is_visited == False:
                            grid[rand_wall[0] + 1][rand_wall[1]].is_active = False
                            grid[rand_wall[0] + 1][rand_wall[1]].is_visited = True
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[1] != 0:
                        if grid[rand_wall[0]][rand_wall[1] - 1].is_active == False or grid[rand_wall[0]][
                            rand_wall[1] - 1].is_visited == False:
                            grid[rand_wall[0]][rand_wall[1] - 1].is_active = False
                            grid[rand_wall[0]][rand_wall[1] - 1].is_visited = True
                        if [rand_wall[0], rand_wall[1] - 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] - 1])
                    if rand_wall[1] != width - 1:
                        if grid[rand_wall[0]][rand_wall[1] + 1].is_active == False or grid[rand_wall[0]][
                            rand_wall[1] + 1].is_visited == False:
                            grid[rand_wall[0]][rand_wall[1] + 1].is_active = False
                            grid[rand_wall[0]][rand_wall[1] + 1].is_visited = True
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Check the right wall
        if rand_wall[1] != width - 1:
            if (grid[rand_wall[0]][rand_wall[1] + 1].is_visited == False and grid[rand_wall[0]][
                rand_wall[1] - 1].is_active == True):

                s_cells = surrounding_cells(rand_wall, grid)
                if s_cells < 2:
                    # Denote the new path
                    grid[rand_wall[0]][rand_wall[1]].is_active = True
                    grid[rand_wall[0]][rand_wall[1]].is_visited = True

                    cell = grid[rand_wall[0]][rand_wall[1]]
                    draw_white(cell, grid, grid_wrapper)

                    # Mark the new walls
                    if rand_wall[1] != width - 1:
                        if grid[rand_wall[0]][rand_wall[1] + 1].is_active == False or grid[rand_wall[0]][
                            rand_wall[1] + 1].is_visited == False:
                            grid[rand_wall[0]][rand_wall[1] + 1].is_active = False
                            grid[rand_wall[0]][rand_wall[1] + 1].is_visited = True
                        if [rand_wall[0], rand_wall[1] + 1] not in walls:
                            walls.append([rand_wall[0], rand_wall[1] + 1])
                    if rand_wall[0] != height - 1:
                        if grid[rand_wall[0] + 1][rand_wall[1]].is_active == False or grid[rand_wall[0] + 1][
                            rand_wall[1]].is_visited == False:
                            grid[rand_wall[0] + 1][rand_wall[1]].is_active = False
                            grid[rand_wall[0] + 1][rand_wall[1]].is_visited = True
                        if [rand_wall[0] + 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] + 1, rand_wall[1]])
                    if rand_wall[0] != 0:
                        if grid[rand_wall[0] - 1][rand_wall[1]].is_active == False or grid[rand_wall[0] - 1][
                            rand_wall[1]].is_visited == False:
                            grid[rand_wall[0] - 1][rand_wall[1]].is_active = False
                            grid[rand_wall[0] - 1][rand_wall[1]].is_visited = True
                        if [rand_wall[0] - 1, rand_wall[1]] not in walls:
                            walls.append([rand_wall[0] - 1, rand_wall[1]])

                # Delete wall
                for wall in walls:
                    if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                        walls.remove(wall)

                continue

        # Delete the wall from the list anyway
        for wall in walls:
            if wall[0] == rand_wall[0] and wall[1] == rand_wall[1]:
                walls.remove(wall)

    # Mark the remaining unvisited cells as walls
    for i in range(0, height):
        for j in range(0, width):
            if grid[i][j].is_visited == False:
                grid[i][j].is_active = False

    for i in range(0, height):
        for j in range(0, width):
            grid[i][j].is_visited = False
