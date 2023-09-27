import pandas
from turtle import Screen, Turtle

turtle = Turtle()
screen = Screen()
screen.title("US States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
guess = Turtle()
guess.penup()
guess.hideturtle()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].tolist()

correct_guesses = []
answer_state = screen.textinput(title="Guess the State",
                                prompt="Guess the first state")

while len(correct_guesses) < 50:
    if answer_state == "Exit":
        missing_states = []
        for state in states_list:
            if state not in correct_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    for state in states_list:
        if answer_state.lower() == state.lower():
            # The line below makes sure the answer_state match the actual state name in dataframe
            answer_state = state
            correct_guesses.append(answer_state)
            state_name = data[data.state == answer_state].state.iloc[0]
            x = int(data[data.state == answer_state].x.iloc[0])
            y = int(data[data.state == answer_state].y.iloc[0])
            guess.goto(x, y)
            guess.write(f"{state_name}")

    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(states_list)} States Correct",
                                    prompt="What's another state's name?")

