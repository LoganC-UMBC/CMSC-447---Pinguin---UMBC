from tkinter import *
import os

class login_screen:
    def __init__(self):
        self.start()

    def register_user(self):
        username_info = self.username.get()
        password_info = self.password.get()

        if username_info != '' and password_info != '':
            filename = username_info+".txt"

            if not os.path.exists(filename):
                with open(filename,'w') as file:
                    file.write(username_info+'\n')
                    file.write(password_info)
                    file.close()
                    self.status_text.set('Registration succeeded')
                    self.register_status['fg'] = 'green'
            else:
                self.status_text.set('Registration failed (username already exists)')
                self.register_status['fg'] = 'red'
        else:
            self.status_text.set('Registration failed (missing entry)')
            self.register_status['fg'] = 'red'

        self.username_entry_reg.delete(0,END)
        self.password_entry_reg.delete(0,END)

    def register(self):
        register_screen = Toplevel(self.main_screen)
        register_screen.title("Pinguin Account Registration")
        register_screen.geometry("300x250")
        register_screen.resizable(False,False)

        self.username = StringVar()
        self.password = StringVar()

        Label(register_screen, text="Please enter details below").pack()
        Label(register_screen,text="").pack()

        Label(register_screen,text="Username *").pack()
        self.username_entry_reg = Entry(register_screen,textvariable=self.username)
        self.username_entry_reg.pack()

        Label(register_screen,text="Password *").pack()
        self.password_entry_reg = Entry(register_screen,textvariable=self.password,show='*')
        self.password_entry_reg.pack()
        Label(register_screen, text="").pack()

        Button(register_screen, text="Register", width="10", height="1",command=self.register_user).pack()
        self.status_text = StringVar()
        self.status_text.set('')
        self.register_status = Label(register_screen,textvariable=self.status_text,font=("Calibri",9))
        self.register_status.pack()

    def login_user(self):
        username_info = self.username.get()
        password_info = self.password.get()

        if username_info != '' and password_info != '':
            filename = username_info + ".txt"

            if os.path.exists(filename):
                with open(filename, 'r') as file:
                    file.readline()
                    password = file.readline()
                    if password == password_info:
                        print("logged in!")
                    else:
                        print("wrong password")

                    file.close()

            else:
                print("account doesn't exist")

        else:
            print("missing entry")

        self.username_entry_log.delete(0, END)
        self.password_entry_log.delete(0, END)


    def login(self):
        login_screen = Toplevel(self.main_screen)
        login_screen.title("Pinguin Account Registration")
        login_screen.geometry("300x250")
        login_screen.resizable(False, False)

        self.username = StringVar()
        self.password = StringVar()

        Label(login_screen, text="Please enter details below").pack()
        Label(login_screen, text="").pack()

        Label(login_screen, text="Username").pack()
        self.username_entry_log = Entry(login_screen, textvariable=self.username)
        self.username_entry_log.pack()

        Label(login_screen, text="Password").pack()
        self.password_entry_log = Entry(login_screen, textvariable=self.password, show='*')
        self.password_entry_log.pack()
        Label(login_screen, text="").pack()

        Button(login_screen, text="login", width="10", height="1", command=self.login_user).pack()

    def start(self):
        self.main_screen = Tk()
        self.main_screen.geometry("300x250")
        self.main_screen.title("Pinguin Account Login")
        self.main_screen.resizable(False,False)

        Label(text = "test", bg = "grey", width="300", height="2",font = ("Calibri",13)).pack()
        Label(text="").pack()

        Button(text = "Login", height="2", width="30", command=self.login).pack()
        Label(text="").pack()

        Button(text = "Register", height="2", width="30", command=self.register).pack()
        Label(text="").pack()

        self.main_screen.mainloop()

if __name__ == '__main__':
    login_screen()