# Snake-Game
This project is a simple implementation of the classic Snake game using Python's turtle graphics library. The player controls the snake, which grows longer as it eats fruit (red squares). The goal is to achieve the highest score without the snake colliding with itself or the game boundaries.

## Features
1.Dynamic Gameplay: The snake grows longer as it eats fruit.

2.Score Tracking: The score updates in real time and is displayed on the screen.

3.Game Over Screen: Displays the final score when the game ends.

4.Keyboard Controls: Use arrow keys to control the direction of the snake.

## Requirements
- Python 3.x
- Turtle module (included in Python's standard library)


## How to Play

1.Objective: Eat as many fruits as possible without colliding with the game boundary or yourself. The game ends when a collision occurs.

2.Controls:
 Use the arrow keys to control the snake's movement:
 - Up Arrow: Move up
 - Down Arrow: Move down
 - Left Arrow: Move left
 - Right Arrow: Move right

3.Scoring:
- Each fruit eaten increases the score by 1.
- The snake grows longer with each fruit consumed.

4.Game Over:
- The game ends if the snake collides with the boundary or any part of its body.
- The game ends, the player's final score is displayed.

## Code Features

## Game Elements:
1. Game Screen:
- A bordered play area of size 600x500 pixels with a black background.

2. Snake:
- Initially a single green block that grows as it eats fruits.

3. Fruit:
- A randomly placed white square that repositions each time the snake eats it.

4.Score Display:
- Shows the player's current score at the top of the screen.

## Functional Highlights:
1. Keyboard Control:
- The snake responds to arrow key inputs for direction changes.
2. Collision Detection:
- Detects collision with the boundary or the snake's own body to end the game.
3. Dynamic Snake Growth:
- Adds new red blocks to the snake's body each time it eats a fruit.
4. Adjustable Speed:
- The game speeds up slightly after each fruit is eaten.

## Troubleshooting
1. Turtle Not Found:
If Python can't find the turtle module, ensure you have Python 3.x installed correctly.

2. Script Doesn't Run:
Ensure Python is installed and added to the system's PATH.
## Output
![image](https://github.com/user-attachments/assets/aec67e02-a89f-4f10-ab7b-feb355c8339c)
