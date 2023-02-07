# <---- Import Statements ---->
from turtle import Turtle, Screen
import pandas
from states_name_display import States_Name_Display
from repeated_answers import detect_repeated_ans

# <---- Constants ---->
TOTAL_STATES = 50

# <---- Initializing Turtle Object and the Screen ---->
turtle = Turtle()
screen = Screen()
screen.title("U.S STATES GAME")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writing_turtle = States_Name_Display()


# <---- Dialog Box Function ---->
def dialog_box(correct_ans):
    """"
    This function takes no of correct answers and total no of states as augments, displays dialog box and returns received input from the user
    """
    answer = screen.textinput(title=f"{correct_ans}/{TOTAL_STATES} are correct",
                              prompt="Enter a state name?").lower()
    return answer


# 50_states.csv states and their positions on the image black_states_img.gif
states_data = pandas.read_csv("50_states.csv")

# Converting data into a lists
states_lst = states_data.state.to_list()
x_values = states_data.x.to_list()
y_values = states_data.y.to_list()

count_correct_ans = 0
input_ans_lst = []
game_is_on = True

while game_is_on:

    # Taking answer from the user
    answer = dialog_box(count_correct_ans)
    for state in states_lst:
        if state.lower() == answer:

            # Checking if it's a repeated answer
            repeated = detect_repeated_ans(input_ans_lst, answer)
            if repeated:
                break
            elif repeated is None:
                state_index = states_lst.index(state)
                x_value = x_values[state_index]
                y_value = y_values[state_index]
                input_ans_lst.append(answer)
                writing_turtle.write(x_value, y_value, state)
                count_correct_ans += 1

    if len(input_ans_lst) == 50:
        print("YOU WON THE GAME!")
        print("Game Over")
        game_is_on = False

screen.exitonclick()
