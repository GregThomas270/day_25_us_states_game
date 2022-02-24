from turtle import Turtle


class StateObject(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.hideturtle()

    def write_guess(self, player_guess):
        self.write(player_guess, False, "center", ("arial", 8, "normal"))

    def go_to_state(self, pos_x_loc, pos_y_loc):
        print(pos_x_loc)
        self.goto(pos_x_loc, pos_y_loc)
