import pygame, sys
from pygame.sprite import Group
from cell import Cell
from turn import Turn

# We start with crosses
turn = Turn.CROSSES

def check_events(cells, is_game_ended):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            on_cell_click(cells, (event.pos[0], event.pos[1]))
            if check_game_end(cells):
                is_game_ended = True

def create_cells(screen):
    # implying that the screen is a square
    size = screen.get_width() * 0.2
    cells = Group()
    for i in range(3):
        left = size + i * (size + 2)
        for j in range(3):
            top = size + j * (size + 2)
            cell = Cell(screen, {'left': left, 'top': top, 'size': size })
            cells.add(cell)

    return cells

def toggle_cell(cell):
    if cell.is_togglable():
        cell.fill(turn)
        toggle_turn()

def toggle_turn():
    global turn
    if turn == Turn.CROSSES:
        turn = Turn.NOUGHTS
    else:
        turn = Turn.CROSSES

def on_cell_click(cells, event_pos):
    for cell in cells:
        x1 = cell.coords['left']
        x2 = cell.coords['left'] + cell.coords['size']
        y1 = cell.coords['top']
        y2 = cell.coords['top'] + cell.coords['size']
        if x1 <= event_pos[0] <= x2 and y1 <= event_pos[1] <= y2:
            toggle_cell(cell)

def check_game_end(cells):
    cells_list = list(map(lambda c: c, cells))
    cells_signs = list(map(lambda c: c.sign, cells_list))
    screen = cells_list[0].screen
    line_color = (0, 0, 0)
    for i in range(3):
        # rows
        if all(cells_signs[i::3]) and len(set(cells_signs[i::3])) == 1:
            start_pos = cells_list[i].coords['left'], cells_list[i].coords['top'] + cells_list[i].coords['size'] / 2
            end_pos = cells_list[i+6].coords['left'] + cells_list[i+6].coords['size'], cells_list[i+6].coords['top'] + cells_list[i+6].coords['size'] / 2
            pygame.draw.line(screen, line_color, start_pos, end_pos)
            return cells_list[i].sign
        # cols
        elif all(cells_signs[i:i+3]) and len(set(cells_signs[i:i+3])) == 1:
            start_pos = cells_list[i].coords['left'] + cells_list[i].coords['size'] / 2, cells_list[i].coords['top']
            end_pos = cells_list[i+3].coords['left'] + cells_list[i+3].coords['size'] / 2, cells_list[i+3].coords['top'] + cells_list[i+3].coords['size']
            pygame.draw.line(screen, line_color, start_pos, end_pos)
            return cells_list[i].sign

    # main diag
    if all(cells_signs[::4]) and len(set(cells_signs[::4])) == 1:
        start_pos = cells_list[0].coords['left'], cells_list[0].coords['top']
        end_pos = cells_list[8].coords['left'] + cells_list[8].coords['size'], cells_list[8].coords['top'] + cells_list[8].coords['size']
        pygame.draw.line(screen, line_color, start_pos, end_pos)
        return cells_list[i].sign
    # other diag
    elif all(cells_signs[::2]) and len(set(cells_list[::2])) == 1:
        start_pos = cells_list[6].coords['left'] + cells_list[6].coords['size'], cells_list[6].coords['top']
        end_pos = cells_list[2].coords['left'], cells_list[2].coords['top'] + cells_list[2].coords['size']
        pygame.draw.line(screen, line_color, start_pos, end_pos)
        return cells_list[i].sign

    return False
