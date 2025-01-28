from tkinter import *
import pandas as pd
from random import randint, choice

BACKGROUND_COLOR = "#B1DDC6"

current_card ={}
word_choice = ""

#-----------------------read csv--------------------#
global word_dict

#french_words is csv file with 2 columns

try:
    # check if file is available
    french_df = pd.read_csv("words_to_learn.csv")  # words_to_learn csv to df

except FileNotFoundError:
    # if not available, create file
    french_df = pd.read_csv("data/french_words.csv")
    word_dict = french_df.to_dict(orient="records")
    # print(word_dict)
else:
    word_dict = french_df.to_dict(orient="records")  # french_df becomes active list

#word_dict is a list of dictionary
#[{'French': 'partie', 'English': 'part'}, {'French': 'histoire', 'English': 'history'}]

#-----------------------functions--------------------#
def pick_word():
    global current_card, timer, word_dict
    window.after_cancel(timer)
    current_card = choice(word_dict)
    word_choice = current_card["French"]
    canvas.itemconfig(card_title, text="French", fill = "black")
    canvas.itemconfig(card_word, text=word_choice, fill = "black")
    canvas.itemconfig(card_face, image=img_card_front)
    timer = window.after(3000, flip_card)

#-----------------------functions--------------------#
def flip_card():
    global current_card
    canvas.itemconfig(card_face, image = img_card_back)
    eng_word = current_card["English"]
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=eng_word, fill="white")

def tick():
    global word_dict

    word_dict.remove(current_card)
    #check if words_to_learn.csv is available
    update_dict()
    pick_word()

def update_dict():
    global word_dict, french_df

    # word_dict is a list of dictionary
    try:
        #check if file is available
        french_df = pd.read_csv("words_to_learn.csv") #words_to_learn csv to df

    except FileNotFoundError:
        #if not available, create file
        word_df = pd.DataFrame(word_dict)#convert word dict to df
        word_df.to_csv("words_to_learn.csv", index = False) #df to csv

    else:
        word_df = pd.DataFrame(word_dict)  #convert word dict to df
        word_df.to_csv("words_to_learn.csv",index = False) #df to csv



    # save to words_to_learn.csv
#------------------UI-----------------#

window = Tk()
window.title("Flash Card")
window.config(width = 800, height = 526, bg = BACKGROUND_COLOR, padx= 50, pady=50)

timer = window.after(3000, flip_card)

img_card_front = PhotoImage(file = "images/card_front.png")
img_card_back = PhotoImage(file = "images/card_back.png")
canvas = Canvas(width = 800, height = 526, bg = BACKGROUND_COLOR,highlightthickness=0)
card_face = canvas.create_image(400,265, image = img_card_front)
canvas.grid(column = 0, row = 0, columnspan = 2)

img_wrong = PhotoImage(file="images/wrong.png")
button_wrong = Button(image = img_wrong, borderwidth = 0, highlightthickness = 0, command =  pick_word)
button_wrong.grid(column=0, row = 1)

img_right = PhotoImage(file="images/right.png")
button_right = Button(image = img_right, borderwidth = 0, highlightthickness = 0, command =  tick)
button_right.grid(column=1, row =1)

card_word = canvas.create_text(400, 263, text="word", font=("Arial", 60, "bold"))
card_title = canvas.create_text(400, 150, text="title", font=("Arial", 40, "italic"))

pick_word()

window.mainloop()
