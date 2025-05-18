class Node:
    # Tartalmaz egy állapotot és egy szülőt
    def __init__(self, state, parent=None):
        self.state = state
        self.parent = parent

    # Megadja, hogy milyen 1 lépésből meglátogható csomópontok vannak
    def expand(self, problem):
        li = []
        for act in problem.actions(self.state):
            li.append(Node(problem.result(self.state, act), self))
        return li


def search(problem, is_depth_first=False, graph_search=False):
    initial_node = Node(problem.initial)
    frontier = [initial_node]
    search_path = []    # Csomópontok útvonala
    explored = set()    # Gráfkereséshez

    while frontier:     # addig megyünk, míg vannak csomópontok
        if is_depth_first:
            selected_node = frontier.pop()  #LIFO
        else:
            selected_node = frontier.pop(0) #FIFO

        search_path.append(selected_node)

        if problem.goal_test(selected_node.state):
            print('GOAL!')
            return selected_node, search_path

        if graph_search:
            explored.add(selected_node.state)

        children = selected_node.expand(problem)
        for child in children:
            if not graph_search or child.state not in explored:
                # Elkerüljük a duplikátumokat a frontier-ben is gráfkeresésnél
                if child not in frontier:
                    frontier.append(child)

    print('Unsolvable')
    return None, None


def breadth_first_tree_search(problem):
    return search(problem, is_depth_first=False, graph_search=False)

def breadth_first_graph_search(problem):
    return search(problem, is_depth_first=False, graph_search=True)

def depth_first_tree_search(problem):
    return search(problem, is_depth_first=True, graph_search=False)

def depth_first_graph_search(problem):
    return search(problem, is_depth_first=True, graph_search=True)