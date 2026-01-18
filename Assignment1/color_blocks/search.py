from search_node import search_node
from color_blocks_state import color_blocks_state
import heapq


def create_open_set():
    open_list = []
    best_g = {}  # state -> g
    heapq.heapify(open_list)
    return open_list,best_g

'''here we use dictionary to have access in o(1) to a the state according to the key. this helpful to the check duplicate function'''
def create_closed_set():
    close_dict = {}
    return close_dict


def add_to_open(vn, open_set):
    heap, best_g = open_set
    heapq.heappush(heap, vn)

    state = vn.state
    if state not in best_g or vn.g < best_g[state]:
        best_g[state] = vn.g


def open_not_empty(open_set):
    # this function also responsible to delete unnecessary nodes in dictionary
    heap, best_g = open_set
    while heap:
        node = heap[0]
        state = node.state
        g = node.g
        if state not in best_g or best_g[state] == g:
            return True
        heapq.heappop(heap)
    return False


def get_best(open_set):
    heap, best_g = open_set
    node = heapq.heappop(heap)
    state = node.state
    g = node.g
    if state not in best_g or best_g[state] == g:
        return node
    return None
'''we select vn.state as a key because we implement __hash__ for it'''


def add_to_closed(vn, closed_set):
    closed_set[vn.state] = vn


# returns False if curr_neighbor state not in open_set or has a lower g from the node in open_set
# remove the node with the higher g from open_set (if exists)
def duplicate_in_open(vn, open_set):
    _, best_g = open_set
    state = vn.state

    if state not in best_g:
        return False
    if vn.g < best_g[state]:
        best_g[state] = vn.g
        return False
    return True


# returns False if curr_neighbor state not in closed_set or has a lower g from the node in closed_set
# remove the node with the higher g from closed_set (if exists)
def duplicate_in_closed(vn, closed_set):
    state = vn.state
    if state not in closed_set:
        return False
    if vn.g < closed_set[state].g:
        del closed_set[state]
        return False
    return True


# helps to debug sometimes..
def print_path(path):
    for i in range(len(path) - 1):
        print(f"[{path[i].state.get_state_str()}]", end=", ")
    print(path[-1].state.get_state_str())


def search(start_state, heuristic):
    open_set = create_open_set()
    closed_set = create_closed_set()
    start_node = search_node(start_state, 0, heuristic(start_state))
    add_to_open(start_node, open_set)

    while open_not_empty(open_set):

        current = get_best(open_set)

        if color_blocks_state.is_goal_state(current.state):
            path = []
            while current:
                path.append(current)
                current = current.prev
            path.reverse()
            return path

        add_to_closed(current, closed_set)

        for neighbor, edge_cost in current.get_neighbors():
            curr_neighbor = search_node(neighbor, current.g + edge_cost, heuristic(neighbor), current)
            if not duplicate_in_open(curr_neighbor, open_set) and not duplicate_in_closed(curr_neighbor, closed_set):
                add_to_open(curr_neighbor, open_set)

    return None
