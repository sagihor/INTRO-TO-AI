from color_blocks_state import color_blocks_state
# you can add helper functions and params
'''this function returns tuple of all colors combination of a neighboring cubes '''


def generate_colors_combination_for_pair(first_cube: tuple, second_cube: tuple):
    comb = []
    comb.append((first_cube[0], first_cube[1]))
    comb.append((second_cube[0], second_cube[1]))
    comb.append((first_cube[0], second_cube[1]))
    comb.append((second_cube[0], first_cube[1]))
    comb.append((first_cube[0], second_cube[0]))
    comb.append((first_cube[1], second_cube[1]))
    return comb


def generate_neighbors_in_goal(goal: list):
    comb = []
    for i in range(len(goal) - 1):
        j = i + 1
        comb.append((goal[i], goal[j]))
        comb.append((goal[j], goal[i]))
    return comb

goal_state_list = []
goal_state_set = None


def init_goal_for_heuristics(goal_blocks: str):
    global goal_state_list
    global goal_state_set
    list_of_string = goal_blocks.split(",")
    goal_state_list = [int(item) for item in list_of_string]
    goal_state_set = set(goal_state_list)


def base_heuristic(_color_blocks_state: color_blocks_state):
    value = 0
    goal_combinations = generate_neighbors_in_goal(goal_state_list)
    blocks_list = _color_blocks_state.tuple_of_blocks
    for i in range(len(blocks_list) - 1):
        j = i + 1
        blocks_combinatins = generate_colors_combination_for_pair(blocks_list[i], blocks_list[j])
        value_to_add = 1
        for comb in goal_combinations:
            if comb in blocks_combinatins:
                value_to_add = 0
                break
        value = value + value_to_add
    return value

'''counting the number of cubes that are in the face of the color_block_state and not in the goal state'''
def advanced_heuristic(_color_blocks_state):
    value = 0
    for (front, side) in _color_blocks_state.tuple_of_blocks:
        if front not in goal_state_set:
            value = value + 1
    return value

