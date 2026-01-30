# Imports
import tkinter as tk

jim_toggle = False

# Tells the button what to do (functions go first)
def say_jim():
    global jim_toggle
    jim_toggle = not(jim_toggle)
    if jim_toggle:
        label.config(text="Jim.", bg="green")
        jim_button.config(text="Jim.", bg="green")
        root.title("Jim.")
    else:
        label.config(text="Jeff(!?)", bg="red")
        jim_button.config(text="GO BACK", bg="red")
        root.title("GET RID OF JEFF")

# Create main window
root = tk.Tk()
root.title("Smth Corny")
root.geometry("800x600")

# Create label (text)
label = tk.Label(root, text="Jeff(!?)", bg="red", font=('Arial', 28))
label.pack()

# Create button
jim_button = tk.Button(root, text="GO TO JIM", command=say_jim, bg="red", font=('Arial', 14))
jim_button.pack()

# Runs program above
root.mainloop()