from tkinter import *


chores = ["TRASH", "DISHES", "VACUUM", "BATHROOM", "DOG"]
people = ["JOSH", "JEN", "KATIE", "JONATHAN"]
 
class Table:
     
    def __init__(self,root):
         
        # code for creating table
        for i in range(total_rows):
            for j in range(total_columns):
                 
                self.e = Entry(root, width=20, fg='white',
                               font=('Arial',16,'bold'))
                 
                self.e.grid(row=i, column=j)
                self.e.insert(END, lst[i][j])

num_chores = len(chores)

# take the data
lst = [[""]+chores, [people[0]]+["-"]*num_chores, [people[1]]+["-"]*num_chores, [people[2]]+["-"]*num_chores, [people[3]]+["-"]*num_chores]
  
# find total number of rows and
# columns in list
total_rows = len(lst)
total_columns = len(lst[0])
  
# create root window
root = Tk()
t = Table(root)
root.mainloop()