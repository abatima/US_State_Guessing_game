from turtle import Turtle


class StateWriter(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()

    def write_state(self, name, coordinates):
        self.teleport(*coordinates)
        self.write(name)