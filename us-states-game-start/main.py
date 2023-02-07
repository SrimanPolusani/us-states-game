from turtle import Turtle, Screen
import pandas
from states_name_display import States_Name_Display
from detecting_repeated_answers import detect_repeated_ans

turtle = Turtle()
screen = Screen()
screen.title("U.S STATES GAME")
image = "./blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writing_turtle = States_Name_Display()


def take_input(numb_of_correct_ans, numb_of_total_sates):
    answer = screen.textinput(title=f"{numb_of_correct_ans}/{numb_of_total_sates} are correct",
                              prompt="Enter a state name?").lower()
    return answer


states_data = pandas.read_csv("./50_states.csv")
all_states_lst = states_data.state.to_list()
all_x_values = states_data.x.to_list()
all_y_values = states_data.y.to_list()

no_of_correct_ans = 0
input_ans_lst = []
game_is_on = True

while game_is_on:
    answered_state = take_input(no_of_correct_ans, 50)
    for state in all_states_lst:
        if state.lower() == answered_state:
            repeated = detect_repeated_ans(input_ans_lst, answered_state)
            if repeated:
                break
            elif repeated is None:
                x_y_values_index = all_states_lst.index(state)
                x_value = all_x_values[x_y_values_index]
                y_value = all_y_values[x_y_values_index]
                input_ans_lst.append(answered_state)
                writing_turtle.write(x_value, y_value, state)
                no_of_correct_ans += 1
                total_no_of_states = len(all_states_lst)
                screen.title(f"{no_of_correct_ans}/{total_no_of_states} are correct")
                at_least_one_element = True

    if len(input_ans_lst) == 50:
        print("YOU WON THE GAME!")
        game_is_on = False

screen.exitonclick()
