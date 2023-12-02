import tkinter as tk


class Vegetable:
    """ This class is to create different vegetable objects to sell"""


    _slots_ = ['_name' , '_total_available_quantity' , '_selling_quantity' , '_price']

    def _init_(self , name , total_qnty , selling_qunty , price):
        self._name = name
        if isinstance (total_qnty , int):       # --> Ensuring the total quantity not in negative
            assert(total_qnty > 0)
            self._total_available_quantity = total_qnty
        else:
            raise ValueError("please enter appropriate vlaue of total available quantity")
        self._selling_quantity = selling_qunty
        self._price = price
        
    def str(self):
        return str(self._name)


class LinkedList:
    """ This class is to create the linked list """


    class Node:
        """ This class is to create node object  for linked list"""

        _slots_ = "_item" , "_next"

        def init(self , item = None , next = None):
            """ This mwthod is to initialize the data members of Node class"""

            self._item = item
            self._next = next


    slots = "_head" , "_end" ,"_size"

    def _init_(self):
        """ This method is to initialize the datamembers of LinkedList class """

        self._head = self.Node()
        self._end = self._head
        self._size = 0

    def isempty(self):
        """ This methhod is to check whether the linkelist in empty or not"""
        return self._head == self._end
    
    def _str_(self):
        """ THis method is to display the items of the linkedlist"""

        if self.isempty():
            return "[]"
        ans = "["
        pos = self._head
        while pos._next is not None:
            ans += str(pos._next._item) + ","
            pos = pos._next
        return ans[:-1] + "]"
    
    def iter(self):
        """ This method is to make linkedlis as iterable object"""

        current_node = self._head
        while current_node is not None:
            yield current_node._item
            current_node = current_node._next

    
    def append(self , item):
        """ This method is to append the element at the end of the LinkedList"""

        new_node = self.Node(item)
        self._end._next = new_node
        self._end = new_node
        self._size += 1



    def delete(self , name):
        """ This class is to delete element in linked list"""

        pos = self._head
        while pos._next is not None:
            if pos._next._item._name == name :
                pos._next = pos._next._next
                self._size -= 1
                if pos._next == self._end:
                    self._end = pos
                break
            pos = pos._next



l1 = LinkedList()



def alter_availability( name , tot_qnty , sell_qnty , price):
    

    with open("C:/Users/user/Downloads/listvegetables.txt" , "r") as fi:
        lines = fi.read().split("\n")
        count = 0
        for line in lines:
            if not line.startswith(" "):
                count += 1
        add_veg = 1
        
        if count > 0:
            with open("C:/Users/user/Downloads/listvegetables.txt","w") as f:
                for line in lines:
                    written = False
                    for word in line.split(","):
                        if word == name:
                            f.write(str(name) + "," + str(tot_qnty) + ","+  str(sell_qnty) + "," + str(price) + ","+"\n")
                            written = True
                            add_veg -= 1
                            break
                    if written != True:
                        if (not line.startswith(" ")):
                            f.write(line + "\n")
                if add_veg == 1:
                    f.write(str(name) + "," + str(tot_qnty) + ","+  str(sell_qnty) + "," + str(price) + "," )
        elif count == 0:
            with open("C:/Users/user/Downloads/listvegetables.txt" , "a") as f:
                f.write(str(name) + "," + str(tot_qnty) + ","+  str(sell_qnty) + "," + str(price) + "," )

        


def submit():
    vegetable_name = vegetable_entry.get()
    total_quantity = int(total_quantity_entry.get())
    selling_quantity = int(selling_quantity_entry.get())
    price = int(price_entry.get())

    data = [vegetable_name, total_quantity, selling_quantity, price]
    return alter_availability(data[0] , data[1] , data[2] , data[3])

def hfo():
    """
    directing to the history of orders page
    """
    import historyoforders

def log():
    """
    directing to the delivery log
    """
    import deliverylog


def displays():
    """
    directing to the availability of vegetables
    """
    import displyvegetables


root = tk.Tk()

root.geometry("400x400")

vegetable_label = tk.Label(root, text="Vegetable name")
vegetable_entry = tk.Entry(root)

total_quantity_label = tk.Label(root, text="Total available quantity")
total_quantity_entry = tk.Entry(root)

selling_quantity_label = tk.Label(root, text="Selling quantity")
selling_quantity_entry = tk.Entry(root)

price_label = tk.Label(root, text="Price")
price_entry = tk.Entry(root)

submit_button = tk.Button(root, text="Submit", command=submit)

vegetable_label.pack()
vegetable_entry.pack()

total_quantity_label.pack()
total_quantity_entry.pack()

selling_quantity_label.pack()
selling_quantity_entry.pack()

price_label.pack()
price_entry.pack()

submit_button.pack(pady = 5)

# these buutton is for directing to another modules
hof1 = tk.Button(root,text = "History" , command = hfo,width=10)
hof1.pack(pady = 5)
display = tk.Button(root,text = "Availability",command = displays,width=10)
display.pack(pady = 5)
d1 = tk.Button(root,text = "Delivery Log",command=log,width= 10)
d1.pack(pady = 5)
root.mainloop()