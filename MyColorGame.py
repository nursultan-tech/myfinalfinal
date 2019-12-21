
import tkinter
import random

# from typing import Any

colours = ['Red', 'Blue', 'Green', 'Pink', 'Black', 'Yellow', 'Orange', 'White', 'Purple', 'Brown', 'Silver']
score = 0
myScore = 0
timeLeft = 60

def startGame(event):
    if timeLeft == 60:
        countdown()
    nextColour()
    container.pack()
    cont.pack_forget()


def nextColour():
    global score
    global timeLeft
    if timeLeft > 0:
        e.focus_set()
        if e.get().lower() == colours[1].lower():
            score += 1

        e.delete(0, tkinter.END)
        random.shuffle(colours)
        label.config(fg=str(colours[1]), text=str(colours[0]))
        scoreLabel.config(text="Score: " + str(score))


def countdown():
    global timeLeft
    if timeLeft > 0:
        timeLeft -= 1
        timeLabel.config(text="Time left: "
                              + str(timeLeft))
        timeLabel.after(1000, countdown)
    elif timeLeft == 0:
        restart()


def restart():
    global timeLeft
    global score
    timeLeft = 60
    finalScoreLabel.config(text="Your score is " + str(score))
    container.pack_forget()
    cont.pack()
    score = int(0)


root = tkinter.Tk()
root.title("COLOR GAME")
root.geometry("400x250")


cont = tkinter.Frame(root, width=475, height=300)

finalScoreLabel = tkinter.Label(cont, text="",
                                font=('Helvetica', 12))
gameOverLabel = tkinter.Label(cont, text="Game Over",
                              font=('Helvetica', 12))
restartButton = tkinter.Button(cont, text="Restart the game")
restartButton.bind("<Button-1>", lambda event: startGame(event))




# cont.pack()
finalScoreLabel.pack()
gameOverLabel.pack()
restartButton.pack()

container = tkinter.Frame(root, width=475, height=300)
container.pack()

instructions = tkinter.Label(container, text="Type in the colour of the words, and not the word text!",
                             font=('Helvetica', 12))
instructions.pack()
scoreLabel = tkinter.Label(container, text="Press enter to start",
                           font=('Helvetica', 12))
scoreLabel.pack()
timeLabel = tkinter.Label(container, text="Time left: " +
                                          str(timeLeft), font=('Helvetica', 12))
timeLabel.pack()
label = tkinter.Label(container, font=('Helvetica', 60))
label.pack()
e = tkinter.Entry(container)
root.bind('<Return>', startGame)
e.pack()
e.focus_set()
root.mainloop()
