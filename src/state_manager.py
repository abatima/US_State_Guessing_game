import pandas

class StateManager:
    def __init__(self):
        self.data = pandas.read_csv("src/50_states.csv")
        self.all_states = self.data.state.to_list()
        self.guessed_states = []

    def check_guess(self, guess):
        if guess in self.data.state.values and guess not in self.guessed_states:
            self.guessed_states.append(guess)

    def get_coordinates(self, state_name):
        guessed_state_row = self.data[self.data.state == state_name]
        return int(guessed_state_row.x.item()), int(guessed_state_row.y.item())

    def save_missing_states(self):
        missing_states = list(set(self.all_states) - set(self.guessed_states))
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("missing_states.csv")