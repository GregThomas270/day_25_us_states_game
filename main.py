import pandas as pd
import turtle
from name_class import StateObject
# guess = input("Guess a state: ")
# # This line looks for the row that coincides with the player's guess
# coordinate = states_list[states_list.state == guess]
# # These two pull the data from the row found above in the columns "x" and "y"
# x_cor = coordinate.x
# y_cor = coordinate.y
states_guessed = []

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

states_data = pd.read_csv("50_states.csv")
states_list_data = states_data.state
states_list = states_list_data.tolist()

# Prompt player for guess
player_guess = screen.textinput("Guess a State", "Enter the name of a state").title()
game_over = False
while not game_over:
    # Check if guess in either list
    if player_guess in states_list and player_guess not in states_guessed:
        # Add guess to states_guessed list
        states_guessed.append(player_guess)
        # Retrieve coordinates for guess and store as variables
        coordinate = states_data[states_data.state == player_guess]
        pos_x = int(coordinate.x)
        pos_y = int(coordinate.y)
        # Create object to print guess on screen
        guess_object = StateObject()
        guess_object.go_to_state(pos_x, pos_y)
        guess_object.write_guess(player_guess)
        if len(states_guessed) == 50:
            game_over = True
    else:
        player_guess = screen.textinput(f"{len(states_guessed)} / 50 States guessed", "Enter the name of a state").title()


screen.mainloop()
