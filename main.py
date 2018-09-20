from copy import copy
from datetime import datetime

from GameOfLife import *
from conway import *

pygame.init()

size = width, height = 600, 600
white = pygame.Color(255, 255, 255)
black = pygame.Color(0, 0, 255)
screen = pygame.display.set_mode(size)

CURRENT_GEN = CUSTOM_GEN


def game_of_life(CURRENT_GEN):
    count = 0
    # OLD_GEN = copy(CURRENT_GEN)
    # first_pass = True
    # start_time = datetime.now()
    # while CURRENT_GEN != OLD_GEN or first_pass:
    while 1:
        NEW_GEN = set()
        if count == 25:
            count = 0
            NEW_GEN = NEW_GEN.union(CUSTOM_GEN)
        # first_pass = False
        for cell in CURRENT_GEN:
            neighbours = get_cell_neighbours(cell).difference(CURRENT_GEN)
            for neighbour in neighbours:
                if rule_four(neighbour, CURRENT_GEN):
                    NEW_GEN.add(neighbour)
            if rule_one(cell, CURRENT_GEN) and rule_two(cell, CURRENT_GEN) and rule_three(cell, CURRENT_GEN):
                NEW_GEN.add(cell)
        CURRENT_GEN = copy(NEW_GEN)
        print(CURRENT_GEN)
        CURRENT_GEN = clean_boundary(CURRENT_GEN)
        for i in CURRENT_GEN:
            pygame.draw.line(screen, white, i, i)
            pygame.display.flip()
        screen.fill(black)
        count += 1
        # if CURRENT_GEN == OLD_GEN:
        #     finish_time = datetime.now()
        #     print("Total number of iterations :", count)
        #     print("Total time taken:", finish_time - start_time)
        #     print("Game of life complete!!")


if __name__ == "__main__":
    game_of_life(CURRENT_GEN)
