import time
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class VirtualPet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.happiness = 50
        self.energy = 50

    def feed(self):
        self.hunger -= 10
        self.happiness += 5
        self.update_status()

    def play(self):
        self.happiness += 10
        self.energy -= 5
        self.update_status()

    def rest(self):
        self.energy += 15
        self.update_status()

    def update_status(self):
        self.hunger = max(0, min(100, self.hunger))
        self.happiness = max(0, min(100, self.happiness))
        self.energy = max(0, min(100, self.energy))
        hunger_bar["value"] = self.hunger
        happiness_bar["value"] = self.happiness
        energy_bar["value"] = self.energy

        if self.hunger >= 90:
            messagebox.showwarning("Warning", f"{self.name} is very hungry!")
        if self.happiness <= 10:
            messagebox.showwarning("Warning", f"{self.name} is very unhappy!")
        if self.energy <= 10:
            messagebox.showwarning("Warning", f"{self.name} is very tired!")

def feed_pet():
    pet.feed()

def play_with_pet():
    pet.play()

def rest_pet():
    pet.rest()

root = tk.Tk()
root.title("Virtual Pet")

# Create pet
pet_name = input("Enter the name of your virtual pet: ")
pet = VirtualPet(pet_name)

# Create GUI
canvas = tk.Canvas(root, width=400, height=300)
canvas.pack()

# Create hunger bar
hunger_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", maximum=100, value=pet.hunger)
hunger_bar.place(x=100, y=20)

# Create happiness bar
happiness_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", maximum=100, value=pet.happiness)
happiness_bar.place(x=100, y=60)

# Create energy bar
energy_bar = ttk.Progressbar(root, orient="horizontal", length=200, mode="determinate", maximum=100, value=pet.energy)
energy_bar.place(x=100, y=100)

# Create buttons
feed_button = tk.Button(root, text="Feed", command=feed_pet)
feed_button.place(x=50, y=140)

play_button = tk.Button(root, text="Play", command=play_with_pet)
play_button.place(x=150, y=140)

rest_button = tk.Button(root, text="Rest", command=rest_pet)
rest_button.place(x=250, y=140)

root.mainloop()
