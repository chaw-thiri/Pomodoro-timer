import tkinter as tk

def show_selection():
    selected_option = var.get()
    label.config(text=f"You selected: {selected_option}")

# Create the main window
root = tk.Tk()
root.title("Radio Buttons Example")

# Create a Tkinter variable to hold the selected option
var = tk.StringVar()

# Create radio buttons and associate them with the variable

radio_button1 = tk.Radiobutton(root, text="Option 1", variable=var, value="Option 1", command=show_selection)
radio_button2 = tk.Radiobutton(root, text="Option 2", variable=var, value="Option 2", command=show_selection)
radio_button3 = tk.Radiobutton(root, text="Option 3", variable=var, value="Option 3", command=show_selection)

# Place the radio buttons in the window
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Create a label to display the selected option
label = tk.Label(root, text="")
label.pack()

# Start the Tkinter event loop
root.mainloop()
