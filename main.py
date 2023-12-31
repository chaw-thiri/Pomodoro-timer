from tkinter import *
import math
import pygame
from tkinter import messagebox
pygame.mixer.init()
#  ---------------------------------------------------------- CONSTANTS -----------------------------------
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#17B794"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 25
REPS = 0
timer = None
# ---------------------------- How to use the app ---------------------------------------------------------------------
def help():
    messagebox.showinfo(title="How to Use",message="Click START to Set Timer (25 mins)\nWhen you hear a notification "
                                                   "sound your work session is up.\nTake Short Break (5 mins)\nThat "
                                                   "will takes place for 4 times.\nAt the end you will get long break "
                                                   "of 25 mins.\nClick Reset or Press ESC to restart your session "
                                                   "from the beginning."
                                                   "\nHave a productive day!")


# ---------------------------- BACKGROUND MUSIC and NOTI Sounds -------------------------------------------------------
def noti():
    pygame.mixer.music.load("noti.mp3")
    pygame.mixer.music.play(loops=0)


def sound(song):
    # TODO : play sound when the song is selected
    # options = ["Sound off", "Library", "Rainy day", "Coffee Shop"]
    song = var.get()
    if song == "Library":
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Library.mp3")
        pygame.mixer.music.play(loops=8)
    elif song == "Rainy day":
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Rainy Day.mp3")
        pygame.mixer.music.play(loops=8)
    elif song == "Coffee Shop":
        pygame.mixer.music.stop()
        pygame.mixer.music.load("Cafe.mp3")
        pygame.mixer.music.play(loops=27)
    elif song == "Sound off":
        pygame.mixer.music.stop()


# ----------------------------------------------------------- TIMER RESET -----------------------------------
def reset_timer():
    global timer
    window.after_cancel(timer)
    global REPS
    REPS = 0
    # reset all the labels
    pygame.mixer.music.stop()
    var.set("Sound off")
    timerLabel.config(text="Pomodoro")
    canvas.itemconfig(timer_text, text="00:00")
    checkLabel.config(text="")


# ----------------------------------------------------------- TIMER MECHANISM --------------------------------
# cannot use loop here, will freeze the program
def start():
    # Call different time according to current reps
    global REPS
    REPS += 1
    if REPS == 8:
        count_down(LONG_BREAK_MIN * 60)
        timerLabel.config(text="REST", font=(FONT_NAME, 23, "bold"), fg=GREEN, bg=YELLOW)
    elif (REPS % 2 == 0):  # 2,4,6 sessions are short break
        count_down(SHORT_BREAK_MIN * 60)
        timerLabel.config(text="Break", font=(FONT_NAME, 23, "bold"), fg=GREEN, bg=YELLOW)
    else:  # 1,3,5,7 are work minutes
        count_down(WORK_MIN * 60)
        timerLabel.config(text="STUDY", font=(FONT_NAME, 23, "bold"), fg=RED, bg=YELLOW)


# ------------------------------------------------------ COUNTDOWN MECHANISM -------------------------------------
def count_down(count):
    # calculate min and sec
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # To get 00:00 format
    # for seconds
    if count_sec == 0:
        count_sec = "00"
    elif count_sec < 10:
        count_sec = f"0{count_sec}"
    # for minutes
    if count_min == 0:
        count_min = "00"
    elif count_min < 10:
        count_min = f"0{count_min}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    # refresh the frame every second
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)  # 1000 miliseconds
    else:  # the timer hits 00:00
        pygame.mixer.music.stop()
        noti()
        start()
        if REPS % 2 == 0:
            checkLabel.config(text="🟢" * math.floor(REPS / 2), font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)


# ---------------------------- UI SETUP -------------------------------------------------------
window = Tk()
window.title("🍅Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# ADD TIMER label AND 🟢 label
# add TIMER label
timerLabel = Label(width=10)
timerLabel.config(text="Pomodoro", font=(FONT_NAME, 23, "bold"), fg=GREEN, bg=YELLOW)
timerLabel.grid(row=0, column=1)

checkLabel = Label()
checkLabel.config(font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
checkLabel.grid(row=3, column=1)

# add tomato image and timer text using canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomatoImg = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomatoImg)
timer_text = canvas.create_text(100, 133, text="00:00", font=(FONT_NAME, 14, "bold"), fill="white")
canvas.grid(row=1, column=1)

# add start buttom
startB = Button(width=7, highlightthickness=0)
startB.config(text="Start", command=start)
startB.grid(row=2, column=0)

# add end buttom
endB = Button(width=7, highlightthickness=0)
endB.config(text="Reset", command=reset_timer)
endB.grid(row=2, column=2)

# add help buttom
help_button=Button(window,text='❓',font=(FONT_NAME,12),command=help, bd= 0,highlightthickness=1,fg=PINK,bg=YELLOW)
help_button.grid(row=5,column = 0)

# add drop down menu for playing background music
var = StringVar()
var.set("Choose a sound option")

options = ["Sound off", "Library", "Rainy day", "Coffee Shop"]

# Create an option menu and associate it with the variable
option_menu = OptionMenu(window,var,*options, command=sound)
option_menu.grid(row=5, column=0, columnspan=4)


# ------------------------------------------------------------- Key binding ---------------------------------------

window.bind('<Escape>', lambda x:reset_timer())


window.mainloop()

