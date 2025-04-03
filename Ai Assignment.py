import collections
from itertools import permutations

BOARD_SIZE = 8

KNIGHT_MOVES = [(-2, -1), (-2, 1), (2, -1), (2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2)]
# Letters for my name: Jad Atout
LETTERS = ['J', 'A', 'D', 'T', 'O', 'U']
# Example states for there different tries
state_1 = [('J', (1, 1)), ('A', (2, 2)), ('D', (4, 1)), ('T', (2, 4)), ('O', (5, 4)), ('U', (6, 7))]
state_2 = [('J', (3, 2)), ('A', (4, 3)), ('D', (5, 3)), ('T', (4, 5)), ('O', (6, 5)), ('U', (4, 6))]
state_3 = [('J', (2, 3)), ('A', (3, 4)), ('D', (6, 2)), ('T', (1, 3)), ('O', (7, 3)), ('U', (8, 6))]




initial_state = tuple(sorted(state_3, key=lambda x: x[0]))
user_letter = None




def is_knight_move(start, end):
    x1, y1 = start
    x2, y2 = end
    return (abs(x1 - x2), abs(y1 - y2)) in [(2, 1), (1, 2)]


def find_knight_path(state, current_position, visited):

    if len(visited) == len(state):
        return True

    for next_letter, next_position in state.items():

        if next_position not in visited and is_knight_move(current_position, next_position):
            if find_knight_path(state, next_position, visited | {next_position}):
                return True

    return False


def is_goal(state, start_letter):
    state_dict = {letter: pos for letter, pos in state}
    if start_letter not in state_dict:
        return False
    start_position = state_dict[start_letter]
    return find_knight_path(state_dict, start_position, {start_position})


# ---------------------------------------
# 3) توليد الحالات اللاحقة (Successors)
# ---------------------------------------

def get_new_states(current_state):

    possible_states = []
    state_list = list(current_state)  # Convert tuple to a mutable list

    # Track occupied positions
    occupied_positions = {position for (_, position) in state_list}

    for index, (piece, (row_index, column_index)) in enumerate(state_list):
        possible_moves = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        for row_offset, column_offset in possible_moves:
            new_row_index = row_index + row_offset
            new_column_index = column_index + column_offset

            # Check if the new position is inside the board
            if 0 <= new_row_index < BOARD_SIZE and 0 <= new_column_index < BOARD_SIZE:

                # Check if the new position is not occupied
                if (new_row_index, new_column_index) not in occupied_positions:
                    # Create a new updated state
                    updated_state = state_list[:]
                    updated_state[index] = (piece, (new_row_index, new_column_index))

                    # Convert back to a tuple and sort by piece name for consistency
                    new_state_tuple = tuple(sorted(updated_state, key=lambda x: x[0]))
                    move_description = f"{piece} moves from ({row_index},{column_index}) to ({new_row_index},{new_column_index})"

                    possible_states.append((new_state_tuple, move_description))

    return possible_states




def dfs(initial_state, start_letter):
    stack = [(initial_state, [])]
    visited_states = set([initial_state])
    expanded_states_count = 0

    while stack:
        current_state, path_taken = stack.pop()
        expanded_states_count += 1

        # Check if the current state is the goal
        if is_goal(current_state, start_letter):
            return current_state, path_taken, expanded_states_count

        # Explore all possible new states
        for next_state, move_description in get_new_states(current_state):
            if next_state not in visited_states:
                visited_states.add(next_state)
                stack.append((next_state, path_taken + [move_description]))

    return None, None, expanded_states_count






def bfs(initial_state, start_letter):
    queue = collections.deque([(initial_state, [])])
    visited_states = set([initial_state])
    expanded_states_count = 0

    while queue:
        current_state, path_taken = queue.popleft()
        expanded_states_count += 1

        if is_goal(current_state, start_letter):
            return current_state, path_taken, expanded_states_count


        for next_state, move_description in get_new_states(current_state):
            if next_state not in visited_states:
                visited_states.add(next_state)
                queue.append((next_state, path_taken + [move_description]))

    return None, None, expanded_states_count




def main():
    global user_letter
    print("\nHello! Let's play the Knight's Move Game.")
    print("Student Name: Jad Atout")
    print("\nHere's the list of letters you can choose from: ", ", ".join(LETTERS))
    print("\nInitial State (starting positions):")

    for letter, position in initial_state:
        print(f"  {letter} starts at {position}")

    print("\nNow, pick a letter to start with.")

    while True:
        user_input = input(f"Enter your chosen letter from {LETTERS}: ").upper().strip()
        if user_input in LETTERS:
            user_letter = user_input
            break
        else:
            print(f"Oops! '{user_input}' is not valid. Choose a letter from {LETTERS}.")

    # --------- DFS Search -----------
    print("\nLet's try Depth First Search (DFS) now...")
    goal_state_dfs, path_dfs, expanded_dfs = dfs(initial_state, user_letter)

    if goal_state_dfs:
        print("\nGreat! We found the goal using DFS!")
        print("Goal State (final positions):")
        for letter, pos in sorted(goal_state_dfs, key=lambda x: x[0]):
            print(f"  {letter} is at {pos}")

        print("\nHere's the sequence of moves in DFS:")
        for step in path_dfs:
            print(f"  {step}")

        print(f"\nIn DFS, we expanded {expanded_dfs} states.")
    else:
        print("\nNo solution was found using DFS.")
        print(f"DFS expanded {expanded_dfs} states.")

    print("=" * 60)

    # --------- BFS Search -----------
    print("\nNow, let's try Breadth First Search (BFS)...")
    goal_state_bfs, path_bfs, expanded_bfs = bfs(initial_state, user_letter)

    if goal_state_bfs:
        print("\nSuccess! We found the goal using BFS!")
        print("Goal State (final positions):")
        for letter, pos in sorted(goal_state_bfs, key=lambda x: x[0]):
            print(f"  {letter} is at {pos}")

        print("\nHere's the sequence of moves in BFS:")
        for step in path_bfs:
            print(f"  {step}")

        print(f"\nIn BFS, we expanded {expanded_bfs} states.")
    else:
        print("\nNo solution was found using BFS.")
        print(f"BFS expanded {expanded_bfs} states.")

    print("=" * 60)


if __name__ == "__main__":
    main()
