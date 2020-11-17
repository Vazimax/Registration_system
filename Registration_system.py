from tkinter import *

def register_user():
    username_info = username.get()
    password_info = password.get()

    file = open(f"{username_info}.txt","w")
    file.write(f"The user name is {username_info}\n")
    file.write(f"The password is {password_info}")
    file.close()

    username_input.delete(0, END)
    password_input.delete(0, END)

    Label(screen1,text="The Registration is successful",fg="green").pack()

def register():
    global screen1
    screen1 = Toplevel(screen)
    screen1.geometry("400x300")
    screen1.title("Register")

    global username
    global password
    username = StringVar()
    password = StringVar()

    global username_input
    global password_input
    Label(screen1,text="PLease enter the information :").pack()
    Label(screen1,text="").pack()
    Label(screen1,text="Username * ").pack()
    username_input = Entry(screen1,textvariable=username)
    username_input.pack()
    Label(screen1,text="Password * ").pack()
    password_input = Entry(screen1,textvariable=password)
    password_input.pack()
    Label(screen1,text="").pack()
    Button(screen1, text="Register",width=20, command=register_user).pack()

def main_screen():
    global screen
    screen = Tk()
    screen.geometry("400x300")
    screen.title("Registration")
    Label(text="Registration System", bg="black",width="400",height="2",fg="white",font=("Courier")).pack()
    Label(text="").pack()
    Button(text='Register',width="20",command= register).pack()

    screen.mainloop()

main_screen()