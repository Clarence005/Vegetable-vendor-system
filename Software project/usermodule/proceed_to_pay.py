import tkinter as tk
import datetime
import smtplib


def payment_successful():
    """
    This functions shows our order and delivery time and Notification to the user mail
    """
    label = tk.Label(root, text="Payment Successful!")
    label.pack()
    pay = open("C:/Users/user/Downloads/payeement.txt",'r')
    items = pay.readlines()
    for i in items:
        value = i.split(",")
    veg = []
    quan= []
    # displaying orders
    for i in range(0,len(value)-1,2):
        veg.append(value[i])
        quan.append(value[i+1])
    payment = open("C:/Users/user/Downloads/payeement.txt",'w')
    payment.close()
    # Displaying Delivery time
    current_time = datetime.datetime.now()
    tim = str(current_time.time())
    dt = tim.split(":")
    hrs = int(dt[0])
    minutes = dt[1]
    finaltm = hrs + 2
    deliverytime = str(finaltm)+":"+minutes
    del_time = tk.Label(root,text =f"Delivery time : {deliverytime}")
    del_time.pack()
    sendmail(value) # calling the send mail function to send notification
 

def dummy_payment():
    payment_successful()


def sendmail(value):
    """
    Sending mail through mail id
    """
    data = ""
    print(value)
    for i in range(0,len(value)-1,2):
        data +=  "Vegetable : " + value[i] + "\n" + "Quantity : " + value[i+1]+"\n"
    data += "Totalcost : "+ "RS : " + value[len(value)-1] + "\n"
    data += "your Order is sucessfull"
    print(data)
    myemail = 'greenbox5678@gmail.com'
    passwords = 'jejgnwwamadrbxvq' #worg nlex uhtc gthy
    # creates SMTP session
    server = smtplib.SMTP('smtp.gmail.com', 587)
    
    # start TLS for security
    server.starttls()
    
    # Authentication
    server.login(user=myemail,password = passwords)
    
    # message to be sent
    mail = open("C:/Users/user/Downloads/email.txt",'r')
    sendermail = mail.read()
    # sending the mail
    server.sendmail(myemail, sendermail, data)
    server.close()

def direct():
    import historyoforders
    # Create a Tkinter window.
root = tk.Tk()
root.geometry("450x350")
# Add a label to the window.
label = tk.Label(root, text="Your Cart",font=('Bold',10))
label.pack()

# Add a list of vegetables to the window.
pay = open("C:/Users/user/Downloads/payeement.txt",'r')
items = pay.readlines()
for i in items:
    val = i.split(",")
vegetables = []
quantity = []
for i in range(0,len(val)-1,2):
    vegetables.append(val[i])
    quantity.append(val[i+1])
# Displaying the orders
for vegetable in range(len(vegetables)):
    line = tk.Label(root, text=f"veg:{vegetables[vegetable]}",font=('Bold',12))
    line.pack()
    quan = tk.Label(root,text=f"quantity:{quantity[vegetable]}",font=('Bold',12))
    quan.pack()
price = tk.Label(root,text=f"Amount:{val[len(val)-1]}",font=('Bold',12))
price.pack()


# Add a dummy payment button to the window.
payment_button = tk.Button(root, text="Pay", command=dummy_payment,font=('Bold',10),width= 12)
payment_button.pack(pady = 10)

# Directing to Home page
home = tk.Button(root, text = "History",command = direct,font=('Bold',10),width= 12)
home.pack(pady = 10)


quit_button = tk.Button(root, text="Quit", command=root.quit,font=('Bold',10),width= 12)
quit_button.pack(pady = 10)

# Start the Tkinter mainloop.
root.mainloop()


# terminating the sessio