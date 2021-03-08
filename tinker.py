from tkinter import *
import sys
from github import Github
from getpass import getpass
from git import Repo
import os
import sys

def login(username,access_token):
    g = Github(access_token)

    try:
        repo_list = [i for i in g.get_user().get_repos()]
        print('\n')
        for i in repo_list:
            repo_name = str(i).replace('Repository(full_name="', '')
            repo_name = str(repo_name).replace('")', '')
            print('https://github.com/' + repo_name)
            login_success_screen = Toplevel()
            login_success_screen.title("Success")
            login_success_screen.geometry("150x100")
            Label(login_success_screen, text="Login Success").pack()
            
    except Exception as e:
        print('\nCredientials does not match')
        print(e)
        sys.exit()

def command1():
    if entry1.get == 'admin' and entry2.get()== 'password' or entry1.get() == 'test' and entry2.get == 'pass':
        root.deiconify()
        top.destroy()

def command2():
    top.destroy()
    root.destroy()
    sys.exit()
    
root = Tk()
top = Toplevel()

top.geometry('300x260')
top.title('Login to GitHub')
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

root.title('Saama Git Accelerator')
root.configure(background='white')
root.geometry('855x650')
root.withdraw()
root.mainloop()