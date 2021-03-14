import pygame


class Cell:
    def __init__(self, x, y):
        self.column_ind = x
        self.row_ind = y
        self.value = 1
        self.observed = False
        self.previous = None
        self.neighbors = []

    def draw_cell(self, surface, cell_width, color, line_width=0):
        cell = pygame.Rect(cell_width * self.column_ind, cell_width * self.row_ind, cell_width, cell_width)
        pygame.draw.rect(surface, color, cell, width=line_width)

    def change_value(self):
        self.value = 0

    def add_neighbors(self, grid):
        i = self.row_ind
        j = self.column_ind
        rows_number = len(grid) - 1
        columns_number = len(grid[0]) - 1
        if i > 0 and grid[i - 1][j].value:
            self.neighbors.append(grid[i - 1][j])
        if i < rows_number and grid[i + 1][j].value:
            self.neighbors.append(grid[i + 1][j])
        if j < columns_number and grid[i][j + 1].value:
            self.neighbors.append(grid[i][j + 1])
        if j > 0 and grid[i][j - 1].value:
            self.neighbors.append(grid[i][j - 1])
        if i > 0 and j < columns_number and grid[i - 1][j + 1].value:
            self.neighbors.append(grid[i - 1][j + 1])
        if i > 0 and j > 0 and grid[i - 1][j - 1].value:
            self.neighbors.append(grid[i - 1][j - 1])
        if i < rows_number and j < columns_number and grid[i + 1][j + 1].value:
            self.neighbors.append(grid[i + 1][j + 1])
        if i < rows_number and j > 0 and grid[i + 1][j - 1].value:
            self.neighbors.append(grid[i + 1][j - 1])


