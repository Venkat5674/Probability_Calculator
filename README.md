# Probability Calculator

## Project Overview
The Probability Calculator is a Python project that simulates random draws from a hat to estimate probabilities for various scenarios.

## Features
- Supports creating hats with different colored balls.
- Simulates random draws without replacement.
- Estimates probabilities through repeated experiments.

## Example Usage
```python
from probability_calculator import Hat, experiment

hat = Hat(blue=5, red=4, green=2)
probability = experiment(
    hat=hat,
    expected_balls={"red": 1, "green": 2},
    num_balls_drawn=4,
    num_experiments=2000
)
print(probability)
```

## Example Output
```
0.356
```

## How to Run
1. Create a hat using the `Hat` class, specifying the number of balls of each color.
2. Use the `experiment` function to estimate probabilities for specific scenarios.
3. Run multiple experiments for more accurate results.
