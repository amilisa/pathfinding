import pygame
import sys
import tkinter as tk
from Cell import Cell
from path_finding_algorithm import breadth_first_search as bfs


WIDTH, HEIGHT = 600, 600
FPS = 60
GREY = (51, 51, 51)
WHITE = (255, 255, 255)
BLUE = (30, 144, 255)
GREEN = (0, 250, 154)
ROWS_NUMBER, COLUMNS_NUMBER = 28, 28
CELL_WIDTH, CELL_HEIGHT = 560 / ROWS_NUMBER, 560 / ROWS_NUMBER

grid = [[Cell(i, j) for i in range(COLUMNS_NUMBER)] for j in range(ROWS_NUMBER)]
start_point = grid[0][0]
end_point = grid[27][27]


def draw_grid(surface, array, color, width, height):
    pygame.draw.rect(surface, color, (0, 0, width, height), width=40)
    for i in range(0, ROWS_NUMBER):
        for j in range(0, COLUMNS_NUMBER):
            array[i][j].draw_cell(surface, CELL_WIDTH, color, 1)
    pygame.display.update()


def transform_to_index(y, x, cell_width):
    i = int(y // cell_width) - 1
    j = int(x // cell_width) - 1
    return i, j


def submit():
    global start_point
    global end_point
    start_row, start_column = [int(item) for item in entry_start_point.get().split(',')]
    end_row, end_column = [int(item) for item in entry_end_point.get().split(',')]
    start_point = grid[start_row][start_column]
    end_point = grid[end_row][end_column]
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
    WINDOW.fill(WHITE)
    pygame.display.set_caption("Path Finding")
    clock = pygame.time.Clock()
    draw_grid(WINDOW, grid, GREY, WIDTH, HEIGHT)
    start_point.draw_cell(WINDOW, CELL_WIDTH, (0, 0, 0))
    end_point.draw_cell(WINDOW, CELL_WIDTH, (14, 67, 90))
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
                i, j = transform_to_index(y, x, CELL_WIDTH)
                grid[i][j].draw_cell(WINDOW, CELL_WIDTH, BLUE)
                pygame.display.update()
                grid[i][j].change_value()
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
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
            cell.draw_cell(WINDOW, CELL_WIDTH, GREEN)
            pygame.time.delay(50)
            pygame.display.update()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()


if __name__ == "__main__":
    main()