def search(problem, is_depth_first=False, graph_search=False):
    # 1. node: (allapot, szulo)
    initial_node = (problem.initial, None)
    # felfedezere varo allapotok
    frontier = [initial_node]
    # eddig bejart
    search_path = []
    # felfedezett node-ok (grafkereseshez)
    explored = set()

    # addig fut a loop, amig el nem erunk a felfedezendo node-ok vegere
    while frontier:
        # kovetkezo allapot kivalasztasa, attol fuggoen
        # hogy milyen keresest csinalunk
        if is_depth_first:  # FIFO, depth-first
            current_state, parent = frontier.pop(0)
        else:   # LIFO, width-first
            current_state, parent = frontier.pop()

        # aktualis allapot hozzafuzese a bejart uthoz
        search_path.append((current_state, parent))

        # ha elerjuk a celallapotot:
        if problem.goal_test(current_state):
            print('GOAL!')
            return (current_state, parent), search_path

        # grafkeresesnel a felfedezett allapotok rogzitese itt:
        if graph_search:
            explored.add(current_state)

        for action, next_state in problem.next_state(current_state):
            # ha nem grafkereses, akkor ez fix lefut
            # ha grafos, akkor a kovetkezo state-nek nem szabad az eddig felfedezettben lennie
            if not graph_search or next_state not in explored:
                frontier.append((next_state, (current_state, action)))

    print('Unsolvable')
    return None, None
