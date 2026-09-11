import tkinter as tk
#creates the actual application window
window = tk.Tk()
#This names our window
window.title("Yusuf's Pokemon battle Simulator")
#1000 is the width and 700 is the height of the window 
window.geometry("1000x700")
#create a label to display text inside a Window
title_label = tk.Label(
    window,
    text="Yusuf's Pokemon battle Arena",
    font=("Arial", 40)
)
#this creates a title in the window
title_label.pack()
#Create a label for user instructions in the window
instruction_label = tk.Label(
    window,
    text="Choose your pokemon!",
    font=("Arial", 20)
)
#tells program where to put user instructions
instruction_label.pack()

#This starts the event lopp to allow the window to wait for user interaction
window.mainloop()

