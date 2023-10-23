import turtle
import pandas

screen = turtle.Screen()
screen.title("ETH States game")
image = "photo_.gif.gif"
screen.addshape(image)

turtle.shape(image)
""" __author__ = "Abenezer Alemayhu"   
    __Date__="10/22/2023"

"""


data = pandas.read_csv("10_states.csv")
states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 10:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/10 State", prompt="What another state name? ")
    if answer_state == "Exit":
        missing_state = []
        for state in states:
            if state not in guessed_states:
                missing_state.append(state)
        new_data = pandas.DataFrame(missing_state)
        new_data.to_csv("State_missing.csv")
        break
    if answer_state in states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]

        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# def get_mouse_click_coordinate(x,y):
""" Used this Function to find the coordinate of the states"""
#     print(x,y)
#
#
#
#
# turtle.onscreenclick(get_mouse_click_coordenat)
# turtle.mainloop()
screen.exitonclick()
