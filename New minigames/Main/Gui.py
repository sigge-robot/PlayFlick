from tkinter import * # imports Tkinter


def skibidi():

    window = Tk() #makes the window
    theme = "#00bbff"


    window.geometry("500x500")
    window.title("Main Menu")
    window.config(background= theme)
    window.resizable(False,False)

    titleLabel = Label(window,
                text="You are gay",
                font=('areal', 40, 'bold'), 
            bg=(theme)
                )


    titleLabel.pack(pady= 10)


    window.mainloop() #place window on screen , lisens for events

