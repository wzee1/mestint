import numpy as np
import random

class QLearningAgent:
    def __init__(self, n_states, n_actions, learning_rate):
        self.n_states = n_states
        self.n_actions = n_actions
        self.learning_rate = learning_rate

        # minden sor egy allapotot reprezental, minden oszlop egy akciot
        # minden akciohoz rendelunk egy jutalomerteket
        self.q_table = np.zeros((n_states, n_actions))

    def act(self, state, epsilon):
        # 0 es 1 kozotti szam, hogy eldontsuk hogy exploit vagy explore lesz
        random_val = random.uniform(0, 1)

        # epsilon: esely arra, hogy explore-ol vagy exploit-ol
        if epsilon > random_val:
            # explore
            return random.randint(0, self.n_actions - 1)
        # exploit
        return np.argmax(self.q_table[state])

    def learn(self, state, action, reward, new_state, gamma):
        # uj q-ertek becsles kiszamolasa
        new_estimate = reward + gamma * max(self.q_table[new_state])

        self.q_table[state][action] += self.learning_rate * (new_estimate - self.q_table[state][action])