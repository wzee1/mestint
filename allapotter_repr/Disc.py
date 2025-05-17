from search import Problem, Trial_Error


class Disc(Problem):
    def __init__(self, initial_state):
        #self.state = initial_state
        super().__init__(initial_state)


    def actions(self, state):
        return [i for i in range(2, len(state) + 1)]


    def result(self, state, action):
        new_state = state
        flipped_sublist = list(reversed(state[:action]))
        new_state[:action] = flipped_sublist

        return new_state


    def goal_test(self, state):
        return state == sorted(state)


def main():
    #dp = Disc([6, 7, 3, 2, 8, 5, 4, 1])
    dp = Disc([3, 2, 4, 1, 5])
    #print(dp.actions(dp))
    #dp.result(dp.state, 3)
    print(Trial_Error(dp))


main()
