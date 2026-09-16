import tkinter as tk
from pokemon import Pokemon

#creates the actual application window
window = tk.Tk()

#This names our window
window.title("Yusuf's Pokemon battle Simulator")

#1000 is the width and 700 is the height of the window
window.geometry("1000x700")

#player choice variable that is remembered by program
player_pokemon = None

#creating object for the pokemon using the Pokemon class and added stats
charmander = Pokemon(
    "Charmander",
    "Fire",
    39,
    52,
    43,
    60,
    50,
    65
)
#showing the stats of the pokemon
print(charmander.name, charmander.pokemon_type)
print(charmander.hp)
print(charmander.attack)
print(charmander.defence)
print(charmander.special_attack)
print(charmander.special_defence)
print(charmander.speed)

#Assigning the stats of a pokemon
squirtle = Pokemon(
    "Squirtle",
    "Water",
    44,
    48,
    65,
    50,
    64,
    43
)
#Displaying the stats of squirtle
print(squirtle.name, squirtle.pokemon_type)
print(squirtle.hp)
print(squirtle.attack)
print(squirtle.defence)
print(squirtle.special_attack)
print(squirtle.special_defence)
print(squirtle.speed)

#Assigning the stats of Bulbasaur
bulbasaur = Pokemon(
    "Bulbasaur",
    "Grass",
    45,
    49,
    49,
    65,
    65,
    45
)
#displays stats of bulbasaur
print(bulbasaur.name, bulbasaur.pokemon_type)
print(bulbasaur.hp)
print(bulbasaur.pokemon_type)
print(bulbasaur.hp)
print(bulbasaur.attack)
print(bulbasaur.defence)
print(bulbasaur.special_attack)
print(bulbasaur.special_defence)
print(bulbasaur.speed)


#Creating a function for if the player chooses charmander
def choose_pokemon(pokemon):
    global player_pokemon
    player_pokemon = pokemon
    result_label.config(text=f"You chose {pokemon}!")

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

#creating label or text spot for chosen pokemon
result_label = tk.Label(
    window,
    text="",
    font=("Arial", 20)
)

#adding result label to the window
result_label.pack()

#Pokemon selection frame to hold the buttons
pokemon_frame = tk.Frame(window)
#to place the area in the window
pokemon_frame.pack()

#creates visual button for a pokemon choice and stored the button in "charmander_button"
charmander_button = tk.Button(
    pokemon_frame,
    text = "Charmander",
    font = ("Arial", 18),
    command=lambda: choose_pokemon("Charmander")
)

#tells program to put the "Button" in the grid in the window
charmander_button.grid(
    row = 0,
    column = 0,
    padx = 20,
    pady = 20
)

#create button for pokemon choice
squirtle_button = tk.Button(
    pokemon_frame,
    text = "Squirtle",
    font = ("Arial", 18),
    command=lambda: choose_pokemon("Squirtle")
)
#tells program to put the "Button" in the grid in the window
squirtle_button.grid(
    row = 0,
    column = 1,
    padx = 20,
    pady = 20
)

#create button for pokemon choice
bulbasaur_button = tk.Button(
    pokemon_frame,
    text = "Bulbasaur",
    font = ("Arial", 18),
    command=lambda: choose_pokemon("Bulbasaur")
)
#tells program to put the "Button" in the grid in the window
bulbasaur_button.grid(
    row = 0,
    column = 2,
    padx = 20,
    pady = 20
)

#This starts the event lopp to allow the window to wait for user interaction
window.mainloop()

