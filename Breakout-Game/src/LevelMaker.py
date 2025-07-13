import random
import pygame
import math
from src.Brick import Brick

# Patterns
NONE = 1
SINGLE_PYRAMID = 2
MULTI_PYRAMID = 3 
DOTTED = 4
GRADIENT = 5
CHECKERBOARD = 7
SPIKES = 8

# Brick Styles
SOLID = 1            # All colors the same in this row
ALTERNATE = 2        # Alternate colors
SKIP = 3             # Skip every other brick
NONE = 4             # No block in this row
RAINBOW = 5          # New rainbow pattern

class LevelMaker:
    def __init__(self):
        pass

    @classmethod
    def CreateMap(cls, level):
        bricks = []

        # Define difficulty parameters based on level
        num_rows = min(7, level)  # Increase rows with level, max at 7
        num_cols = min(21, 7 + level)  # Increase columns with level, max at 21

        # Set tier and color based on the level
        if level <= 3:
            highest_tier = 0  # All bricks are one-hit breakable
            highest_color = 1
        else:
            highest_tier = min(3, (level - 4) // 2)  # Gradually increase the tier
            if highest_tier > 3:
                highest_tier = 3
            highest_color = min(5, level % 5 + 3)  # Max color based on level

        # Updated row patterns including new ones
        row_patterns = [
            SOLID, ALTERNATE, SKIP, RAINBOW, DOTTED, GRADIENT, CHECKERBOARD, SPIKES
        ]

        for y in range(num_rows):
            row_pattern = random.choice(row_patterns)
            skip_flag = random.choice([True, False])
            alternate_flag = random.choice([True, False])

            for x in range(num_cols):
                b = Brick(x * 96 + 24 + (13 - num_cols) * 48, y * 48)

                # Set brick properties
                b.tier = highest_tier
                b.color = random.randint(1, highest_color)

                # Apply the chosen row pattern
                if row_pattern == SOLID:
                    b.color = random.randint(1, highest_color)
                elif row_pattern == ALTERNATE:
                    if alternate_flag:
                        b.color = random.randint(1, highest_color)
                    alternate_flag = not alternate_flag
                elif row_pattern == SKIP:
                    if skip_flag:
                        skip_flag = not skip_flag
                        continue
                    else:
                        skip_flag = not skip_flag
                elif row_pattern == RAINBOW:
                    b.color = (y % 5) + 1  # Cycle through colors
                elif row_pattern == DOTTED:
                    if x % 3 == 0:
                        b.color = random.randint(1, highest_color)
                    else:
                        continue  # Skip this brick
                elif row_pattern == GRADIENT:
                    b.color = (x % highest_color) + 1  # Gradual color change

                elif row_pattern == CHECKERBOARD:
                    if (x + y) % 2 == 0:
                        b.color = random.randint(1, highest_color)
                elif row_pattern == SPIKES:
                    if x >= (num_cols // 2) - (y % 2) and x <= (num_cols // 2) + (y % 2):
                        b.color = random.randint(1, highest_color)

                bricks.append(b)

        if len(bricks) == 0:
            return LevelMaker.CreateMap(level)

        return bricks
