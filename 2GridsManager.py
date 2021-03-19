from tkinter import *
root=Tk()
root.title("Saama Git Accelerator")
root.geometry('500x300')

label1=Label(root,text='', borderwidth=1, relief="solid",fg='black',bg='white',font=('Arial',16))
label1.pack(padx=100,side=LEFT,ipadx=200,ipady=200)
 
label2=Label(root,text='', borderwidth=1, relief="solid",fg='black',bg='white',font=('Arial',16))
label2.pack(padx=100,side=RIGHT,ipadx=200,ipady=200)

btn1 = Button(root, text = 'Logo Here!', fg ="black",bg ="light blue", 
                command = root.destroy) 
 
btn1.place(x=25,y=25)

btn2 = Button(root, text = 'Commit Files!', fg ="black",bg ="light blue", 
                command = root.destroy) 
 
btn2.place(x=120,y=26)


btn3 = Button(root, text = 'Download Files!', fg ="black",bg ="light blue", 
                command = root.destroy) 
 
btn3.place(x=220,y=26)

btn4 = Button(root, text = 'Browse Files!', fg ="black",bg ="light blue", 
                command = root.destroy) 
 
btn4.place(x=230,y=100)

btn5 = Button(root, text = 'Repository List!', fg ="black",bg ="light blue", 
                command = root.destroy) 
 
btn5.place(x=135,y=105)

root.mainloop() 
