from pathlib import Path

import gymnasium as gym

from common import Params
from plotting import plot_q_values_map
from q_learning import Qlearning


params = Params(
    total_episodes=5_000,
    learning_rate=0.3,
    gamma=0.95,
    epsilon=0.1,
    seed=63,
    is_slippery=False,
    map_size=(4, 12),
    savefig_folder=Path("figures"),
)

if __name__ == "__main__":
    avg_rewards = []
    avg_steps = []
    env = gym.make(
        "CliffWalking-v0",
        is_slippery=params.is_slippery,
        render_mode="rgb_array",
    )

    env.action_space.seed(params.seed)
    learner = Qlearning(
        learning_rate=params.learning_rate,
        gamma=params.gamma,
        state_size=env.observation_space.n,
        action_size=env.action_space.n,
        epsilon=params.epsilon,
    )
    total_rewards, total_steps = learner.run_environment(
        env=env, num_episodes=params.total_episodes
    )
    plot_q_values_map(learner.qtable, env, params.map_size[0], params.map_size[1])
