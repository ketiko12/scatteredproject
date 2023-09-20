from tkinter import *
root=Tk()
myMenu=Menu(root)
root.config(menu=myMenu)
def function1():
 print('Menu item clicked!')
submenu=Menu(myMenu)
myMenu.add_cascade(label="File", menu=submenu)
submenu.add_command(label="Project", command=function1)
submenu.add_command(label='Save', command=function1)
submenu.add_separator()
submenu.add_command(label='Exit', command=function1)

newmenu=Menu(myMenu)
myMenu.add_cascade(label='Exit', menu=newmenu)
newmenu.add_command(label='Undo', command=function1)

toolbar=Frame(root, bg='blue')
insertButton=Button(toolbar, text='INsert File', command=function1)
insertButton.pack(side=LEFT,padx=2, pady=3)

printButton=Button(toolbar, text='print',command=function1)
printButton.pack(side=LEFT, padx=2, pady=4)
toolbar.pack(side=TOP, fill=X)
status=Label(root, text='This is the status', bd=1, relief=SUNKEN, anchor=W)
status.pack(side=BOTTOM, fill=X)

import tkinter.messagebox
tkinter.messagebox.showinfo('Title','This is awesome!')
response=tkinter.messagebox.askquestion('Question-1','Do you like coffee?')

if response=='yes':
 print('There is the pot with water and coffee box.Make a coffee and bring it for me too. ')



root.mainloop()


print('Hello world');

c=6*4
print(c)