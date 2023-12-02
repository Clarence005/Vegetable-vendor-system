import tkinter as tk
def run_this_file():
    def save_address():
        """
        This functions save the address in the file
        """
        flat_number = flat_entry.get()
        street_name = street_entry.get()
        place_name = place_entry.get()
        district_name = district_entry.get()
        history = open("C:/Users/user/Downloads/ownerhistory.txt",'r')
        full_address = "Address : " + f"{flat_number}, {street_name}, {place_name}, {district_name}," +"\n"
        history = open("C:/Users/user/Downloads/ownerhistory.txt",'a')
        history.write(full_address)
        print("Full Address:", full_address)
        # You can save the full address to a file or perform any other desired action
        
    def direct():
        """
        This function direct the page to the proceedtopay module
        """
        import proceed_to_pay

    # Create the main window
    window = tk.Tk()
    window.geometry("450x350")
    window.title("Enter the  Address")

    # Create labels and entry fields for the address components
    flat_label = tk.Label(window, text="Flat Number:")
    flat_label.pack()

    flat_entry = tk.Entry(window)
    flat_entry.pack()

    #creating the label for the streetname
    street_label = tk.Label(window, text="Street Name:")
    street_label.pack()

    # # Creating an entry for street name
    street_entry = tk.Entry(window)
    street_entry.pack()

    # Creating an label for place name
    place_label = tk.Label(window, text="Place Name:")
    place_label.pack()

    # Creating an entry for place name
    place_entry = tk.Entry(window)
    place_entry.pack()

    # Creating an label for district
    district_label = tk.Label(window, text="District Name:")
    district_label.pack()

    # Creating an entry for district
    district_entry = tk.Entry(window)
    district_entry.pack()

    # Create a button to save the address
    save_button = tk.Button(window, text="Save Address", command=save_address,width = 10)
    save_button.pack()

    payement = tk.Button(window,text = "Pay",command = direct,width =10)
    payement.pack(pady = 4)

    # Start the main event loop
    window.mainloop()
