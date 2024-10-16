# The Indian State Game
from turtle import *
import pandas
screen = Screen()
image = 'indian_map.gif'
screen.addshape(image)
screen.setup(width=713, height=837)
tim = Turtle(image)



data = pandas.read_csv('indian-states.csv')
all_states = data.state.to_list()



game_is_on = True
while game_is_on:
    answer = textinput(title='Guess', prompt='Guess the states name').title()
    if answer in all_states:
        state_data = data[data.state == answer]
        state = Turtle()
        state.penup()
        state.hideturtle()
        state.goto(int(state_data.x), int(state_data.y))
        state.write(answer)





def mouse_click_cor(x, y):
    print(x, y)

tim.onclick(mouse_click_cor)

screen.mainloop()