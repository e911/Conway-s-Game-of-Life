from copy import copy

ALIVE = True
DEAD = False

CURRENT_GEN = {(22, 5), (23, 5), (24, 5), (24, 6), (23, 7)}
OLD_GEN = {}
X_BOUNDARY = 80
Y_BOUNDARY = 80

def clean_boundary(neighbours):
	"""Make sure the points stay withing boundary by warping the boundary"""
	return set(map(lambda x: (1 if x[0]>X_BOUNDARY else X_BOUNDARY if x[0]==0 else x[0],
						1 if x[1]>Y_BOUNDARY else Y_BOUNDARY if x[1]==0 else x[1]),
						neighbours))

def get_cell_neighbours(cell):
	"""Returns a list of coordinate points of neighbours of given cell"""
	x_coordinate=cell[0]
	y_coordinate=cell[1]
	neighbours=set()
	for x in range(x_coordinate-1,x_coordinate+2):
		for y in range(y_coordinate-1,y_coordinate+2):
			if (x,y)==cell:
				pass
			else:
				neighbours.add((x,y))
	return clean_boundary(neighbours)

def get_number_of_alive_neighbours_of_a_point(cell):
	neighbours = get_cell_neighbours(cell)
	return len(CURRENT_GEN.intersection(neighbours))

def rule_one(cell):
	"""Any live cell with fewer than two live neighbours dies, as if caused by underpopulation"""
	if cell in CURRENT_GEN and get_number_of_alive_neighbours_of_a_point(cell)<2:
		return DEAD
	return ALIVE
	
def rule_two(cell):
	"""Any live cell with two or three live neighbours lives on to the next generation."""
	if cell in CURRENT_GEN and get_number_of_alive_neighbours_of_a_point(cell) in (2,3):
		return ALIVE
	return DEAD

def rule_three(cell):
	"""Any live cell with more than three live neighbours dies, as if by overpopulation."""
	if cell in CURRENT_GEN and get_number_of_alive_neighbours_of_a_point(cell)>3:
		return DEAD
	return ALIVE

def rule_four(cell):
	"""Any dead cell with exactly three live neighbours becomes a live cell, as if by reproduction."""
	if cell not in CURRENT_GEN and get_number_of_alive_neighbours_of_a_point(cell)==3:
		return ALIVE
	return DEAD

def game_of_life():
    global CURRENT_GEN
    global OLD_GEN
    NEW_GEN = set()
    OLD_GEN = copy(CURRENT_GEN)
    print(CURRENT_GEN)
    for cell in CURRENT_GEN:
        neighbours = get_cell_neighbours(cell).difference(CURRENT_GEN)
        for neighbour in neighbours:
            if rule_four(neighbour):
                NEW_GEN.add(neighbour)
        if rule_one(cell) and rule_two(cell) and rule_three(cell):
            print(2)
            NEW_GEN.add(cell)
    CURRENT_GEN = copy(NEW_GEN)
    print(CURRENT_GEN)   
    print("finish") 
    CURRENT_GEN = clean_boundary(CURRENT_GEN)
    if CURRENT_GEN == OLD_GEN:
        print ("Game of life complete")


if __name__ == "__main__":
	game_of_life()