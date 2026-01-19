from typing import Tuple

import numpy as np
import math


class ValueIteration:

    def __init__(
        self,
        theta=0.0001,
        discount_factor=1.0,
    ):
        self.theta = theta
        self.discount_factor = discount_factor


    def calculate_q_values(
        self, current_capital: int, value_function: np.ndarray, rewards: np.ndarray
    ) -> np.ndarray:
        """
        Helper function to calculate the value for all action in a given state.

        Args:
            current_capital: The gambler’s capital. Integer. (state)
            value_function: The vector that contains values at each state. (the recursive value function)
            rewards: The reward vector. (the immediate reward according to the gambler's problem definition)

        Returns:
            A vector containing the expected value of each action in THIS state.
            Its length equals to the number of actions.
        """
        if current_capital == 0 or current_capital == 100:  # no actions to do
            return np.array([])

        num_actions = min(current_capital, 100 - current_capital)  # can bet 1...current_capital or the sum leads to 100
        value_vect = np.zeros(num_actions+1, dtype=float)

        # all the possible gains/loss probabilities
        win_p = 1/6
        loss_p = 5/12
        loss_half_p = 5/12

        for action in range(1, num_actions + 1):  # for each possible bet
            win_state = current_capital + action
            lose_state = current_capital - action
            half_state = current_capital - math.ceil(action / 2)
            immediate = 1 if win_state == 100 else 0.0
            # win_state collects immediate reward if reaches 100
            # in loss and loss half there is no reward at all
            value_vect[action] = (
                    win_p * (immediate + self.discount_factor * value_function[win_state]) +
                    loss_p * (0.0 + self.discount_factor * value_function[lose_state]) +
                    loss_half_p * (0.0 + self.discount_factor * value_function[half_state])
            )
        return value_vect

    def value_iteration_for_gamblers(self) -> Tuple[np.ndarray, np.ndarray]:
        """ """
        policy = np.zeros(101, dtype=int)
        rewards = np.zeros(101, dtype=int)
        rewards[100] = 1  # goal reward
        V = np.zeros(101, dtype=float)

        while True:
            delta: float = 0.0
            for state in range(1, 100):
                q_values = self.calculate_q_values(state, V, rewards)
                best_value = np.max(q_values)
                delta = max(delta, abs(best_value - V[state]))
                V[state] = best_value
            if delta < self.theta:  # reached convergences
                break
        # update policy
        for s in range(1, 100):
            q = self.calculate_q_values(s, value_function=V, rewards=rewards)
            policy[s] = int(np.argmax(q)) + 1

        return policy, V