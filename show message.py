import os
from tkinter import*
from tkinter import messagebox
def call():
	messagebox.showinfo("Succcesfull","Installation Completed")
root=Tk()
b=Button(root,text="Click",command=call)
b.pack()

root.mainloop()
os.system("pause")
