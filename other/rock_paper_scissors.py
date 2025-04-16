import random
import tkinter as tk
from tkinter import ttk

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'tie'
    elif (
        (player_choice == 'rock' and computer_choice == 'scissors') or
        (player_choice == 'paper' and computer_choice == 'rock') or
        (player_choice == 'scissors' and computer_choice == 'paper')
    ):
        return 'player'
    else:
        return 'computer'

class RockPaperScissorsGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock Paper Scissors")
        self.player_score = 0
        self.computer_score = 0
        
        # Create main frame
        main_frame = ttk.Frame(root, padding="10")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Create labels
        self.status_label = ttk.Label(main_frame, text="Choose your move!", font=('Arial', 12))
        self.status_label.grid(row=0, column=0, columnspan=3, pady=10)
        
        self.score_label = ttk.Label(main_frame, text="Score - You: 0, Computer: 0", font=('Arial', 12))
        self.score_label.grid(row=1, column=0, columnspan=3, pady=5)
        
        # Create styled buttons
        button_style = {'font': ('Arial', 14), 'width': 10, 'height': 2}
        
        tk.Button(main_frame, text="Rock", command=lambda: self.play("rock"),
                 bg='red', fg='white', **button_style).grid(row=2, column=0, padx=5)
        tk.Button(main_frame, text="Paper", command=lambda: self.play("paper"),
                 bg='green', fg='white', **button_style).grid(row=2, column=1, padx=5)
        tk.Button(main_frame, text="Scissors", command=lambda: self.play("scissors"),
                 bg='blue', fg='white', **button_style).grid(row=2, column=2, padx=5)
        
        tk.Button(main_frame, text="Quit", command=self.root.destroy,
                 font=('Arial', 12), width=8).grid(row=3, column=0, columnspan=3, pady=10)

    def play(self, player_choice):
        computer_choice = get_computer_choice()
        winner = determine_winner(player_choice, computer_choice)
        
        # Update status
        status_text = f"Computer chose: {computer_choice}\n"
        if winner == 'tie':
            status_text += "It's a tie!"
        elif winner == 'player':
            status_text += "You win!"
            self.player_score += 1
        else:
            status_text += "Computer wins!"
            self.computer_score += 1
            
        self.status_label["text"] = status_text
        self.score_label["text"] = f"Score - You: {self.player_score}, Computer: {self.computer_score}"

def main():
    root = tk.Tk()
    app = RockPaperScissorsGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()

