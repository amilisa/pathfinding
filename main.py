import pygame
import sys
import window_tools
import drawing_tools
import misc

from constants.colors import *
from constants.sizes import *
from Cell import Cell
from EntryWindow import EntryWindow
from path_finding_algorithm import breadth_first_search as bfs


FPS = 60


def main():
    grid = [[Cell(i, j) for i in range(COLUMNS_NUMBER)] for j in range(ROWS_NUMBER)]
    pygame.init()
    clock = pygame.time.Clock()
    WINDOW = window_tools.create_main_window(WIDTH, HEIGHT, GREY, "Path Finding")
    drawing_tools.draw_instructions(WINDOW, SUB_ORIGIN, HEIGHT, WHITE)
    grid_wrapper = drawing_tools.create_grid_wrapper(WINDOW, SUB_ORIGIN, SUB_ORIGIN, GRID_SIZE, GRID_SIZE, WHITE)
    drawing_tools.draw_grid(grid_wrapper, grid, ROWS_NUMBER, COLUMNS_NUMBER, CELL_SIZE, GREY)
    entry_window = EntryWindow()
    entry_window.mainloop()
    start_row, start_column = entry_window.entry_start_row, entry_window.entry_start_column
    end_row, end_column = entry_window.entry_end_row, entry_window.entry_end_column
    start_point, end_point = misc.init_path_points(grid, start_row, start_column, end_row, end_column)
    start_point.draw_cell(grid_wrapper, CELL_SIZE, GREEN)
    end_point.draw_cell(grid_wrapper, CELL_SIZE, RED)
    pygame.display.update()

    running = True
    while running:
        clock.tick(FPS)
        event_list = pygame.event.get()
        for event in event_list:
            if event.type == pygame.QUIT:
                sys.exit()

        mouse_buttons_pressed = pygame.mouse.get_pressed()
        if mouse_buttons_pressed[0]:
            x, y = pygame.mouse.get_pos()
            drawing_tools.draw_obstacle(x, y, grid_wrapper, grid, SUB_ORIGIN, CELL_SIZE, MIN_INDEX, MAX_INDEX, BLUE)

        keys_pressed = pygame.key.get_pressed()
        if keys_pressed[pygame.K_f]:
            running = False

    path = bfs(start_point, end_point, grid, grid_wrapper)
    if path:
        drawing_tools.draw_path(path, grid_wrapper, end_point, CELL_SIZE, GREEN)
        path_length = len(path)
        message = f"The shortest path has been found!\nThe path length is {path_length} blocks."
    else:
        message = "There is no path between the points."
    answer = window_tools.show_message(message)

    if answer:
        main()

    while True:
        event = pygame.event.wait()
        if event.type == pygame.QUIT:
            sys.exit()


if __name__ == "__main__":
    main()
