import tkinter as tk
root = tk.Tk()
root.geometry("450x350")
# importing data from file
datas = open("C:/Users/user/Downloads/listvegetables.txt",'r')
sep_data = datas.readlines()
for data in range(1,len(sep_data)):
    val = sep_data[data].split(",")

    # Displaying vegetable name
    Veg1 = tk.Label(root,text = "Vegetable : " + f"{val[0]}")
    Veg1.pack()

    # Displaying Total quantity
    total_qn = tk.Label(root,text = "Total quantity : " + f"{val[1]}")
    total_qn.pack()

    # Displaying the selling Quantity
    selling_qn = tk.Label(root,text= "Selling quantity : "+f"{val[2]}")
    selling_qn.pack()

    # Displaying the total price
    price = tk.Label(root,text = "Amount : " + f"{val[3]}")
    price.pack()


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

def deliverylog():
    """
    Deliverylog module
    """
    import deliverylog

# direct towards the alter the availability module
alter_availability = tk.Button(root,text="Alter",command = alter,width=10)
alter_availability.pack()

# create a button for the history of orders module
hfo = tk.Button(root,text="History",command = HOF,width=10)
hfo.pack()

# This button is for directing towards deliverylog
dl = tk.Button(root,text="Delivery log",command = deliverylog,width=10)
dl.pack()
root.mainloop()