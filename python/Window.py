# import tkinter as tk
from tkinter import ttk
from tkinter import *


class Window:
    def __init__(self, window):
        self.window = window
        self.window.title('Products Aplication')
        
        # self.window.configure(background='black')
        width = 1300
        height = 820
        x = self.window.winfo_screenwidth() // 2 - width // 2
        y = 0
        posicion = str(width) + "x" + str(height) + "+" + str(x) + "+" + str(y)
        self.window.geometry(posicion)
        self.window.state('zoomed')
        Label(self.window, text="Products Aplication", font=("Arial", 20), bg="pink").pack()

        sizeButton = int(1300/3)
        positionXButton=0
        positionYButton=height-40
        fgButton = "white"
        Button(self.window, text="Add Product", font=("Arial", 15), bg="green", fg=fgButton, command=self.add_product).place(x=positionXButton, y=positionYButton, width=sizeButton)
        positionXButton+=sizeButton

        Button(self.window, text="Delete Product", font=("Arial", 15), bg="red", fg=fgButton, command=self.delete_product).place(x=positionXButton, y=positionYButton, width=sizeButton)
        positionXButton+=sizeButton

        Button(self.window, text="Update Product", font=("Arial", 15), bg="blue", fg=fgButton, command=self.update_product).place(x=positionXButton, y=positionYButton, width=sizeButton)

        #Se crea la tabla
        self.threeViews = ttk.Treeview(self.window, columns=('Name', 'Price', 'Quantity'))
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
        self.threeViews.insert('', END, text='1', values=('Product 1', '$100', '10'))
        self.threeViews.pack()
        self.threeViews.place(relx=0.5, rely=0.2, anchor=CENTER)
    def add_product(self):
        pass
    def delete_product(self):
        pass
    def update_product(self):
        pass
