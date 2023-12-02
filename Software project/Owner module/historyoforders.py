class Hfo:
    """
    This class is basicaly to display the last place order by stack
    """
    def __init__(self):
        #constructor
        self._order = []
        self._size = 0


    def push(self,val):
        """
        Appending element at the lost
        """
        self._order.append(val)
        self._size +=1


    def pop(self):
        """
        Removing the last element from the stack
        """
        poped_item = self._order[len(self._order)-1]
        del self._order[len(self._order)-1]
        return poped_item


    def isempty(self):
        """
        Check wether the stack is empty or not
        """
        return len(self._order) == 0


    def display(self):
        for i in self._order:
            print(i)


import tkinter as tk

def display_order_history(order_list):
    # Create a Tkinter window.
    root = tk.Tk()
    root.geometry("450x350")

    # Add a label to the window.
    label = tk.Label(root, text="Order History")
    label.pack()
    # Iterate through the order list and add a line for each order.
    for order in order_list:
        cart = tk.Label(root,text = "Order : " + order[0])
        cart.pack()
        num =  find(order)
        for data in range(1,num-1,2):
            line = tk.Label(root, text=f"Vegetable: {order[data]}")
            line.pack()
            quan = tk.Label(root,text=f"quantity :{order[data+1]}")
            quan.pack()
        price = tk.Label(root,text = f"Amount : Rs.{order[num-1]}")
        price.pack()


    
    # direct towards the alter the availability module
    alter_availability = tk.Button(root,text="Alter",command = alter,width=10)
    alter_availability.pack(pady = 2)

    # create a button for the history of orders module
    hfo = tk.Button(root,text="Deliverylog",command = HOF,width=10)
    hfo.pack(pady = 2)

    # This button is for directing towards deliverylog
    dl = tk.Button(root,text="Vegetables",command = vegetables,width=10)
    dl.pack(pady = 2)

    # Add a Quit button to the window.
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady = 2)

    # Start the Tkinter mainloop.
    root.mainloop()


def find(lst):
    """
    This function is for finding the index of Address
    """
    count = 0
    for i in lst:
        if(i.startswith("Address")):
            return count
        count += 1


def alter():
    """
    Directing to the alter module
    """
    import ALterthevegetables


def HOF():
    """
    Directing to the history bof orders
    """
    import deliverylog


def vegetables():
    """
    Directing to the Display the availability of vegetables module
    """
    import displyvegetables


L = Hfo()
history = open("C:/Users/user/Downloads/ownerhistory.txt",'r')
val = history.readlines()
order_list = []
for i in val:
    lst = []
    lst.append(i)
    L.push(lst)
while(not L.isempty()):
    val = L.pop()
    for j in val:
        veg = j.split(",")
        order_list.append(veg)

    # Create an order list.

# Display the order history.
display_order_history(order_list)
root = tk.Tk()
root.geometry("450x350")




