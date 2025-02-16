##include<stdio.h>
#int main()
#{
#int n;
#printf("enter the number :-  ");
#scanf("%d",&n);
#if(n%2==0)
#{printf("%d is even",n);}
#else
#{printf("%d is odd",n);};
#return 0;
#}v
import tkinter as tk
from tkinter import messagebox

class SimCardLockAnimation:
    def __init__(self, root):
        self.root = root
        self.root.title("Sim Card Lock")
        self.root.geometry("400x600")
        self.is_locked = True

        # Create canvas
        self.canvas = tk.Canvas(self.root, width=300, height=400, bg="white", highlightthickness=0)
        self.canvas.pack(pady=20)

        # Sim card representation
        self.sim_card = self.canvas.create_rectangle(100, 150, 200, 300, fill="gray", outline="black", width=2)
        self.lock_indicator = self.canvas.create_text(150, 130, text="Locked", fill="red", font=("Arial", 14))
        self.lock_icon = self.canvas.create_oval(125, 180, 175, 230, fill="red")
        
        # Toggle button
        self.toggle_button = tk.Button(
            self.root, text="Unlock SIM", command=self.toggle_lock, bg="blue", fg="white", font=("Arial", 12), padx=10, pady=5
        )
        self.toggle_button.pack(pady=20)

    def toggle_lock(self):
        if self.is_locked:
            # Unlock the SIM
            self.is_locked = False
            self.canvas.itemconfig(self.lock_indicator, text="Unlocked", fill="green")
            self.canvas.itemconfig(self.lock_icon, fill="green")
            self.toggle_button.config(text="Lock SIM")
        else:
            # Lock the SIM
            self.is_locked = True
            self.canvas.itemconfig(self.lock_indicator, text="Locked", fill="red")
            self.canvas.itemconfig(self.lock_icon, fill="red")
            self.toggle_button.config(text="Unlock SIM")

if __name__ == "__main__":
    root = tk.Tk()
    app = SimCardLockAnimation(root)
    root.mainloop()
