from search import Problem, Trial_Error


class SlidingBlock(Problem):
    def __init__(self, initial_state):
        super().__init__(initial_state)


    def actions(self, state):
        return ["up", "down", "left", "right"]


    def result(self, state, action):
        new_state = [list(row) for row in state]
        for r_index, row in enumerate(state):
            for c_index, col in enumerate(row):
                if state[r_index][c_index] == 0:
                    try:
                        if action == "up":
                            new_state[r_index][c_index] = state[r_index + 1][c_index]
                            new_state[r_index + 1][c_index] = 0
                        elif action == "down":
                            new_state[r_index][c_index] = state[r_index - 1][c_index]
                            new_state[r_index - 1][c_index] = 0
                        elif action == "left":
                            new_state[r_index][c_index] = state[r_index][c_index - 1]
                            new_state[r_index][c_index - 1] = 0
                        elif action == "right":
                            new_state[r_index][c_index] = state[r_index][c_index + 1]
                            new_state[r_index][c_index + 1] = 0
                    except:
                        return state
                    finally:
                        break

        return new_state


    def goal_test(self, state):
        return state == [[1, 2, 3], [4, 5, 6], [7, 8, 0]]


def main():
    sp = SlidingBlock([[8, 3, 5], [1, 0, 6], [4, 7, 2]])
    #print(dp.actions(dp))
    #dp.result(dp.state, 3)
    print(Trial_Error(sp))


main()
