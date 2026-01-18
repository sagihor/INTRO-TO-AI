goal_state = []


def init_goal_for_search(goal_blocks):
    global goal_state
    list_of_string = goal_blocks.split(",")
    goal_state = [int(item) for item in list_of_string]


def get_state_str(tuple_of_blocks):
    final_str = ""
    index = 0
    for tup in tuple_of_blocks:
        if index == 0:
            final_str = final_str + str(tup)
        else:
            final_str = final_str + f",{str(tup)}"
        index = index + 1
    return final_str


class color_blocks_state:
    # you can add global params
    def __init__(self, blocks_str, **kwargs):
        # you can use the init function for several purposes
        # in case we have not needed space
        if type(blocks_str) == str:
            blocks_str = blocks_str.replace(" ", "")
            parts = blocks_str.split("),")
            list_of_blocks = []
            for part in parts:
                part = part.replace("(", "").replace(")", "")
                a, b = part.split(",")
                list_of_blocks.append((int(a), int(b)))
            self.tuple_of_blocks = tuple(list_of_blocks)
        else:  # is tuple
            self.tuple_of_blocks = tuple((a, b) for (a, b) in blocks_str)
        # I chose to use tuple because the hashing process is fast. it will be useful in dictionary

    @staticmethod
    def is_goal_state(_color_blocks_state):
        blocks_list = _color_blocks_state.tuple_of_blocks
        for i in range(len(goal_state)):
            if goal_state[i] != blocks_list[i][0]:
                return False
        return True

    def spin_at_index(self, index):
        copy_of_blocks_list = []
        for block in self.tuple_of_blocks:
            copy_of_blocks_list.append((block[0], block[1]))
        tuple_to_flip = copy_of_blocks_list[index]
        new_tuple = (tuple_to_flip[1], tuple_to_flip[0])
        copy_of_blocks_list[index] = new_tuple
        copy_tuple_of_blocks = tuple(copy_of_blocks_list)
        return copy_tuple_of_blocks

    def flip_up_to(self, index):
        new_list = []
        # Appeanding in reverse up to the given index
        for i in range(len(self.tuple_of_blocks)-1, index-1, -1):
            new_list.append(self.tuple_of_blocks[i])
        # adding the rest
        for i in range(0, index):
            new_list.append(self.tuple_of_blocks[i])
        new_tuple = tuple(new_list)
        return new_tuple

    def get_neighbors(self):
        neighbors_list = []
        # Generating all neighbors given from one spin.
        for i in range(len(self.tuple_of_blocks)):
            neighbor_from_spin = color_blocks_state(self.spin_at_index(i))
            neighbors_list.append((neighbor_from_spin, 1))
        # Generating all neighbors given from a flip.
        for i in range(1, len(self.tuple_of_blocks)):
            neighbor_from_flip = color_blocks_state(self.flip_up_to(i))
            neighbors_list.append((neighbor_from_flip, 1))
        return neighbors_list

    def __hash__(self):
        return hash(self.tuple_of_blocks)

        # you can change the body of the function if you want

    def __eq__(self, other):
        return self.tuple_of_blocks == other.tuple_of_blocks
        # you can change the body of the function if you want

    # for debugging states
    def get_state_str(self):
        final_str = ""
        index = 0
        for tup in self.tuple_of_blocks:
            if index == 0:
                final_str = final_str + str(tup)
            else:
                final_str = final_str + f",{str(tup)}"
            index = index + 1
        return final_str

    def __repr__(self):
        return f"{self.get_state_str()}"
    # you can add helper functions
