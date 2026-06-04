from tkinter import *
from tkinter import messagebox

# Add Task Function
def add_task():
    task = entry.get()

    if task != "":
        task_listbox.insert(END, task)
        entry.delete(0, END)
    else:
        messagebox.showwarning("Warning", "Please Enter a Task")

# Delete Task Function
def delete_task():
    try:
        selected_task = task_listbox.curselection()[0]
        task_listbox.delete(selected_task)
    except:
        messagebox.showwarning("Warning", "Please Select a Task")

# Clear All Tasks Function
def clear_tasks():
    result = messagebox.askyesno("Confirm", "Do you want to clear all tasks?")
    if result:
        task_listbox.delete(0, END)

# Main Window
root = Tk()
root.title("To-Do List Application")
root.geometry("500x500")

# Heading
heading = Label(root, text="TO-DO LIST APPLICATION",
                font=("Arial", 18, "bold"))
heading.pack(pady=10)

# Entry Box
entry = Entry(root, width=40, font=("Arial", 12))
entry.pack(pady=10)

# Add Button
add_btn = Button(root, text="Add Task",
                 width=20, command=add_task)
add_btn.pack(pady=5)

# Task List
task_listbox = Listbox(root, width=50, height=12,
                       font=("Arial", 12))
task_listbox.pack(pady=10)

# Delete Button
delete_btn = Button(root, text="Delete Selected Task",
                    width=20, command=delete_task)
delete_btn.pack(pady=5)

# Clear Button
clear_btn = Button(root, text="Clear All Tasks",
                   width=20, command=clear_tasks)
clear_btn.pack(pady=5)

root.mainloop()
