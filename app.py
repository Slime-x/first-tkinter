import tkinter as tk

def button_cmd():
    print("The button is pressed")

root = tk.Tk()
root.geometry("600x400")
root.title("I will choose later")

label = tk.Label(root, text="This is a text", font=("Calibri", 18), width=100, pady=50)
button = tk.Button(root, text="Click me", padx=10, pady=10 ,command=button_cmd)
text = tk.Text(root, font=('calibri', 20), height=1, width=10)

label.pack()
text.pack()
button.pack()

root.mainloop()