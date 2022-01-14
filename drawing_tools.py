import os
import pygame
from constants.sizes import CELL_SIZE, ROWS_NUMBER, COLUMNS_NUMBER
from constants.colors import *


def draw_instructions(surface, position_x, position_y, color):
    font = pygame.font.Font(os.path.join("font", "joystix monospace.ttf"), 12)
    obstacles_instruction = font.render("Click on the grid and drag the mouse to draw obstacles", True, color)
    start_instruction = font.render("Press F to start the search", True, color)
    surface.blit(obstacles_instruction, (position_x, position_y - 60))
    surface.blit(start_instruction, (position_x, position_y - 40))


def create_grid_wrapper(surface, position_x, position_y, width, height, color):
    subsurface_rect = pygame.Rect(position_x, position_y, width, height)
    grid_wrapper = surface.subsurface(subsurface_rect)
    grid_wrapper.fill(color)
    return grid_wrapper


def draw_grid(surface, grid, rows_number, columns_number, cell_size, color):
    for i in range(0, rows_number):
        for j in range(0, columns_number):
            grid[i][j].draw_cell(surface, cell_size, color, 1)
    pygame.display.update()


def draw_path_point(i, j, surface, grid, cell_size, color):
    grid[i][j].draw_cell(surface, cell_size, color)
    pygame.display.update()
    grid[i][j].is_path_point = True


def draw_obstacle(i, j, surface, grid, cell_size, color):
    if not grid[i][j].is_path_point:
        grid[i][j].draw_cell(surface, cell_size, color)
        pygame.display.update()
        grid[i][j].is_active = False


def draw_path(path, surface, goal, cell_size, color, grid):
    for cell in path:
        if cell is not goal:
            cell.draw_cell(surface, cell_size, color)
            pygame.time.delay(50)
            draw_grid(surface, grid, ROWS_NUMBER, COLUMNS_NUMBER, CELL_SIZE, GREY)
