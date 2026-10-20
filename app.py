import tkinter as tk
from tkinter import ttk

def convert():
    ...


root = tk.Tk()
root.geometry("600x400")
root.title("I will choose later")

label = ttk.Label(root, text='Kg into grams:', font='Arial 20 bold')
label.pack()

input_frame = ttk.Frame(master = root)
entry = ttk.Entry(master = input_frame)
button = ttk.Button(master = input_frame, text='Convert', command=convert)

entry.pack(side='left', padx=10)
button.pack(side='left', padx=10)
input_frame.pack()






root.mainloop()




# Code i did but later dont need.

# def button_cmd():
#     print("The button is pressed")



# label = ttk.Label(root, text="This is a text", font=("Calibri", 18))
# button = tk.Button(root, text="Click me", padx=10, pady=10 ,command=button_cmd)
# text = tk.Text(root, font=('calibri', 20), height=1, width=10)

# label.pack()
# text.pack()
# button.pack()

# print("Available themes:", style.theme_names())
# print("Current theme:", style.theme_use())