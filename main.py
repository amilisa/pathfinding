import pygame
import sys
import tkinter as tk
from Cell import Cell
from path_finding_algorithm import breadth_first_search as bfs


WIDTH, HEIGHT = 600, 650
FPS = 60
GREY = (51, 51, 51)
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
GREEN = (0, 250, 154)
RED = (255, 65, 84)
ROWS_NUMBER, COLUMNS_NUMBER = 28, 28
MIN_INDEX = 0
MAX_INDEX = 27
GRID_SIZE = 560
CELL_WIDTH, CELL_HEIGHT = GRID_SIZE / ROWS_NUMBER, GRID_SIZE / ROWS_NUMBER
SUB_ORIGIN = 20

grid = [[Cell(i, j) for i in range(COLUMNS_NUMBER)] for j in range(ROWS_NUMBER)]
start_point = grid[MIN_INDEX][MIN_INDEX]
end_point = grid[MAX_INDEX][MAX_INDEX]


def draw_grid(surface, array, color):
    for i in range(0, ROWS_NUMBER):
        for j in range(0, COLUMNS_NUMBER):
            array[i][j].draw_cell(surface, CELL_WIDTH, color, 1)
    pygame.display.update()


def is_index_valid(row, column, min_index, max_index):
    if row < min_index or row > max_index:
        return False
    if column < min_index or column > max_index:
        return False
    return True


def transform_to_index(y, x, cell_width):
    i = int(y // cell_width)
    j = int(x // cell_width)
    return i, j


def submit():
    global start_point
    global end_point
    start_row, start_column = [int(item) for item in entry_start_point.get().split(',')]
    end_row, end_column = [int(item) for item in entry_end_point.get().split(',')]
    start_point = grid[start_row][start_column]
    end_point = grid[end_row][end_column]
    grid[start_row][start_column].is_path_point = True
    grid[end_row][end_column].is_path_point = True
    window.destroy()


window = tk.Tk()
window.title('Entry window')
window.resizable(False, False)

label_start_point = tk.Label(master=window, text="Start point (row, column):")
label_end_point = tk.Label(master=window, text="End point (row, column):")
entry_start_point = tk.Entry(master=window, width=15)
entry_end_point = tk.Entry(master=window, width=15)
button_submit = tk.Button(master=window, text="Submit", command=submit)

label_start_point.grid(row=0, column=0, padx=5, pady=10)
label_end_point.grid(row=1, column=0, padx=5, pady=10)
entry_start_point.grid(row=0, column=1, padx=5)
entry_end_point.grid(row=1, column=1, padx=5)
button_submit.grid(columnspan=2, row=2, pady=5)

window.update()
s = window.geometry()
window_width, window_height = [int(i) for i in window.geometry().split("+")[0].split("x")]
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width / 2 - window_width / 2)
y = int(screen_height / 2 - window_height / 2)
window.geometry(f"+{x}+{y}")
window.mainloop()


def main():
    pygame.init()
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
    WINDOW.fill(GREY)
    pygame.display.set_caption("Path Finding")
    clock = pygame.time.Clock()
    subsurface_rect = pygame.Rect(SUB_ORIGIN, SUB_ORIGIN, GRID_SIZE, GRID_SIZE)
    grid_wrapper = WINDOW.subsurface(subsurface_rect)
    grid_wrapper.fill(WHITE)
    draw_grid(grid_wrapper, grid, GREY)
    start_point.draw_cell(grid_wrapper, CELL_WIDTH, GREEN)
    end_point.draw_cell(grid_wrapper, CELL_WIDTH, RED)
    pygame.display.update()

    running = True
    while running:
        clock.tick(FPS)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                sys.exit()

            is_left_mouse_button_down = pygame.mouse.get_pressed()[0]
            if is_left_mouse_button_down:
                x, y = pygame.mouse.get_pos()
                i, j = transform_to_index(y - SUB_ORIGIN, x - SUB_ORIGIN, CELL_WIDTH)
                if is_index_valid(i, j, MIN_INDEX, MAX_INDEX) and not grid[i][j].is_path_point:
                    grid[i][j].draw_cell(grid_wrapper, CELL_WIDTH, BLUE)
                    pygame.display.update()
                    grid[i][j].change_value()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_f:
                running = False
                break

    for i in range(ROWS_NUMBER):
        for j in range(COLUMNS_NUMBER):
            grid[i][j].add_neighbors(grid)

    path = bfs(start_point, end_point)
    if not path:
        print("There is no path")
    else:
        for cell in path:
            cell.draw_cell(grid_wrapper, CELL_WIDTH, GREEN)
            pygame.time.delay(50)
            pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()


if __name__ == "__main__":
    main()
