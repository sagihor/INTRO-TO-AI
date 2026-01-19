from pathlib import Path

import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

from common import Params

sns.set_theme()

params = Params(
    total_episodes=2000,
    learning_rate=0.5,
    gamma=0.95,
    epsilon=0.1,
    seed=63,
    is_slippery=False,
    map_size=(4, 12),
    savefig_folder=Path("figures"),
)


def qtable_directions_map(qtable: np.ndarray, n_rows: int, n_cols: int):
    """Get the best learned action & map it to arrows."""
    print(qtable)
    qtable_val_max = qtable.max(axis=1).reshape(n_rows, n_cols)
    qtable_best_action = np.argmax(qtable, axis=1).reshape(n_rows, n_cols)
    directions = {0: "↑", 1: "→", 2: "↓", 3: "←"}
    qtable_directions = np.empty(qtable_best_action.flatten().shape, dtype=str)
    eps = np.finfo(float).eps  # Minimum float number on the machine
    for idx, val in enumerate(qtable_best_action.flatten()):
        if qtable_val_max.flatten()[idx] != 0:  # eps:
            # Assign an arrow only if a minimal Q-value has been learned as best action
            # otherwise since 0 is a direction, it also gets mapped on the tiles where
            # it didn't actually learn anything
            qtable_directions[idx] = directions[val]

    qtable_directions = qtable_directions.reshape(n_rows, n_cols)
    return qtable_val_max, qtable_directions


def plot_q_values_map(qtable, env, n_rows, n_cols):
    """Plot the last frame of the simulation and the policy learned."""
    qtable_val_max, qtable_directions = qtable_directions_map(qtable, n_rows, n_cols)

    # Plot the last frame
    fig, ax = plt.subplots(nrows=1, ncols=2, figsize=(15, 5))
    ax[0].imshow(env.render())
    ax[0].axis("off")
    ax[0].set_title("Last frame")

    # Plot the policy
    sns.heatmap(
        qtable_val_max,
        annot=qtable_directions,
        fmt="",
        ax=ax[1],
        cmap=sns.color_palette("Blues", as_cmap=True),
        linewidths=0.7,
        linecolor="black",
        xticklabels=[],
        yticklabels=[],
        annot_kws={"fontsize": "xx-large"},
    ).set(title="Learned Q-values\nArrows represent best action")
    for _, spine in ax[1].spines.items():
        spine.set_visible(True)
        spine.set_linewidth(0.7)
        spine.set_color("black")
    img_title = f"frozenlake_q_values_{n_rows}x{n_cols}.png"
    fig.savefig(params.savefig_folder / img_title, bbox_inches="tight")
    plt.show()
