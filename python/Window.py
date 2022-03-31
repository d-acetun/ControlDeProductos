# import tkinter as tk
from tkinter import ttk
from tkinter import *

class Window:
    def __init__(self, window):
        self.window = window
        self.window.title('Products Aplication')
        self.window['bg'] = 'skyblue1'
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
        self.entryPrice = Entry(frameForm, width=30, font=font).grid(row=1, column=1, padx=10)
        self.entryQuantity = Entry(frameForm, width=30, font=font).grid(row=2, column=1, pady=10, padx=10)
        
        #* EW PARA EXTENDER HORIZONTALMENTE
        #* NS PARA EXTENDER VERTICALMENTE
        #* NSEW PARA EXTENDER EN TODAS LAS DIRECCIONES
        #* columnspan indica que se extiende en todas las columnas
        style = ttk.Style()
        style.configure("G.TButton", foreground="green", font=font)
        ttk.Button(frameForm, text="ADD", style="G.TButton", command=self.add_product).grid(row=3, column=0, sticky="we", columnspan=3, pady=10, padx=10)
        
        self.message = Label(frameForm, text='', fg='red').grid(row=4, column=0, sticky="we", columnspan=3, padx=10)
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
        for x in range(50):
            self.threeViews.insert('', END, text=str(x), values=('Product 1', '$100', '10'))

        self.threeViews.grid(row=1, column=0, sticky="n", pady=10, padx=10)


    def add_product(self):
        print(self.entryName.get())
        pass
    def delete_product(self):
        pass
    def update_product(self):
        pass
