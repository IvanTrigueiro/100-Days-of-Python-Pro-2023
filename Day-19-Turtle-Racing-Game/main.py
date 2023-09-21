from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

screen.setup(width=500, height=400)
screen.textinput(title="Make your bet!", prompt="Which turtle will win the race? Enter a color: ")


screen.exitonclick()