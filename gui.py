from tkinter import *

window = Tk()

window.title('python')

# textbox
textbox = Entry(window,width = 50,bg = 'red').grid(row = 0 , column=0)

# label
Label(window,text = "I am GUI",width = 50,bg = 'white',fg='black').grid(row =1,column=1)

Button(window,text = 'SUBMIT',width = 20, bg = 'red',fg = 'black').grid(row=1,column=0)




window.mainloop()


