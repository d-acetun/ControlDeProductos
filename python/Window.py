# import tkinter as tk
import imp
from math import prod
from tkinter import ttk
from tkinter import *
from DataBase import DataBase
import pymysql
class Window:
    def __init__(self, window):
        self.window = window
        self.window.title('Products Aplication')
        self.window['bg'] = 'skyblue1'
        self.window.protocol('WM_DELETE_WINDOW', self.close_window)
        self.Database = DataBase()
        Grid.rowconfigure(window, (0,1,2), weight=1)

        Grid.columnconfigure(window, (0), weight=1)
        
        
        font=('Arial', '10', 'bold')

        # self.window.configure(background='black')
        width = 400
        height = 600
        x = self.window.winfo_screenwidth() // 2 - width // 2
        y = self.window.winfo_screenheight() // 2 - height // 2
        posicion = str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y)
        self.window.geometry(posicion)
        # self.window['bg'] = 'pink'
        # self.window.state('zoomed')
        #Asi se puede cambiar el color de fondo
        # frameForm = Frame(self.window, width=400, height=400)
        #primero cambiar color y despues ponerle el grid
        # frameForm['bg'] = 'red'
        frameForm = Frame(self.window)
        # frameForm['bg'] = 'green'
        frameForm.grid(row=0, column=0, sticky=N)

        # frameForm['bg'] = 'red'
        Label(frameForm, text='Name', font=font).grid(row=0, column=0)

        Label(frameForm, text='Price', font=font).grid(row=1, column=0)

        Label(frameForm, text='Quantity', font=font).grid(row=2, column=0 , padx=10)

        self.entryName = Entry(frameForm, width=30, font=font)
        self.entryName.focus()
        self.entryName.grid(row=0, column=1, pady=10, padx=10)
        self.entryPrice = Entry(frameForm, width=30, font=font)
        self.entryPrice.grid(row=1, column=1, padx=10)
        self.entryQuantity = Entry(frameForm, width=30, font=font)
        self.entryQuantity.grid(row=2, column=1, pady=10, padx=10)
        
        #* EW PARA EXTENDER HORIZONTALMENTE
        #* NS PARA EXTENDER VERTICALMENTE
        #* NSEW PARA EXTENDER EN TODAS LAS DIRECCIONES
        #* columnspan indica que se extiende en todas las columnas
        style = ttk.Style()
        style.configure("G.TButton", foreground="green", font=font)
        ttk.Button(frameForm, text="ADD", style="G.TButton", command=self.add_product).grid(row=3, column=0, sticky="we", columnspan=3, pady=10, padx=10)
        
        self.message = Label(frameForm, text='')
        self.message.grid(row=4, column=0, sticky="we", columnspan=3, padx=10)
        fgButton = "white"
        fontButton = ('Arial', '15', 'bold')

        # Button(self.window, text="Delete Product", bg="red", fg=fgButton, font=fontButton).grid(row=3, column=0, sticky="we")

        # Button(self.window, text="Update Product", bg="blue", fg=fgButton, font=fontButton).grid(row=3, column=1, sticky="we")
        
        frameButtons=Frame(self.window)
        # frameButtons['bg'] = 'green'
        frameButtons.grid(row=2, column=0, sticky="we s")
        frameButtons.columnconfigure((0,1), weight=1)
        style.configure("B.TButton", foreground="blue",  font=fontButton)
        style.configure("R.TButton", foreground="red", font=fontButton)
        ttk.Button(frameButtons, text="Update Product", style="B.TButton", command=self.update_product).grid(row=0, column=0, sticky="we")
        ttk.Button(frameButtons, text="Delete Product", style="R.TButton", command=self.delete_product).grid(row=0, column=1, sticky="we")
        
        # Se crea la tabla
        fontHeading = ('Arial', '10', 'bold')
        
        fontTree = ('Arial', '10', 'italic')
        style.configure('F.Treeview', font=fontTree)
        style.configure('F.Treeview.Heading', foreground='blue', font=fontHeading)
        
        self.threeViews = ttk.Treeview(self.window, height=15, columns=('Name', 'Price', 'Quantity'), style='F.Treeview')
        #Establecemos el tamaño de las columnas y centramos la tabla
        self.threeViews.column('#0', width=80, anchor=CENTER)
        self.threeViews.column('Name', width=80, anchor=CENTER)
        self.threeViews.column('Price', width=80, anchor=CENTER)
        self.threeViews.column('Quantity', width=80, anchor=CENTER)


        #Se establece el encabezado de la tabla
        self.threeViews.heading('#0', text='Id', anchor=CENTER)
        self.threeViews.heading('Name', text='Name', anchor=CENTER)
        self.threeViews.heading('Price', text='Price', anchor=CENTER)
        self.threeViews.heading('Quantity', text='Quantity', anchor=CENTER)
        
        self.get_products()


    def get_products(self):
        products = self.Database.selectAllData()
        #clean table
        self.threeViews.delete(*self.threeViews.get_children())
        for product in products:
            self.threeViews.insert('', END, text=str(product[0]), values=(product[1], product[2], product[3]))

        self.threeViews.grid(row=1, column=0, sticky="n", pady=10, padx=10)
        
    def add_product(self):
        #check if the fields are empty and if the price is a number
        if(self.entryName.get() == "" or self.entryPrice.get() == "" or self.entryQuantity.get() == ""):
            self.message['text'] = "Please fill all the fields"
            self.message['fg'] = "red"
            return
        if self.entryQuantity.get().isdigit() == False or self.isFloat(self.entryPrice.get()) == False:
            self.message['text'] = "Incorrectly filled fields"
            self.message['fg'] = "orange"
            return

        self.Database.addProduct(self.entryName.get(), self.entryPrice.get(), self.entryQuantity.get())
        print(self.entryName.get().isdigit(), self.entryPrice.get().isdigit(), self.isFloat(self.entryQuantity.get()))
        self.entryName.delete(0, END)
        self.entryPrice.delete(0, END)
        self.entryQuantity.delete(0, END)
        self.message['text'] = "Product added"
        self.message['fg'] = "green"
        self.get_products()
        # self.Database.addProduct("www", 3.3, 10)
        pass
    def delete_product(self):
        pass
    def update_product(self):
        pass

    def isFloat(self, value):
        try:
            float(value)
            return True
        except ValueError:
            return False

    def close_window(self):
        self.Database.closeConnection()
        self.window.destroy()
        print('Cerrando')
