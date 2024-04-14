import tkinter as tk
from tkinter import scrolledtext
from adventure import play, resume

class AdventureGUI:
    def __init__(self, master):
        self.master = master
        master.title("Adventure Game")

        self.output_text = scrolledtext.ScrolledText(master, wrap=tk.WORD, width=50, height=20)
        self.output_text.pack(expand=True, fill='both')

        self.command_entry = tk.Entry(master)
        self.command_entry.pack(fill='x')
        self.command_entry.bind("<Return>", self.process_command)

        self.resume_button = tk.Button(master, text="Resume Game", command=self.resume_game)
        self.resume_button.pack()

        self.play_button = tk.Button(master, text="New Game", command=self.start_new_game)
        self.play_button.pack()

        self.output_text.insert(tk.END, "Welcome to Adventure Game!\n")
    def process_command(self, event):
        command = self.command_entry.get().strip()
        if command.lower() == 'quit':
            self.master.destroy()
        elif "WELCOME TO ADVENTURE!!  WOULD YOU LIKE INSTRUCTIONS?" in self.output_text.get('1.0', tk.END):
            self.output_text.insert(tk.END, f"\n> {command}\n")
            self.output_text.insert(tk.END, play(command))
        else:
            self.output_text.insert(tk.END, f"\n> {command}\n")
            self.output_text.insert(tk.END, play(command))
        self.command_entry.delete(0, tk.END)

    def start_new_game(self):
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, "Starting new game...\n")
        self.output_text.insert(tk.END, play())

    def resume_game(self):
        savefile = 'adventure_save.txt'  # Specify the save file name here
        self.output_text.delete('1.0', tk.END)
        self.output_text.insert(tk.END, "Resuming game...\n")
        self.output_text.insert(tk.END, resume(savefile))
        

root = tk.Tk()
app = AdventureGUI(root)
root.mainloop()
