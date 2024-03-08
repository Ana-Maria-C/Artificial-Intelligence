import time
from GameState import GameState


def main():
    state1 = GameState([8, 6, 7, 2, 5, 4, 0, 3, 1])
    state2 = GameState([2, 5, 3, 1, 0, 6, 4, 7, 8])
    state3 = GameState([2, 7, 5, 0, 8, 4, 3, 1, 6])
    states = [state1, state2, state3]

    for state in states:
        print(f"For state: {state.vect[1:]}")
        print()
        # Greedy with Manhattan Distance Heuristic
        start_time = time.time()
        solution, max_depth = state.greedy_search(GameState.manhattan_distance)
        end_time = time.time()
        print("Greedy with Manhattan Distance Heuristic:")
        print_solution_info(solution, max_depth, start_time, end_time)
        print()

        # Greedy with Hamming Distance Heuristic
        start_time = time.time()
        solution, max_depth = state.greedy_search(GameState.hamming_distance)
        end_time = time.time()
        print("Greedy with Hamming Distance Heuristic:")
        print_solution_info(solution, max_depth, start_time, end_time)
        print()

        # Greedy with My Heuristic
        start_time = time.time()
        solution, max_depth = state.greedy_search(GameState.my_heuristic)
        end_time = time.time()
        print("Greedy with My Heuristic:")
        print_solution_info(solution, max_depth, start_time, end_time)

        # IDDFS
        start_time = time.time()
        solution, max_depth, moves = state.iddfs()
        end_time = time.time()
        print("IDDFS:")
        print_solution_info(solution, max_depth, start_time, end_time)
        print()


def print_solution_info(solution, max_depth, start_time, end_time):
    if solution is not None:
        print("Solution found:")
        print(solution.vect[1:])
        # print("Moves:", solution.moves)
        print("Max depth:", max_depth)
        time_taken = end_time - start_time
        print(f"Time taken to find the solution: {time_taken} seconds")
    else:
        print("No solution found.")


if __name__ == '__main__':
    main()
