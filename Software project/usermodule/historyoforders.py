import tkinter as tk

class Hfo:
    """
    This is stack representation to show the last place orders as first
    """
    def __init__(self):
        # Constructor
        self._order = []
        self._size = 0


    def push(self,val):
        """
        Appending the datas
        """
        self._order.append(val)
        self._size +=1


    def pop(self):
        """
        Removing the datas
        """
        poped_item = self._order[len(self._order)-1] # taking the last placed order
        del self._order[len(self._order)-1]
        return poped_item


    def isempty(self):
        """
        Check if the stack is empty or not
        """
        return len(self._order) == 0


    def display(self):
        for i in self._order:
            print(i)


def display_order_history(order_list):
    # Create a Tkinter window.
    root = tk.Tk()
    root.geometry("450x350")

    # Add a label to the window.
    label = tk.Label(root, text="Order History")
    label.pack()
    # Iterate through the order list and add a line for each order.
    for order in order_list:
        cart = tk.Label(root,text = "Order :" + order[0])
        cart.pack()
        for data in range(1,len(order)-1,2):
            line = tk.Label(root, text=f"Vegetable: {order[data]}")
            line.pack()
            quan = tk.Label(root,text=f"quantity :{order[data+1]}")
            quan.pack()
        price = tk.Label(root,text = f"Amount :{order[len(order)-1]}")
        price.pack()

    def direct():
        import linkedlist_vegetables


    # Directing to interface page
    directing = tk.Button(root,text = "Home",command=direct)
    directing.pack()

    # Add a Quit button to the window.
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady = 10)

    # Start the Tkinter mainloop.
    root.mainloop()


L = Hfo()
# Retriving datas from the file
history = open("C:/Users/user/Downloads/history.txt",'r')
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




