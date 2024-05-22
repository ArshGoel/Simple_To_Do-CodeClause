#---------------------Import Statements------------------#
from tkinter import *
import time
from tkinter import ttk
from ttkthemes import ThemedTk      ########-------pip install ttkthemes-------######
from tkinter import font
import tkinter.simpledialog as simpledialog

#---------------------Functions------------------#
def update_time():
    global tasks,ctask
    current_time = time.strftime("%H:%M:%S")
    time1 = current_time.split(':')[0]
    incomplete_tasks = len(tasks)
    complete_tasks = len(ctask)
    if 5 <= int(time1[0]) < 12:
        greeting_label.config(text=f"Good morning Sir!. \nYou have {incomplete_tasks} incomplete tasks. \nYou have {complete_tasks} completed tasks.")
    elif 12 <= int(time1[0]) < 17:
        greeting_label.config(text=f"Good afternoon Sir!. \nYou have {incomplete_tasks} incomplete tasks.\nYou have {complete_tasks} completed tasks.")
    else:
        greeting_label.config(text=f"Good evening Sir!. \nYou have {incomplete_tasks} incomplete tasks.\nYou have {complete_tasks} completed tasks.")
    root.after(10, update_time)

def remove_completed():
    global tasks
    selected_task = listbox.curselection()
    if len(selected_task) > 0:
        tasks[selected_task[0]] = tasks[selected_task[0]]
        listbox.delete(selected_task[0])
        tasks.pop(selected_task[0])

    update_time()

def add_task():
    task = entry.get()
    if task != "":
        tasks.append(task)
        listbox.insert(END, task)
        entry.delete(0, END)

def edit_task():
    global tasks
    selected_task = listbox.curselection()
    if len(selected_task) > 0:
        task_to_edit = tasks[selected_task[0]]
        edit_to_do= simpledialog.askstring("Edit To Do", "Enter the new to-do description:", initialvalue=task_to_edit)
        if edit_to_do is not None:
            tasks[selected_task[0]] = edit_to_do
            listbox.delete(selected_task[0])
            listbox.insert(selected_task[0], edit_to_do)
            update_time()

def mark_complete():
    global ctask
    selected_task = listbox.curselection()
    # print(selected_task)
    if len(selected_task) > 0:
        tasks[selected_task[0]] = "Completed: " + tasks[selected_task[0]]
        listbox.delete(selected_task[0])
        ctask.append(tasks[selected_task[0]])
        completed.insert(selected_task[0],tasks[selected_task[0]])
        tasks.pop(selected_task[0])
    update_time()

#---------------------GUI Window------------------#
root = ThemedTk(theme="adapta")
root.title("To-Do List App")
root.maxsize(500,760)
root.minsize(500,760)
root.iconbitmap(r"F:\PYTHON\Internship\Simple To Do\logo.ico")

font1 = font.Font(family='Lucida Calligraphy',size=12)

# Create a frame to hold the entry widget and add button
frame = ttk.Frame(root)
frame.pack(padx=10, pady=10)

# Create a label to display the greeting
greeting_label = ttk.Label(frame,font=font1)
greeting_label.grid(row=0, column=0, padx=5, pady=5)

# Create an entry widget for the user to enter tasks
entry = ttk.Entry(frame, width=30,font=font1)
entry.grid(row=1, column=0)

# Create a button to add tasks to the list
add_button = Button(frame, text="Add Task", command=add_task,font=font1)
add_button.grid(row=1, column=1)

l1 = ttk.Label(root,text="Incomplete Tasks...",font=font1)
l1.pack(padx=10, pady=10)

# Create a listbox to display the tasks
listbox = Listbox(root, width=50, height=10,font=font1)
listbox.pack(padx=10, pady=10)

l2 = ttk.Label(root,text="Completed Tasks...",font=font1)
l2.pack(padx=10, pady=10)

completed = Listbox(root, width=50, height=10,font=font1)
completed.pack(padx=10, pady=10)

# Create buttons to mark tasks as completed and remove completed tasks
complete_button = Button(root,font=(font1),text="Mark Complete", command=mark_complete)
complete_button.pack(side=LEFT,padx=10, pady=10)

remove_button = Button(root,font=font1, text="Remove Completed", command=remove_completed)
remove_button.pack(side=RIGHT, padx=10, pady=10)

edit_button = Button(root,font=font1, text="Edit Task", command=edit_task)
edit_button.pack(anchor="s", padx=10, pady=10)
tasks = []
ctask = []
# Call the update_time function to start the time-changing label
update_time()

root.mainloop()