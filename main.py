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

        row = event.widget.grid_info()['row']
        col = event.widget.grid_info()['column']
        self.moveSelected(row-1, col-1)

        next_entry = self.entries[("NEXT", chores[col-1])]

        min_timestamp = float("inf") 
        next = people[0]

        for person in people:
            value = self.entries[(person, chores[col-1])].get()
            if value == "-":
                next = person
                break

            int_timestamp = datetime.strptime(value, "%d %B %H:%M:%S").timestamp()
            if int_timestamp <= min_timestamp:
                min_timestamp = int_timestamp
                next = person

        next_entry.delete(0, END)
        next_entry.insert(0, next)

    def moveSelected(self, x : int, y : int):
        self.entries[(people[self.selectedX], chores[self.selectedY])].config({"background": "white"})
        self.selectedX = x
        self.selectedY = y
        self.entries[(people[self.selectedX], chores[self.selectedY])].config({"background": "dodger blue"})
        
    def moveUp(self, event):
        if (self.selectedX > 0):
            self.moveSelected(self.selectedX - 1, self.selectedY)

    def moveDown(self, event):
        if (self.selectedX < len(people) - 1):
            self.moveSelected(self.selectedX + 1, self.selectedY)
     
    def moveLeft(self, event):
        if (self.selectedY > 0):
            self.moveSelected(self.selectedX, self.selectedY - 1)

    def moveRight(self, event):
        if (self.selectedY < len(chores) - 1):
            self.moveSelected(self.selectedX, self.selectedY + 1)
     
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
        #Typing mode for manual entry
        #Keyboard support
        self.selectedX = 0
        self.selectedY = 0
        self.entries[(people[self.selectedX], chores[self.selectedY])].config({"background": "dodger blue"})
        root.bind("<Up>", self.moveUp)
        root.bind("<Down>", self.moveDown)
        root.bind("<Left>", self.moveLeft)
        root.bind("<Right>", self.moveRight)

set_default_next_assignments()

# create root window
root = Tk()
t = Table(root)

# Set the position of button on the top of window.   
root.mainloop()
