import pygame, sys
from pygame.sprite import Group
from cell import Cell
from turn import Turn

# We start with crosses
turn = Turn.CROSSES

def check_events(cells):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.MOUSEBUTTONUP:
            on_cell_click(cells, (event.pos[0], event.pos[1]))
            
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
    for cell in cells:
        