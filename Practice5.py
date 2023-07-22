
import tkinter as tk

def on_button_click():
    user_input = entry.get()
    print("User input:", user_input)
    # You can store the value in a variable or use it in other ways

root = tk.Tk()
root.title("Value Storage Example")

entry = tk.Entry(root)
entry.pack(pady=10)

button = tk.Button(root, text="Submit", command=on_button_click)
button.pack()

root.mainloop()
