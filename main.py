from tkinter import *


chores = ["TRASH", "DISHES", "VACUUM", "BATHROOM"]
people = ["JOSH", "JEN", "KATIE", "JONATHAN"]

next_assignments = {}

def set_default_next_assignments():
    for i, chore in enumerate(chores):
        next_assignments[chore] = people[i % len(people)]

class Table:
     
    def __init__(self,root):
        
        set_default_next_assignments()
        num_chores = len(chores)

        lst = [[""]+chores] + [[person]+["-"]*num_chores for person in people] + [["NEXT"]+[next_assignments[chore] for chore in chores]]

        total_rows = len(lst)
        total_columns = len(lst[0])
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, fg='blue',
                               font=('Arial',12,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


  
# create root window
root = Tk()
t = Table(root)
root.mainloop()