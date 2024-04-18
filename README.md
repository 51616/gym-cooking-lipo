# Multi-recipe Overcooked used in LIPO

A variant of https://github.com/DavidRother/cooking_zoo used in LIPO.

### Installation
```bash
pip install gym-cooking-lipo
```
---
### Examples

#### Environment creation
```python
from gym_cooking.environment.game.game import Game
from gym_cooking.environment import cooking_zoo

n_agents = 2
max_steps = 100
render = False

level = "full_divider_salad_4"
seed = 1
record = False
max_num_timesteps = 1000
recipes = [
    "LettuceSalad",
    "TomatoSalad",
    "TomatoLettuceSalad",
    "TomatoCarrotSalad",
    "ChoppedCarrot",
    "ChoppedOnion",
]

env = parallel_env = cooking_zoo.parallel_env(
    level=level,
    num_agents=n_agents,
    record=record,
    max_steps=max_num_timesteps,
    recipes=recipes,
    obs_spaces=["dense"],
)
obs = env.reset()
print(obs)
```

#### Human-AI gameplay
```python
from gym_cooking.environment.game.game import Game
from gym_cooking.environment import cooking_zoo

n_agents = 2
num_humans = 1
max_steps = 100
render = False

level = "full_divider_salad_4"  # 'open_room_salad_easy'
seed = 1
record = False
max_num_timesteps = 1000
recipes = [
    "LettuceSalad",
    "TomatoSalad",
    "ChoppedCarrot",
    "ChoppedOnion",
    "TomatoLettuceSalad",
    "TomatoCarrotSalad",
]

parallel_env = cooking_zoo.parallel_env(
    level=level,
    num_agents=n_agents,
    record=record,
    max_steps=max_num_timesteps,
    recipes=recipes,
    obs_spaces=["dense"],
    interact_reward=0.5,
    progress_reward=1.0,
    complete_reward=10.0,
    step_cost=0.05,
)

action_spaces = parallel_env.action_spaces


class CookingAgent:

    def __init__(self, action_space):
        self.action_space = action_space

    def get_action(self, observation) -> int:
        return self.action_space.sample()


player_2_action_space = action_spaces["player_1"]
cooking_agent = CookingAgent(player_2_action_space)
game = Game(parallel_env, num_humans, [cooking_agent], max_steps, render=False)
store = game.on_execute()

print("done")
```

#### Single-player gameplay
```python
from gym_cooking.environment.game.game import Game
from gym_cooking.environment import cooking_zoo


n_agents = 1
num_humans = 1
max_steps = 100
render = False

level = "open_room_blender"
seed = 1
record = False
max_num_timesteps = 100
recipes = ["ChoppedCarrot", "LettuceSalad"]

parallel_env = cooking_zoo.parallel_env(
    level=level,
    num_agents=n_agents,
    record=record,
    max_steps=max_num_timesteps,
    recipes=recipes,
    obs_spaces=["dense"],
)

game = Game(parallel_env, num_humans, [], max_steps)
store = game.on_execute()

print("done")
```