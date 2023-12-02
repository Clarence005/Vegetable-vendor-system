class Hfo:
    """
    This class is basicaly to show the deliverylog by lastin firstout
    """
    def __init__(self):
        # Constructor
        self._order = []
        self._size = 0

    def enqueue(self,val):
        """
        Adding elements to the last of the queue
        """
        self._order.append(val)
        self._size +=1


    def dequeue(self):
        """
        Removing the first element from the queue
        """
        dequeueed_item = self._order[0]
        del self._order[0]
        return dequeueed_item


    def isempty(self):
        """
        Check wether the queue is empty or not
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
    cart = tk.Label(root,text = "Delivery Log:")
    cart.pack()
    # Iterate through the order list and add a line for each order.
    for order in order_list:
        label = tk.Label(root, text="Order : " + order[0])
        label.pack()
        num = find(order)
        for data in range(1,num-1,2):
            line = tk.Label(root, text=f"Vegetable: {order[data]}   quantity : {order[data+1]}")
            line.pack()
        print(order[num-1])
        # This label is for displaying the total cost
        price = tk.Label(root,text = "Amount : Rs."+f"{order[num-1]}")
        price.pack()

        # This label is for displaying the Address
        Add = tk.Label(root,text =  f"{order[num]}" + ",")
        Add.pack()
        street_name = tk.Label(root,text = "Street name : " + f"{order[num+1]}"+ ",")
        street_name.pack()
        place = tk.Label(root,text = "Place name" + f"{order[num+2]}" + ",")
        place.pack()
        district = tk.Label(root,text = "District : " + f"{order[num+3]}")
        district.pack()

    # direct towards the alter the availability module
    alter_availability = tk.Button(root,text="Alter",command = alter,width=10)
    alter_availability.pack(pady = 2)

    # create a button for the history of orders module
    hfo = tk.Button(root,text="History",command = HOF,width=10)
    hfo.pack(pady = 2)

    # This button is for directing towards deliverylog
    dl = tk.Button(root,text="Vegetables",command = vegetables,width=10)
    dl.pack(pady = 2)

    # Add a Quit button to the window.
    quit_button = tk.Button(root, text="Quit", command=root.quit)
    quit_button.pack(pady = 2)

    # Start the Tkinter mainloop.
    root.mainloop()


def alter():
    """
    Directing to the alter module
    """
    import ALterthevegetables


def HOF():
    """
    Directing to the history bof orders
    """
    import historyoforders


def vegetables():
    """
    Directing to the Display the availability of vegetables module
    """
    import displyvegetables

def find(lst):
    count = 0
    for i in lst:
        if(i.startswith("Address")):
            return count
        else:
            count += 1
L = Hfo()
# opening ownerhistoryfile in read mode
history = open("C:/Users/user/Downloads/ownerhistory.txt",'r')
val = history.readlines()
order_list = []
for i in val:
    lst = []
    lst.append(i)
    # enqueue all the orders  to the list
    L.enqueue(lst)
while(not L.isempty()):
    val = L.dequeue()
    veg = val[0].split(",")
    order_list.append(veg)
    
    # Create an order list.

# Display the order history.
print(order_list)
display_order_history(order_list)
root = tk.Tk()
