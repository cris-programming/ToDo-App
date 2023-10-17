from tkinter import *
from datetime import datetime
from os.path import isfile
from keyboard import on_press_key
from tkcalendar import DateEntry

# Check if the 'todos.txt' file exists, and create it if not
if not isfile('todos.txt'):
    try:
        f = open('todos.txt', 'w')
        f.close()
    except:
        pass

# Functions
def add_todo():
    """Add a to-do item to the listbox."""
    
    if todo.get() != '':
        # Get the current date and time
        now = datetime.now()
        current_time = now.strftime("%H:%M")
        date = now.strftime('%d/%m')
        
        if final_date.get_date() != '':
            listbox.insert(1, f'\u2713In {date} at {current_time} >>> {todo.get()} <<< for {final_date.get_date()} at {final_time.get()}')
        else:
            listbox.insert(1, f'\u2713In {date} at {current_time} >>> {todo.get()}')
        todo.delete(0, END)
        final_date.delete(0, END)
        final_time.delete(0, END)
    else:
        pass

def delete_todo():
    """Delete the selected to-do item from the listbox."""
    
    for i in listbox.curselection():
        x = listbox.get(i)
        if x == 'Todos:':
            pass
        if listbox.curselection() == ():
            pass
        else:
            with open('todos.txt', 'w+') as f:
                if x in f.read():
                    text = f.read()
                    f.write(text.replace(x))
            f.close()
            listbox.delete(ANCHOR)
    listbox.selection_clear(0, END)

def save_todo():
    """Save the selected to-do item to the 'todos.txt' file."""
    
    if listbox.curselection() == ():
        pass
    else:
        for i in listbox.curselection():
            x = listbox.get(i)
            if x == 'Todos:':
                pass
            else:
                x = str(x).replace('\u2713', '')
                f = open('todos.txt', 'a')
                f.write(f'{x}\n')
                f.close()
    listbox.selection_clear(0, END)
    
def delete_all():
    """Delete all to-do items from the listbox."""
    
    listbox.select_set(1, END)
    delete_todo()

def save_all():
    """Save all to-do items to the 'todos.txt' file."""
    
    listbox.select_set(1, END)
    save_todo()

def load_todo():
    """Load to-do items from the 'todos.txt' file."""
    
    f = open('todos.txt', 'r+')
    for todo in f:
        listbox.insert(1, f'\u2713{todo}')

# Config the window
root = Tk()
root.title("Todo App")
root.geometry('400x350+100+100')
root.resizable(False, False)
root.attributes('-topmost', 1)
frame = Frame(root)
frame.pack()
root.configure(background = '#9ec3ff')
# Icon : "https://www.flaticon.com/free-icons/to-do" To do icons created by Freepik - Flaticon
p = PhotoImage(file = 'todo.png')
root.iconphoto(False, p)

# Menu
mainmenu = Menu(frame)
mainmenu.add_command(label = "Add", command = add_todo, accelerator = "enter")  
mainmenu.add_command(label = "Delete", command = delete_todo, accelerator = "f11")
mainmenu.add_command(label = "Save", command = save_todo, accelerator = "f10")
mainmenu.add_command(label = "Load", command = load_todo, accelerator = "f12")
mainmenu.add_command(label = "SaveAll", command = save_all)
mainmenu.add_command(label = "DeleteAll", command = delete_all)

# Widgets
listbox = Listbox(root, width = 50, selectmode = SINGLE, selectbackground = '#dedede', selectforeground = '#000000', cursor = "circle")
listbox.pack(pady = 8)
listbox.insert(0, 'Todos:')
listbox.selection_set(first = 1, last = END)
listbox.selection_clear(0, END)
label = Label(root, text = "Enter here your todo and press 'add': ", bg = '#9ec3ff', fg = '#000000')
label.pack(pady=2)
todo = Entry(root, width = 40)
todo.pack(pady = 5)
label = Label(root, text = "Enter here the final date and time: ", bg = '#9ec3ff', fg = '#000000')
label.pack(pady = 0)
final_date = DateEntry(root, width = 25)
final_date.pack(side = LEFT, padx = 20, pady = 0)
final_time = Entry(root, width = 25)
final_time.pack(side = RIGHT, padx = 20, pady = 0)

# Shortcuts
on_press_key('enter', lambda _:add_todo())
on_press_key('f10', lambda _:save_todo())
on_press_key('f11', lambda _:delete_todo())
on_press_key('f12', lambda _:load_todo())

# Mainloop
root.config(menu = mainmenu)
root.mainloop()