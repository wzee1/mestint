import random

from search import Problem, Trial_Error


def change_value(value):
    if value == 0: return 1
    else: return 0

class LightBulb(Problem):
    def __init__(self, initial_state):
        #self.state = initial_state
        super().__init__(initial_state)


    def actions(self, state):
        return [
            [0, 0], [0, 1], [0, 2],
            [1, 0], [1, 1], [1, 2],
            [2, 0], [2, 1], [2, 2],
        ]


    def result(self, state, action):
        new_state = [row for row in state]

        bulb = change_value(state[action[0]][action[1]])
        new_state[action[0]][action[1]] = bulb

        try:
            bulb_up = change_value(state[action[0] - 1][action[1]])
            new_state[action[0] - 1][action[1]] = bulb_up
        except:
            pass

        try:
            bulb_down = change_value(state[action[0] + 1][action[1]])
            new_state[action[0] + 1][action[1]] = bulb_down
        except:
            pass

        try:
            bulb_left = change_value(state[action[0]][action[1] - 1])
            new_state[action[0]][action[1] - 1] = bulb_left
        except:
            pass

        try:
            bulb_right = change_value(state[action[0]][action[1] + 1])
            new_state[action[0]][action[1] + 1] = bulb_right
        except:
            pass

        return new_state


    def goal_test(self, state):
        return state == [[1, 1, 1], [1, 1, 1], [1, 1, 1]]


def main():
    # nagyon sok idobe fog telni valszeg
    lp = LightBulb([
        [random.randint(0, 1) for i in range(3)] for j in range(3)
    ])
    print(Trial_Error(lp))


main()
