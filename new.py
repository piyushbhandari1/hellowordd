
import tkinter as tk
from datetime import datetime

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)

def delete_task():
    try:
        index = listbox.curselection()
        listbox.delete(index)
    except:
        pass

# Create the main window
window = tk.Tk()
window.title("To-Do List")

# Create the listbox to display tasks
listbox = tk.Listbox(window, width=50)
listbox.pack(pady=10)

# Create a scrollbar for the listbox
scrollbar = tk.Scrollbar(window)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the listbox and scrollbar
listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

# Create the entry widget to add new tasks
entry = tk.Entry(window, font=("Helvetica", 14))
entry.pack(pady=10)

# Create the buttons
add_button = tk.Button(window, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(window, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

# Create a label for displaying the date and time
date_label = tk.Label(window, font=("Helvetica", 12), anchor=tk.W)
date_label.pack()

# Function to update the date and time label
def update_datetime():
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    date_label.config(text="Date and Time: " + current_datetime)
    window.after(1000, update_datetime)  # Update every 1 second (1000 milliseconds)

# Start updating the date and time label
update_datetime()

# Start the main event loop
window.mainloop()
