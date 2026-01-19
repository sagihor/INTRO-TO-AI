import math
import random
from typing import List, Tuple

import gymnasium as gym
import numpy as np

SEED = 63

# Set the seed
rng = np.random.default_rng(SEED)


class Qlearning:
    def __init__(
        self,
        learning_rate: float,
        gamma: float,
        state_size: int,
        action_size: int,
        epsilon: float,
    ):
        self.state_size = state_size
        self.action_space_size = action_size
        self.learning_rate = learning_rate
        self.gamma = gamma
        self.epsilon = epsilon
        self.qtable = np.zeros((state_size, action_size))

    def update(self, state: int, action: int, reward: float, new_state: int):
        """In this function you need to implement the update of the Q-table.
        Args:
            state (int): Current state
            action (int): Action taken in the current state
            reward (float): Reward received after taking the action
            new_state (int): New state reached after taking the action.
        """
        best_move = self.qtable[new_state].max()
        self.qtable[state, action] =+ (1 - self.learning_rate)*self.qtable[state, action] + self.learning_rate * (reward + self.gamma * best_move)

    def reset_qtable(self):
        """Reset the Q-table."""
        self.qtable = np.zeros((self.state_size, self.action_space_size))

    def select_epsilon_greedy_action(self, state: int) -> int:
        """Select an action from the Q-table."""
        row = self.qtable[state]
        best_move = int(np.argmax(row))
        if np.random.rand() > self.epsilon:  # chose the best move (Exploitation)
            return best_move
        else:  # chose other than the best (Exploration)
            other_moves = np.delete(np.arange(self.qtable.shape[1]), best_move)
            return np.random.choice(other_moves)

    def train_episode(self, env: gym.Env) -> Tuple[float, int]:
        """Train the agent for a single episode.

        Notice an episode is a single run of the environment until the agent reaches a terminal state
        (the return value of env.step() is True for the third and fourth elements)


        :param env: The environment to train the agent on.
        :return: the cumulative reward obtained during the episode and the number of steps executed in the episode.
        """
        env.reset()
        steps = 0
        cumulative_reward = 0
        terminated = False
        curr_state = 36  # start state
        while not terminated:  # as long we didn't reach goal
            action = self.select_epsilon_greedy_action(curr_state)
            new_state, reward, terminated, _, _ = env.step(action)
            self.update(curr_state, action, float(reward), new_state)
            curr_state = new_state
            cumulative_reward += reward
            steps = steps + 1
        return cumulative_reward, steps

    def run_environment(
        self, env: gym.Env, num_episodes: int
    ) -> Tuple[List[float], List[int]]:
        """
        Run the environment with the given policy.

        Args:
            env (gym.Env): The environment to train the agent on.
            num_episodes (int): The number of episodes to run the environment.

        Returns:
            A tuple (total_rewards, total_steps).
        """
        rewards_list = []
        steps_list = []
        for i in range(num_episodes):
            cum_reward, steps = self.train_episode(env)
            rewards_list.append(cum_reward)
            steps_list.append(steps)
        return rewards_list, steps_list

