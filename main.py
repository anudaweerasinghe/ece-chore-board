from tkinter import *


chores = ["TRASH", "DISHES", "VACUUM", "BATHROOM", "DOG"]
people = ["JOSH", "JEN", "KATIE", "JONATHAN"]
 
class Table:
     
    def __init__(self,root):
        num_chores = len(chores)

        lst = [[""]+chores] + [[person]+["-"]*num_chores for person in people]

        total_rows = len(lst)
        total_columns = len(lst[0])
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=16, fg='blue',
                               font=('Arial',14,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])


  
# create root window
root = Tk()
t = Table(root)
root.mainloop()