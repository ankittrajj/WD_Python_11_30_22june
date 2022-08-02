from tkinter import *

window = Tk()

window.title('python')


# create the function.
def click():
    enter_text = str(textentry.get())
    output.delete(0.0,END)


#     exceptional handling
    try:
        define = mydict[enter_text]
    except:
        define = 'not available'
    output.insert(END,define)

# textbox
textentry = Entry(window,width = 50,bg = 'red')
textentry.grid(row = 0 , column=0)

# label
Label(window,text = "I am GUI",width = 50,bg = 'white',fg='black').grid(row =1,column=1)

Button(window,text = 'SUBMIT',command=click,width = 20, bg = 'red',fg = 'black').grid(row=1,column=0)


# label
Label(window,text = 'Defenation', bg ='red',fg='black',font = 'none 12 bold').grid(row=1,column =2)

# o/p text box

output = Text(window,width = 40,height = 10,bg = 'white')
output.grid(row=0,column=3)


# create the data


mydict = {
    'animal':['dogs','cats'],
    'python': 'a useful prog. language'
}



window.mainloop()


