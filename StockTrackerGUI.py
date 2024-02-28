import tkinter as Tk
import Interface

class MainWindow():  # class that defines how GUI should be made
    def __init__(self, master):  # making constructor
        self.master = master
        self.master.geometry("200x200")  # show how big do we want my window to be 

        self.lbl_tile =Tk.Label(master,text = "Title of my project")       # label object that holds the title to our actual window,pass in master to know what gui 
        self.lbl_tile.place(x=10, y=10)        # Place "title of my project onto the object"

        self.item_name =Tk.Label(master,text = "Item Name")      
        self.item_name.place(x=10, y=50)

        self.txt_item_name = Tk.Entry(master)       #tk.entry allow us to create the text field
        self.txt_item_name.place (x=10,y=70)

        self.buy_price =Tk.Label(master,text = "Buy price ")      
        self.buy_price.place(x=10, y=90)

        self.txt_buy_price = Tk.Entry(master)       #tk.entry allow us to create the text field
        self.txt_buy_price.place (x=10,y=110)

        self.sell_price =Tk.Label(master,text = "Sell price")      
        self.sell_price.place(x=10, y=130)

        self.txt_sell_price = Tk.Entry(master)       #tk.entry allow us to create the text field
        self.txt_sell_price.place (x=10,y=150)
        
        self.quantity =Tk.Label(master,text = "Quantity")      
        self.quantity.place(x=10, y=170)

        self.txt_quantity = Tk.Entry(master)       #tk.entry allow us to create the text field
        self.txt_quantity.place (x=10,y=190)

        self.btn_Enter = Tk.Button(master, text ="Enter", command = self.enter_to_db)                                        #make a button
        self.btn_Enter.place(x=10,y=230)

    def enter_to_db(self):         #take data from gui and pass to write function so it can update the database
        item_name = self.txt_item_name.get()        #get function pulls data is in the text field and return and store in item name
        buy_price = int(self.txt_buy_price.get())           #same but buy price is int 
        sell_price = int(self.txt_sell_price.get())
        quantity = int(self.txt_quantity.get())

        Interface.write_to_database(item_name,buy_price,sell_price,quantity)

root = Tk.Tk()
my_gui = MainWindow(root)  # mygui is = to that class 
root.mainloop()  # this is what makes the GUI run and appear on your screen.
