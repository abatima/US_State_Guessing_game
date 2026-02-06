import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
background_image = "blank_states_img.gif"
correct_counter = 0
game_is_on = True
screen.addshape(background_image)
turtle.shape(background_image)

data = pandas.read_csv("50_states.csv")

while game_is_on:
    guessed_state = screen.textinput(title=f"{correct_counter}/50 Guess the state", prompt="What's the name?").title()

    for state in data.state:
        if state == guessed_state:
            correct_counter += 1


    print(guessed_state)
turtle.mainloop()