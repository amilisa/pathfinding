import pygame


class Cell:
    def __init__(self, x, y):
        self.column_ind = x
        self.row_ind = y
        self.value = 1
        self.is_observed = False
        self.previous = None
        self.neighbors = []
        self.is_path_point = False

    def draw_cell(self, surface, cell_width, color, line_width=0):
        cell = pygame.Rect(cell_width * self.column_ind, cell_width * self.row_ind, cell_width, cell_width)
        pygame.draw.rect(surface, color, cell, width=line_width)

    def change_value(self):
        self.value = 0

    def add_neighbors(self, grid):
        rows_number = len(grid)
        columns_number = len(grid[0])
        direction_vector_row = [-1, 1, 0, 0, -1, -1, 1, 1]
        direction_vector_column = [0, 0, 1, -1, -1, 1, 1, -1]
        for i in range(8):
            row = self.row_ind + direction_vector_row[i]
            column = self.column_ind + direction_vector_column[i]
            if row < 0 or column < 0:
                continue
            if row >= rows_number or column >= columns_number:
                continue
            if grid[row][column].value:
                self.neighbors.append(grid[row][column])




