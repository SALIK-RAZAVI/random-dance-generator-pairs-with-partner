import tkinter as tk
import random

dance_moves = [
    "Moonwalk ", "Robot", "Salsa", "Tango", "Macarena", "hiphop",
    "Twist", "Floss", "Dougie", "Breakdance", "Cha-Cha Slide","slow motion",
    "Electric Slide", "Running Man", "Vogue", "Cabbage Patch", "Charleston"
]

def create_dance_routine():
    your_moves = [random.choice(dance_moves) for _ in range(5)]
    partner_moves = [random.choice(dance_moves) for _ in range(5)]
    return your_moves, partner_moves

def display_routine(your_moves, partner_moves, label1, label2):
    def update_labels(i=0):
        if i < len(your_moves):
            label1.config(text=f"You: {your_moves[i]}")
            label2.config(text=f"Partner: {partner_moves[i]}")
            root.after(1000, update_labels, i + 1)
        else:
            label1.config(text="Dance Over!")
            label2.config(text="Dance Over!")

    update_labels()

root = tk.Tk()
root.title("Random Dance Move Generator")
root.geometry("500x300")

your_label = tk.Label(root, text="", font=("Helvetica", 16))
your_label.pack(pady=10)

partner_label = tk.Label(root, text="", font=("Helvetica", 16))
partner_label.pack(pady=10)

def generate_dance():
    your_moves, partner_moves = create_dance_routine()
    display_routine(your_moves, partner_moves, your_label, partner_label)

generate_button = tk.Button(root, text="Generate Dance Routine", command=generate_dance)
generate_button.pack(pady=20)

root.mainloop()

