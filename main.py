from turtle import Turtle, Screen
import random

is_race_on = False
all_turtles = []
screen = Screen()
screen.setup(500,400)
user_bet = screen.textinput(title = "Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]

for turtles in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.goto(x= -230, y = (-100 + (turtles * 50)))
    new_turtle.color(colors[turtles])
    all_turtles.append(new_turtle)
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if user_bet == winning_color:
                print(f"Congrats!{winning_color} is the winner!")
            else:
                print(f"Ooooh, winning colos ir {winning_color}. Better luck next time!")
        distance_move = random.randint(0, 10)
        turtle.forward(distance_move)


























screen.exitonclick()