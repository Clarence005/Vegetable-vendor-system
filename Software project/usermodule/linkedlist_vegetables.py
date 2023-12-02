import tkinter as tk
from tkinter import messagebox
import random
class Vegetable:
    """ This class is to create different vegetable objects to sell"""


    __slots__ = ['_name' , '_total_available_quantity' , '_selling_quantity' , '_price']

    def __init__(self , name , total_qnty , selling_qunty , price):
        self._name = name
        if isinstance (total_qnty , int):       # --> Ensuring the total quantity not in negative
            assert(total_qnty > 0)
            self._total_available_quantity = total_qnty
        else:
            raise ValueError("please enter appropriate vlaue of total available quantity")
        self._selling_quantity = selling_qunty
        if isinstance(price , int):             # --> Ensuring the price is  not in negative
            assert (price > 0)
            self._price = price
        else:
            raise ValueError("please enter appropriate price ")
        
    def __str__(self):
        return str(self._name)





class LinkedList:
    """ This class is to create the linked list """


    class Node:
        """ This class is to create node object  for linked list"""

        __slots__ = "_item" , "_next"

        def __init__(self , item = None , next = None):
            """ This mwthod is to initialize the data members of Node class"""

            self._item = item
            self._next = next


    __slots__ = "_head" , "_end" ,"_size"

    def __init__(self):
        """ This method is to initialize the datamembers of LinkedList class """

        self._head = self.Node()
        self._end = self._head
        self._size = 0

    def isempty(self):
        """ This methhod is to check whether the linkelist in empty or not"""
        return self._head == self._end
    
    def __str__(self):
        """ THis method is to display the items of the linkedlist"""

        if self.isempty():
            return "[]"
        ans = "["
        pos = self._head
        while pos._next is not None:
            ans += str(pos._next._item) + ","
            pos = pos._next
        return ans[:-1] + "]"
    
    def __iter__(self):
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




#-------------------------------------------------------------------------------------------------------------------#
""" This Program is to give purcase details of user to order Module """


def add_to_cart(name):
    veg = l1._head
    while veg._next is not None:
        if veg._next._item._name == name:
            if veg._next._item._selling_quantity <= veg._next._item._total_available_quantity:
                veg._next._item._total_available_quantity -= veg._next._item._selling_quantity
                return [veg._next._item._name , veg._next._item._selling_quantity , veg._next._item._price]
            else:
                raise ValueError("Out of stock")
        veg = veg._next





#---------------------------------------------------------------------------------------------------------------------#
class ShoppingSystem:
    """
    This class is for frontend
    """
    def __init__(self, master , list):
        # constructor
        self.master = master
        self.master.title("Shopping System")
        self._l1 = list
        self.shopping_cart = []
        self.val = []
        self.price = []
        self.selected_items = None
        self.sellingqun = []
        self.item = []
        # Create a dictionary to store item prices
        item_dict = { }
        kk = 0
        for i in self._l1:
            if kk != 0: 
                k = i._name + "--->" +"Quantity:"+str(i._total_available_quantity)+"--->"+"Rs" + str(i._price)
                val = [i._selling_quantity ]
                self.item.append(i._name)
                self.item.append(i._total_available_quantity)
                self.item.append(i._selling_quantity)
                self.item.append(i._price)
                self.sellingqun.append(val)
                item_dict[k] = val
            kk += 1
        self.item_prices = item_dict

        # Initialize shopping cart

        # Create the item selection list
        notify = tk.Label(self.master,text = "only per kg to be selected")
        notify.pack()
        self.item_listbox = tk.Listbox(self.master, selectmode=tk.MULTIPLE,height = 12,width = 30)
        for item in self.item_prices:
            self.item_listbox.insert(tk.END, item)
        self.item_listbox.pack()

        # Create the "Add to Cart" button
        self.add_to_cart_btn = tk.Button(self.master, text="Add to Cart", command=self.add_to_cart,width=12)
        self.add_to_cart_btn.pack()

        # Create the shopping cart listbox
        self.shopping_cart_listbox = tk.Listbox(self.master,height = 12,width = 30)
        self.shopping_cart_listbox.pack()

        # Create the "Checkout" button
        self.checkout_btn = tk.Button(self.master, text="Checkout", command=self.checkout,width=12)
        self.checkout_btn.pack(pady = 4)

        # patement button directs to pament module
        self.payment_btn = tk.Button(self.master, text="Place order", command=self.payement,width=12)
        self.payment_btn.pack(pady = 4)

        # Create the clear button to clear the data
        self.clear_btn = tk.Button(self.master,text = "Proceed to pay", command=self.clear_fn,width=12)
        self.clear_btn.pack(pady = 4)

        self.historyofoorders = tk.Button(self.master,text = "Order history",command= self.showorder,width = 12)
        self.historyofoorders.pack(pady = 4)
        # Quit button closes the app
        self.quit_button = tk.Button(self.master, text="Quit", command=root.quit)
        self.quit_button.pack(pady = 4)

        # Create the total cost label
        self.total_cost_label = tk.Label(self.master, text="Total Cost: $0.00")
        self.total_cost_label.pack(pady = 4)


    def add_to_cart(self):
        # Get the selected items from the listbox
        self.selected_items = [self.item_listbox.get(index) for index in self.item_listbox.curselection()]

        # Add selected items to the shopping cart
        for item in self.selected_items:
            self.shopping_cart.append(item)
            self.shopping_cart_listbox.insert(tk.END, item)


    def clear_fn(self):
        from Address import run_this_file
        run_this_file()


    def checkout(self):
        # Calculate the total cost
        for i in self.shopping_cart:
            value = i.split("--->Rs")
            g = value[0].split("--->Quantity:")
            self.val.append(g[0])
            self.price.append(int(value[1]))
        total_cost = 0
        for j in self.price:
            total_cost += j

        # Update the total cost label
        self.total_cost_label.config(text="Total Cost: ${:.2f}".format(total_cost))

        # Clear the shopping cart
        self.shopping_cart = []
        self.shopping_cart_listbox.delete(0, tk.END)


    def payement(self):
        # from Address import run_this_file
        # run_this_file()
        """
        This function stores our ordered data in a list
        """
        total_cost = 0
        item = {}
        for l in self.price:
            total_cost += l
        for i in self.val:
            if i in item:
                item[i] += 1
            else:
                item[i] = 1

        # Display warning when the totalcost is less than 100
        if(total_cost<100):
            messagebox.showwarning('Warning', 'Add more items')
        
        # Writing datas into the payement file
        else:
            pay = open("C:/Users/user/Downloads/payeement.txt",'a')
            for j in item:
                pay.write(j)
                pay.write(",")
                pay.write(str(item[j]))
                pay.write(",")
            pay.write(str(total_cost))

            # Wiriting data to both user and owner history of orders file
            history = open("C:/Users/user/Downloads/history.txt",'a')
            ownerhistory = open("C:/Users/user/Downloads/ownerhistory.txt",'a')
            a= random.randint(11000,99999)
            history.write(str(a) +",")
            ownerhistory.write(str(a)+",")
            for k in item:
                history.write(k)
                ownerhistory.write(k)
                history.write(",")
                ownerhistory.write(",")
                history.write(str(item[k]))
                ownerhistory.write(str(item[k]))
                history.write(",")
                ownerhistory.write(",")
            history.write(str(total_cost))
            ownerhistory.write(str(total_cost))
            history.write("\n")
            ownerhistory.write(",")

            # if the quantity goes below 0 removes item from the display box
            for m in item:
                for n in range(0,len(self.item),4):
                    if(m == self.item[n]):
                        change = item[m]
                        self.item[n+1] = self.item[n+1] - change
            b = open("C:/Users/user/Downloads/listvegetables.txt",'w')
            b.close()
            al = open("C:/Users/user/Downloads/listvegetables.txt",'a')
            al.write("veg,total,selling,price"+"\n")
            for d in range(0,len(self.item),4):
                if(self.item[d+1] != 0):
                    al.write(self.item[d]+",")
                    al.write(str(self.item[d+1])+",")
                    al.write(str(self.item[d+2])+",")
                    al.write(str(self.item[d+3]))
                    al.write("\n")
        
    def showorder(self):
        """
        Directing to the history of orders 
        """
        import historyoforders


# Create the main window
root = tk.Tk()
root.geometry("450x350")

def adding(l1):
    list_veg = open("C:/Users/user/Downloads/listvegetables.txt",'r')
    val = list_veg.readlines()
    for i in range(1,len(val)):
        veg = val[i].split(",")
        i1 = veg[0]
        i2 = int(veg[1])
        i3 = int(veg[2])
        i5 = ""
        for j in veg[3]:
          if(j != "/" or j != "n"):
            i5 += j
        i4 = int(i5)
        v1 = Vegetable(i1,i2,i3,i4)
        l1.append(v1)


l1 = LinkedList()
adding(l1)
# Create the shopping system
shopping_system = ShoppingSystem(root , l1)

# Run the main loop
root.mainloop()

