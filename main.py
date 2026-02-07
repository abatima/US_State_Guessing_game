import turtle
from src.state_writer import StateWriter
from src.state_manager import StateManager

screen = turtle.Screen()
screen.title("US States Game")
background_image = "src/blank_states_img.gif"
screen.addshape(background_image)
turtle.shape(background_image)


writer = StateWriter()
manager = StateManager()

while len(manager.guessed_states) < 50:

    answer_state = screen.textinput(title=f"{len(manager.guessed_states)}/50 Guess the state", prompt="What's the name?").title()

    if answer_state == "exit".title():
        manager.save_missing_states()
        break

    if answer_state in manager.all_states and answer_state not in manager.guessed_states:
        manager.guessed_states.append(answer_state)
        coordinates = manager.get_coordinates(answer_state)
        writer.write_state(answer_state, coordinates)
