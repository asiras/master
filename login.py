from tkinter import *

#--------------------------------------------------------------------------------------------------------------
#create the window and add size and title to it
window = Tk()
window.geometry("800x500+300+100")
#set size permanently   #or you can use window.resizabld(false, false)
window.minsize(800, 500)
window.maxsize(800, 500)
window.title(" Saama Git Accelerator")

#-------------------------------------------------------------------------------------------------------------
#functions for the buttons to perform
def login():
    users = {'admin': '1000', 'dev': '2000', 'client': '3000', 'employee': '4000'}
    username = userName.get()
    Pass = Authenticationtoken.get()
    if username in users :
        if (users[username] == Pass):
            label4 = Label(window, text = ("Welcome " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)
            
        else:
            label4 = Label(window, text = ("Incorrect Authenticationtoken for " + username),width = 25, font = ("arial", 40, "bold"))
            label4.place(x = 0, y = 400)

    else:
        label4 = Label(window, text = (username + " does not exist"),width = 25, font = ("arial", 40, "bold"))
        label4.place(x = 0, y = 400)

#----------------------------------------------------------------------------------------------------------------
#first lable
label1 = Label(window, text = " Login to GitHub ", fg = "black", font = ("new times roman", 18))
label1.place(x = 0, y = 10)

label2 = Label(window, text = "User Name :", font = ("arial", 12))
label2.place(x = 110, y = 150)

userName = StringVar()
textBox1 = Entry(window, textvar = userName, width = 30, font = ("arial", 12))
textBox1.place(x = 290, y = 150)

label3 = Label(window, text = "Authentication token :", font = ("arial", 12))
label3.place(x = 116, y = 250)

Authenticationtoken = StringVar()
textBox2 = Entry(window, textvar = Authenticationtoken, width = 30, font = ("arial", 12))
textBox2.place(x = 290, y = 250)

button1 = Button(window, text = "   Login   ", fg = "black", bg = "white", relief = "raised", font = ("arial", 12), command = login)
button1.place(x = 335, y = 340)

#display window
window.mainloop()
