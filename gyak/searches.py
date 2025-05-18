def search(problem, is_depth_first=False, graph_search=False):
    initial_node = (problem.initial, None)
    frontier = [initial_node]
    search_path = []
    explored = set()

    while frontier:
        if is_depth_first:
            current_state, parent = frontier.pop()
        else:
            current_state, parent = frontier.pop(0)

        search_path.append((current_state, parent))

        if problem.goal_test(current_state):
            print("goal")
            return (current_state, parent), search_path

        if graph_search:
            explored.add(current_state)

        for action, next_state in problem.next_state(current_state):
            if not graph_search or (
                next_state not in explored and next_state not in [state for state, parent in frontier]
            ):
                frontier.append((next_state, (current_state, parent)))

    print("unsolvable")
    return None, None