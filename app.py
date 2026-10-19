import tkinter as tk

def button_cmd():
    print("The button is pressed")

root = tk.Tk()

text = tk.Label(root, text = "This is a text", font = "Calibri", width=100)
button = tk.Button(root, text="Click me", command=button_cmd)

text.pack()
button.pack()

root.mainloop()