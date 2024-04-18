```python
from gym_cooking.environment.game.game import Game
from gym_cooking.environment import cooking_zoo

n_agents = 1
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