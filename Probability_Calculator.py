import random

class Hat:
    def __init__(self, **kwargs):
        # Initialize the hat with the given balls
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)

    def draw(self, num_balls):
        # If the number of balls to draw exceeds the available balls, return all balls
        if num_balls >= len(self.contents):
            return self.contents[:]
        
        # Randomly draw balls from the hat
        drawn_balls = random.sample(self.contents, num_balls)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    success_count = 0

    for _ in range(num_experiments):
        # Make a copy of the hat to avoid modifying the original
        temp_hat = Hat(**{color: hat.contents.count(color) for color in set(hat.contents)})
        
        # Perform a draw
        drawn_balls = temp_hat.draw(num_balls_drawn)
        
        # Count the occurrences of each color in the drawn balls
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        
        # Check if the drawn balls meet the expected criteria
        success = True
        for color, count in expected_balls.items():
            if drawn_counts.get(color, 0) < count:
                success = False
                break
        
        if success:
            success_count += 1

    # Calculate and return the probability
    return success_count / num_experiments

# Example usage
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat,
                         expected_balls={"red": 1, "green": 2},
                         num_balls_drawn=4,
                         num_experiments=2000)
print(probability)
