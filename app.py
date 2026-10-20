import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk

def convert():
    kg = entry_int.get()
    gram = kg * 1000
    output_string.set(str(gram) + ' grams')

def convert2():
    gram = entry2_int.get()
    kg = gram / 1000
    output2_string.set(str(kg) + " Kg")


root = ttk.Window(themename = 'darkly')
root.geometry("400x300")
root.title("Unit Converter")

label = ttk.Label(root, text='Kg into Gram:', font='Arial 20 bold')
label.pack(pady=10)

input_frame = ttk.Frame(master = root)

entry_int = tk.IntVar()
entry = ttk.Entry(master = input_frame, textvariable=entry_int)

button = ttk.Button(master = input_frame, text='Convert', command=convert)

entry.pack(side='left', padx=10)
button.pack(side='left', padx=10)
input_frame.pack()

output_string = tk.StringVar()
output = ttk.Label(root, text='Output', font = 'Calibri 16', textvariable=output_string)
output.pack()


label2 = ttk.Label(root, text = 'Gram into Kg:', font='Arial 20 bold')
label2.pack(pady=10)


input_frame2 = ttk.Frame(root)

entry2_int = tk.IntVar()
entry2 = ttk.Entry(input_frame2, textvariable=entry2_int)

button2 = ttk.Button(input_frame2, text='Convert', command=convert2)

entry2.pack(side='left', padx=10)
button2.pack(side='left', padx=10)

input_frame2.pack()

output2_string = tk.StringVar()
output2 = ttk.Label(root,font = 'Calibri 16', textvariable=output2_string)
output2.pack()





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