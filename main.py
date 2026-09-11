import tkinter as tk

#creates the actual application window
window = tk.Tk()

#This names our window
window.title("Yusuf's Pokemon battle Simulator")

#1000 is the width and 700 is the height of the window
window.geometry("1000x700")

#player choice variable that is remembered by program
player_pokemon = None

#Creating a function for if the player chooses charmander
def choose_charmander():
    global player_pokemon
    player_pokemon = "Charmander"
    print("You chose Charmander!")

#creating function for when player chooses squirtle
def choose_squirtle():
    global player_pokemon
    player_pokemon = "Squirtle"
    print("You chose Squirtle!")

#creating function for when player chooses Bulbasaur
def choose_bulbasaur():
    global player_pokemon
    player_pokemon = "Bulbasaur"
    print("You chose Bulbasaur!")

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

#Pokemon selection frame to hold the buttons
pokemon_frame = tk.Frame(window)
#to place the area in the window
pokemon_frame.pack()

#creates visual button for a pokemon choice and stored the button in "charmander_button"
charmander_button = tk.Button(
    pokemon_frame,
    text = "Charmander",
    font = ("Arial", 18),
    command= choose_charmander
)

#tells program to put the "Button" in the grid in the window
charmander_button.grid(row = 0, column = 0, padx = 20, pady = 20)

#create button for pokemon choice
squirtle_button = tk.Button(
    pokemon_frame,
    text = "Squirtle",
    font = ("Arial", 18),
    command= choose_squirtle
)
#tells program to put the "Button" in the grid in the window
squirtle_button.grid(row = 0, column = 1, padx = 20, pady = 20)

#create button for pokemon choice
bulbasaur_button = tk.Button(
    pokemon_frame,
    text = "Bulbasaur",
    font = ("Arial", 18),
    command= choose_bulbasaur
)
#tells program to put the "Button" in the grid in the window
bulbasaur_button.grid(row = 0, column = 2, padx = 20, pady = 20)

#This starts the event lopp to allow the window to wait for user interaction
window.mainloop()

