from tkinter import *
import sys
from github import Github
from getpass import getpass
from git import Repo
import os
import sys
from tkinter import messagebox
from tkinter.scrolledtext import *
import tkinter as tk
def login(username,access_token):
    g = Github(access_token)
    try:
        repo_list = [i for i in g.get_user().get_repos()]
        print('\n')
        display_list=[]
        for i in repo_list:
            repo_name = str(i).replace('Repository(full_name="', '')
            repo_name = str(repo_name).replace('")', '')
            display_list.append('https://github.com/' + repo_name)
        display=ScrolledText(top,height=5)
        display.grid(column=0,pady=10,padx=10)
        print(display_list)
        display.insert(tk.INSERT,display_list)
    except Exception as e:
        messagebox.showinfo(title="git accelerator",message="Credientials does not match")
        print('\nCredientials does not match')
        print(e)
        sys.exit()
    
root = Tk()
top = Toplevel()

top.geometry('750x450')
top.title('Saama Git Accelerator')
top.configure(background='white')
photo = PhotoImage(file='1.gif')
photo1 = Label(top,image=photo,bg='white')
lbl1 = Label(top,text='Username:',font =('Helevtica',10))
entry1 = Entry(top)
lbl2 = Label(top,text='Password:',font =('Helevtica',10))
entry2 = Entry(top,show='*')
button1 = Button(top, text= 'Login',command=lambda:login(entry1.get(),entry2.get()))

photo1.pack()
lbl1.pack()
entry1.pack()
lbl2.pack()
entry2.pack()
button1.pack()

root.title('')
root.configure(background='white')
root.geometry('855x650')
root.withdraw()
root.mainloop()