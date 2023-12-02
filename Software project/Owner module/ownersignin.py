import ctypes
import tkinter as tk
class Signin:
    """
    This class is basicaly an hashtable to store the data
    """
    class Node:
        """
        Creating a node
        """
        def __init__(self,user,password,email,cart = None,historyoforders = None):
                self.user = user
                self.password = password
                self.email = email
                self.cart = cart
                self.hoo = historyoforders


    def __init__(self,capacity):
        self._capacity = capacity
        self._hashtable = (ctypes.py_object * self._capacity)()
        self._size = 0
        # Constructor for the hashtable
    

    def hashval(self,val):
        # returns the index
        index = 0
        num = hash(val)
        index += num % self._capacity
        return index


    def isfull(self):
        """
        Check the hash table is full or not
        """
        return self._size == self._capacity
    
    def resize(self):
        """
        if the hashtable is full then resize the table
        """
        if(self.isfull()):
            self._capacity = self._capacity*2
            temp = (ctypes.py_object * self._capacity)()
        for i in range(self._size):
            temp[i] = self._hashtable[i]
        self._hashtable = temp


    def dataretrive(self):
        """
        Retriving the data from the file
        """
        file = open("C:/Users/user/Downloads/ownerdata.txt",'r')
        datas = file.readlines()
        retrive = []
        for j in datas:
            data = j.split(",")
            userid = data[0]
            retrive.append(userid)
            password = data[1]
            retrive.append(password)
            email = data[2]
            retrive.append(email)
            cart = data[3]
            retrive.append(cart)
            history = data[4]
            retrive.append(history)
        return retrive # returns the retrive data


    def setitem(self):
        """
        Setting the item in the hashtable based on the index
        """
        data = self.dataretrive()
        for i in range(0,len(data),5):
            key = data[i]
            val = data[i+1]
            email = data[i+2]
            cart = data[i+3]
            hoo = data[i+4]
            u1 = self.Node(key,val,email,cart,hoo)
            index = self.hashval(u1.user)
            print(index)
            if(self.isfull()):
                self.resize()
            self._hashtable[index] = u1
        self._size += 1


    def __getitem__(self,key):
        """
        Gets the item by te index value
        """
        self.setitem()
        index = self.hashval(key)
        print(index)
        return self._hashtable[index]


    def check(self,key,val):
        """
        Checks the the key and val are matched
        """
        pasword = self.__getitem__(key)
        if(val == pasword.password):
            return True
        else:
            return False


def login():
    """
    This function basicaly works for checking key and value 
    """
    username = username_entry.get()
    password = password_entry.get()
    Val = Signin(100)
    if Val.check(username,password):
        message_label.config(text="Login successful") # returns the message login sucessful
        import displyvegetables
    else:
        message_label.config(text="Login failed")



def sign():
    """
    Moves to Signup page
    """
    import ownersignup


# Create the main window
window = tk.Tk()
window.title("Sign-In Page")
window.geometry("450x350")

# Create labels and entries for username and password
username_label = tk.Label(window, text="Username:")
username_label.pack()
username_entry = tk.Entry(window)
username_entry.pack()

password_label = tk.Label(window, text="Password:")
password_label.pack()
password_entry = tk.Entry(window, show="*")
password_entry.pack()

# Create a login button
login_button = tk.Button(window, text="Login", command=login)
login_button.pack()
dis = tk.Label(window,text = "Don't have an account")
dis.pack()

# Goes to Signup page
signup = tk.Button(window,text="Signup",command=sign)
signup.pack()


# Create a label to display messages
message_label = tk.Label(window, text="")
message_label.pack()
# Start the main event loop
window.mainloop()



