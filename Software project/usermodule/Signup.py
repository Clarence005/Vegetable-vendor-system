import tkinter as tk
from tkinter import messagebox
class Signup:
    """
    Create a node
    """
    def __init__(self,user,password,email,cart = None,historyoforders = None):
        self._user = user
        self._password = password
        self._email = email
        self._cart = cart
        self._hoo = historyoforders

    def data(self):
        lst = [self._user , self._password , self._email,self._cart,self._hoo]
        return lst


def datastorage(username,password,email):
    """
    This function write the data in the txt file
    """
    D1 = Signup(username,password,email)
    lst = D1.data()
    print(lst)
    files = open("C:/Users/user/Downloads/Datastorage.txt",'a')
    for datas in lst:
        if(datas == None):
            files.write(str(datas)) # writing datas
            files.write(",")
        else:
            item = datas + ","
            files.write(item)
    files.write("\n")



def validate_signup():
    """
    This functions check the already an user or validate the passwords
    """
    username = entry_username.get()
    password = entry_password.get()
    email = entry_email.get()
    confirm_password = entry_confirm_password.get()
    check_user = open("C:/Users/user/Downloads/Datastorage.txt",'r')
    userid = []
    check = check_user.readlines()
    for i in check:
        ID = i.split(",")
        userid.append(ID[0])
    if username == '' or password == '' or confirm_password == '': # check wether the entry is empty or not
        messagebox.showwarning('Warning', 'Please fill in all fields.')
    # checks the both the password and reenter password are correct
    elif password != confirm_password:
        messagebox.showwarning('Warning', 'Passwords do not match.')
    elif username  in userid:
        messagebox.showwarning('warning','Userid is already taken')
    # if all are okay then shows signup sucessfully
    else:
        messagebox.showinfo('Success', 'Signup successful!')
        datastorage(username,password,email)
        # Perform further actions like saving the data or navigating to another page


def user():
    """
    This function directs the button back to the signin page
    """
    import Signin


root = tk.Tk()
root.title('Signup Page')
root.geometry("450x350")

# Username Label and Entry
label_username = tk.Label(root, text='Username:')
label_username.pack()
entry_username = tk.Entry(root)
entry_username.pack()


label_email = tk.Label(root,text = "Email:")
label_email.pack()
entry_email = tk.Entry(root)
entry_email.pack()

# Password Label and Entry
label_password = tk.Label(root, text='Password:')
label_password.pack()
entry_password = tk.Entry(root, show='*')
entry_password.pack()

# Confirm Password Label and Entry
label_confirm_password = tk.Label(root, text='Confirm Password:')
label_confirm_password.pack()
entry_confirm_password = tk.Entry(root, show='*')
entry_confirm_password.pack()

    
# Signup Button
button_signup = tk.Button(root, text='Signup',font = ('Bold',10) ,command=validate_signup)
button_signup.pack(pady = 10)

#Already have an account
already_user = tk.Label(root ,text = "Already have an account",font = ('Bold',10) )
already_user.pack()
signin = tk.Button(root, text="Signin", command = user)
signin.pack(pady = 10)

root.mainloop()
