import tkinter as tk
from tkinter import messagebox

class SimCardLockApp:
    def _init_(self, root):
        self.root = root
        self.root.title("Sim Card Lock")
        self.root.geometry("400x600")
        self.is_locked = True
        self.pin = "4002"  # Default PIN

        # Create canvas
        self.canvas = tk.Canvas(self.root, width=300, height=400, bg="white", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Sim card representation
        self.sim_card = self.canvas.create_rectangle(100, 150, 200, 300, fill="gray", outline="black", width=2)
        self.lock_indicator = self.canvas.create_text(150, 130, text="Locked", fill="red", font=("Arial", 14))
        self.lock_icon = self.canvas.create_oval(125, 180, 175, 230, fill="red")

        # PIN entry interface
        self.pin_frame = tk.Frame(self.root)
        self.pin_label = tk.Label(self.pin_frame, text="Enter PIN:", font=("Arial", 12))
        self.pin_entry = tk.Entry(self.pin_frame, show="*", font=("Arial", 12), width=10)
        self.pin_submit_button = tk.Button(
            self.pin_frame, text="Submit", command=self.verify_pin, bg="green", fg="white", font=("Arial", 10)
        )

        self.pin_label.grid(row=0, column=0, padx=5)
        self.pin_entry.grid(row=0, column=1, padx=5)
        self.pin_submit_button.grid(row=0, column=2, padx=5)
        
        # Toggle button
        self.toggle_button = tk.Button(
            self.root, text="Unlock SIM", command=self.show_pin_entry, bg="blue", fg="white", font=("Arial", 12), padx=10, pady=5
        )
        self.toggle_button.pack(pady=20)

    def show_pin_entry(self):
        if self.is_locked:
            self.pin_frame.pack(pady=10)

    def verify_pin(self):
        entered_pin = self.pin_entry.get()
        if entered_pin == self.pin:
            self.unlock_sim()
        else:
            messagebox.showerror("Error", "Incorrect PIN. Please try again.")

    def unlock_sim(self):
        self.is_locked = False
        self.canvas.itemconfig(self.lock_indicator, text="Unlocked", fill="green")
        self.canvas.itemconfig(self.lock_icon, fill="green")
        self.toggle_button.config(text="Lock SIM", command=self.lock_sim)
        self.pin_frame.pack_forget()

    def lock_sim(self):
        self.is_locked = True
        self.canvas.itemconfig(self.lock_indicator, text="Locked", fill="red")
        self.canvas.itemconfig(self.lock_icon, fill="red")
        self.toggle_button.config(text="Unlock SIM", command=self.show_pin_entry)

if __name__ == "_main_":
    root = tk.Tk()
    app = SimCardLockApp(root)
    root.mainloop()