import turtle
import random
import time

# Create a screen window for the game
screen = turtle.Screen()
screen.title("SNAKE GAME")  # Set the title of the game window
screen.setup(width=700, height=700)  # Set the window size
screen.tracer(0)  # Disable automatic screen updates for better performance
screen.bgcolor("#1d1d1d")  # Set the background color to dark gray

# Draw the game border
border = turtle.Turtle()  # Create a new turtle for drawing the border
border.speed(5)  # Set the drawing speed
border.pensize(4)  # Set the border thickness
border.penup()  # Lift the pen to move without drawing
border.goto(-310, 250)  # Position the pen at the starting point
border.pendown()  # Lower the pen to start drawing
border.color("red")  # Set the border color to red

# Draw the rectangular boundary
border.forward(600)  # Draw top border
border.right(90)
border.forward(500)  # Draw right border
border.right(90)
border.forward(600)  # Draw bottom border
border.right(90)
border.forward(500)  # Draw left border
border.penup()
border.hideturtle()  # Hide the turtle cursor

# Initialize score and delay variables
score = 0
delay = 0.1

# Create the snake turtle
snake = turtle.Turtle()
snake.speed(0)  # Set the speed to fastest
snake.shape("square")
snake.color("green")
snake.penup()
snake.goto(0, 0)
snake.direction = 'stop'  # Initial direction of the snake is stopped

# Create the food turtle
fruit = turtle.Turtle()
fruit.speed(0)
fruit.shape("square")
fruit.color("white")
fruit.penup()
fruit.goto(30, 30)

# List to keep track of snake's body segments
old_fruit = []

# Create the scoring display
scoring = turtle.Turtle()
scoring.speed(0)
scoring.color("white")
scoring.penup()
scoring.hideturtle()
scoring.goto(0, 300)
scoring.write("Score: 0", align="center", font=("Courier", 24, "bold"))

# Functions to control the snake's direction
def snake_go_up():
    if snake.direction != "down":  # Prevent the snake from moving in the opposite direction
        snake.direction = "up"

def snake_go_down():
    if snake.direction != "up":
        snake.direction = "down"

def snake_go_left():
    if snake.direction != "right":
        snake.direction = "left"

def snake_go_right():
    if snake.direction != "left":
        snake.direction = "right"

# Function to move the snake based on its current direction
def snake_move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

# Keyboard bindings to control the snake using arrow keys
screen.listen()
screen.onkeypress(snake_go_up, "Up")
screen.onkeypress(snake_go_down, "Down")
screen.onkeypress(snake_go_left, "Left")
screen.onkeypress(snake_go_right, "Right")

# Main game loop
while True:
    screen.update()  # Refresh the screen

    # Check for collision between snake and food
    if snake.distance(fruit) < 20:
        # Move the fruit to a random position within the game area
        x = random.randint(-290, 270)
        y = random.randint(-240, 240)
        fruit.goto(x, y)

        # Increase the score and speed up the game slightly
        score += 1
        scoring.clear()
        scoring.write("Score: {}".format(score), align="center", font=("Courier", 24, "bold"))
        delay -= 0.001  # Decrease delay to make the game faster

        # Add a new segment to the snake's body
        new_fruit = turtle.Turtle()
        new_fruit.speed(0)
        new_fruit.shape("square")
        new_fruit.color("red")
        new_fruit.penup()
        old_fruit.append(new_fruit)

    # Move the snake's body segments
    for index in range(len(old_fruit) - 1, 0, -1):
        a = old_fruit[index - 1].xcor()
        b = old_fruit[index - 1].ycor()
        old_fruit[index].goto(a, b)

    # Move the first segment to follow the snake's head
    if len(old_fruit) > 0:
        a = snake.xcor()
        b = snake.ycor()
        old_fruit[0].goto(a, b)

    # Move the snake forward
    snake_move()

    # Check if the snake collides with the border
    if snake.xcor() > 280 or snake.xcor() < -300 or snake.ycor() > 240 or snake.ycor() < -240:
        time.sleep(1)
        screen.clear()  # Clear the screen on game over
        screen.bgcolor("turquoise")
        scoring.goto(0, 0)
        scoring.write("    Game Over \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
        break

    # Check if the snake collides with itself
    for food in old_fruit:
        if food.distance(snake) < 20:
            time.sleep(1)
            screen.clear()
            screen.bgcolor("turquoise")
            scoring.goto(0, 0)
            scoring.write("    Game Over \n Your Score is {}".format(score), align="center", font=("Courier", 30, "bold"))
            break

    time.sleep(delay)  # Control the speed of the game

turtle.Terminator()  # Properly close the Turtle graphics window
