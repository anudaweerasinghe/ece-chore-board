from tkinter import *
from datetime import datetime


chores = ["TRASH", "DISHES", "VACUUM", "BATHROOM"]
people = ["JOSH", "JEN", "KATIE", "JONATHAN"]

next_assignments = {}

def set_default_next_assignments():
    for i, chore in enumerate(chores):
        next_assignments[chore] = people[i % len(people)]

class Table:

    def on_click(self, event):
        event.widget.delete(0, END)

        current_date = datetime.now()

        event.widget.insert(0, current_date.strftime("%d %B %H:%M:%S"))

        col = event.widget.grid_info()['column']

        next_entry = self.entries[("NEXT", chores[col-1])]

        min_timestamp = float("inf") 
        next = people[0]

        for person in people:
            value = self.entries[(person, chores[col-1])].get()
            if value == "-":
                next = person
                break

            int_timestamp = float("-inf") if value == "-" else datetime.strptime(value, "%d %B %H:%M:%S").timestamp()
            if int_timestamp <= min_timestamp:
                min_timestamp = int_timestamp
                next = person

        next_entry.delete(0, END)
        next_entry.insert(0, next)
     
    def __init__(self,root):
        
        self.entries = {}
        
        num_chores = len(chores)

        lst = [[""]+chores] + [[person]+["-"]*num_chores for person in people] + [["NEXT"]+[next_assignments[chore] for chore in chores]]

        total_rows = len(lst)
        total_columns = len(lst[0])
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                e = Entry(root, fg='blue',
                               font=('Arial',18,'bold'))
                 
                e.grid(row=i, column=j)
                e.insert(END, lst[i][j])

                if i>0 and j>0:
                    person = people[i-1] if i <= len(people) else "NEXT"
                    self.entries[(person, chores[j-1])] = e

                    if i <= len(people):
                        e.bind("<1>", self.on_click)

set_default_next_assignments()

# create root window
root = Tk()
t = Table(root)

# Set the position of button on the top of window.   
root.mainloop()