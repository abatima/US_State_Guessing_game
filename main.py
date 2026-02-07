import turtle
import pandas

screen = turtle.Screen()
screen.title("US States Game")
background_image = "blank_states_img.gif"
correct_counter = 0
guessed_states = []
game_is_on = True
screen.addshape(background_image)
turtle.shape(background_image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{correct_counter}/50 Guess the state", prompt="What's the name?").title()

    if answer_state == "exit".title():
        missing_states = list(set(all_states) - set(guessed_states))
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")
        print(missing_states)
        break

    if answer_state in data.state.values and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        correct_counter += 1

        #drawing
        guessed_state_row = data[data.state == answer_state]
        x_cor = guessed_state_row.x.item()
        y_cor = guessed_state_row.y.item()
        t = turtle.Turtle()
        t.hideturtle()
        t.teleport(x_cor, y_cor)
        t.write(answer_state)
