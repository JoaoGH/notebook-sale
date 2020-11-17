import csv
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk
import tkcalendar

class Record:

    def __init__(self, dateYmd, brand, laptopName, displaySize, processorType, graphicsCard, diskSpace, discountPrice, listPrice, rating):
        self.dateYmd = dateYmd
        self.brand = brand
        self.laptopName = laptopName
        self.displaySize = float(displaySize)
        self.processorType = processorType
        self.graphicsCard = graphicsCard
        self.diskSpace = diskSpace
        self.discountPrice = float(discountPrice)
        self.listPrice = float(listPrice)
        self.rating = rating
        self.filtered = True

    def preparateRating(self):
        return float(self.rating.split('/')[0])
    
    def toString(self):
        toShow = ''
        toShow += str(self.dateYmd) + ','
        toShow += str(self.brand) + ','
        toShow += str(self.laptopName) + ','
        toShow += str(self.displaySize) + ','
        toShow += str(self.processorType) + ','
        toShow += str(self.graphicsCard) + ','
        toShow += str(self.diskSpace) + ','
        toShow += str(self.discountPrice) + ','
        toShow += str(self.listPrice) + ','
        toShow += str(self.rating)
        return toShow

class Application:
    
    def __init__(self, master=None):
        self.records = []

        master.geometry('1600x650')
        self.fonte = ("Verdana", "8")   
        
        self.containerGeral = Frame(master)
        self.containerGeral.pack(fill=Y, expand=YES)
        
        self.containerSelectFile = Frame(self.containerGeral)
        self.containerSelectFile.pack()
        
        self.containerMenu = Frame(self.containerGeral)
        self.containerMenu.pack()
        
        self.containerBotoes = Frame(self.containerMenu)
        self.containerBotoes["padx"] = 20
        self.containerBotoes["pady"] = 20
        self.containerBotoes.pack(fill=X, anchor='nw')
        self.containerFiltros = Frame(self.containerMenu)
        self.containerFiltros["pady"] = 20
        self.containerFiltros.pack()
        
        self.containerTable = Frame(self.containerGeral)
        self.containerTable.pack()
        self.tree = None
        self.filtrarButton = None

        self.containerFooter = Frame(master)
        self.containerFooter["pady"] = 15
        self.containerFooter.pack()

        self.sair = Button(self.containerFooter)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.containerFooter.quit
        self.sair.pack()
        self.total = Label(self.containerFooter)
        self.total.pack()
        
        self.titulo = Label(self.containerSelectFile, text="Selecione o arquivo")
        self.titulo.pack()
        self.btnBuscar = Button(self.containerSelectFile, text="Buscar Arquivo", font=self.fonte)
        self.btnBuscar["command"] = self.buscarArquivo
        self.btnBuscar.pack(side=RIGHT)       

    def buscarArquivo(self):
        fileWindow = Tk()
        fileWindow.withdraw()
        filePath = askopenfilename(filetypes = [("CSV Files","*.csv")])
        if (filePath):
            self.loadData(filePath)
            self.enableSoftware()

    def enableSoftware(self):
        self.containerSelectFile.destroy()        

        self.localizarLaptopName = Button(self.containerBotoes)
        self.localizarLaptopName["text"] = "Localizar por laptop_name"
        self.localizarLaptopName["font"] = ("Calibri", "10")
        self.localizarLaptopName["width"] = 25
        self.localizarLaptopName["command"] = self.enableLaptoNameFilter
        self.localizarLaptopName.pack(side=LEFT, fill='x')
        
        self.localizarDiskSpace = Button(self.containerBotoes)
        self.localizarDiskSpace["text"] = "Localizar por disk_space"
        self.localizarDiskSpace["font"] = ("Calibri", "10")
        self.localizarDiskSpace["width"] = 25
        self.localizarDiskSpace["command"] = self.enableDiskSpaceFilter
        self.localizarDiskSpace.pack(side=LEFT, fill='x')
        
        self.localizarDateBrand = Button(self.containerBotoes)
        self.localizarDateBrand["text"] = "Filtrar por date_ymd e brand"
        self.localizarDateBrand["font"] = ("Calibri", "10")
        self.localizarDateBrand["width"] = 25
        self.localizarDateBrand["command"] = self.enableDateBrandFilter
        self.localizarDateBrand.pack(side=LEFT, fill='x')
        
        self.aplicarDesconto = Button(self.containerBotoes)
        self.aplicarDesconto["text"] = "Aplicar desconto"
        self.aplicarDesconto["font"] = ("Calibri", "10")
        self.aplicarDesconto["width"] = 25
        self.aplicarDesconto["command"] = self.enableAplicarDesconto
        self.aplicarDesconto.pack(side=LEFT, fill='x')
        
        self.contagemRating = Button(self.containerBotoes)
        self.contagemRating["text"] = "Contagem por rating"
        self.contagemRating["font"] = ("Calibri", "10")
        self.contagemRating["width"] = 25
        self.contagemRating["command"] = self.enableContagemRating
        self.contagemRating.pack(side=LEFT, fill='x')

    def clearFiltersContainer(self):
        if hasattr(self, 'laptopNameLabel'):
            self.laptopNameLabel.destroy()
        if hasattr(self, 'laptopNameEntry'):
            self.laptopNameEntry.destroy()
        if hasattr(self, 'diskSpaceLabel'):
            self.diskSpaceLabel.destroy()
        if hasattr(self, 'diskSpaceEntry'):
            self.diskSpaceEntry.destroy()
        if hasattr(self, 'dateYmdLabel'):
            self.dateYmdLabel.destroy()
        if hasattr(self, 'dateYmdEntry'):
            self.dateYmdEntry.destroy()
        if hasattr(self, 'brandLabel'):
            self.brandLabel.destroy()
        if hasattr(self, 'brandEntry'):
            self.brandEntry.destroy()
        if hasattr(self, 'listPriceInicialLabel'):
            self.listPriceInicialLabel.destroy()
        if hasattr(self, 'listPriceInicialEntry'):
            self.listPriceInicialEntry.destroy()
        if hasattr(self, 'listPriceFinalLabel'):
            self.listPriceFinalLabel.destroy()
        if hasattr(self, 'listPriceFinalEntry'):
            self.listPriceFinalEntry.destroy()
        if hasattr(self, 'descontoDesejadoLabel'):
            self.descontoDesejadoLabel.destroy()
        if hasattr(self, 'descontoDesejadoEntry'):
            self.descontoDesejadoEntry.destroy()
        if hasattr(self, 'novoArquivoLabel'):
            self.novoArquivoLabel.destroy()
        if hasattr(self, 'novoArquivoEntry'):
            self.novoArquivoEntry.destroy()

    def enableLaptoNameFilter(self):
        self.clearFiltersContainer()
        self.showTable()

        self.laptopNameLabel = Label(self.containerFiltros, text="Laptop Name: ", font=self.fonte)
        self.laptopNameLabel.pack(side=LEFT)
        self.laptopNameEntry = Entry(self.containerFiltros)
        self.laptopNameEntry["width"] = 30
        self.laptopNameEntry["font"] = self.fonte
        self.laptopNameEntry.pack(side=LEFT)

        if (self.filtrarButton != None):
            self.filtrarButton.destroy()
        self.filtrarButton = Button(self.containerFiltros, text='Filtrar', font=self.fonte)
        self.filtrarButton["command"] = self.findByLaptopName
        self.filtrarButton.pack()

    def enableDiskSpaceFilter(self):
        self.clearFiltersContainer()
        self.showTable()

        self.diskSpaceLabel = Label(self.containerFiltros, text="Disk Space: ", font=self.fonte)
        self.diskSpaceLabel.pack(side=LEFT)
        self.diskSpaceEntry = Entry(self.containerFiltros)
        self.diskSpaceEntry["width"] = 30
        self.diskSpaceEntry["font"] = self.fonte
        self.diskSpaceEntry.pack(side=LEFT)
        
        if (self.filtrarButton != None):
            self.filtrarButton.destroy()
        self.filtrarButton = Button(self.containerFiltros, text='Filtrar', font=self.fonte)
        self.filtrarButton["command"] = self.findByDiskSpace
        self.filtrarButton.pack()

    def enableDateBrandFilter(self):
        self.clearFiltersContainer()
        self.showTable()
        
        self.dateYmdLabel = Label(self.containerFiltros, text="Date Ymd: ", font=self.fonte)
        self.dateYmdLabel.pack(side=LEFT)
        self.dateYmdEntry = Entry(self.containerFiltros)
        self.dateYmdEntry["width"] = 30
        self.dateYmdEntry["font"] = self.fonte
        self.dateYmdEntry.pack(side=LEFT)

        self.brandLabel = Label(self.containerFiltros, text="Brand: ", font=self.fonte)
        self.brandLabel.pack(side=LEFT)
        self.brandEntry = Entry(self.containerFiltros)
        self.brandEntry["width"] = 30
        self.brandEntry["font"] = self.fonte
        self.brandEntry.pack(side=LEFT)
        
        if (self.filtrarButton != None):
            self.filtrarButton.destroy()
        self.filtrarButton = Button(self.containerFiltros, text='Filtrar', font=self.fonte)
        self.filtrarButton["command"] = self.findByDateYmdAndBrand
        self.filtrarButton.pack()

    def enableAplicarDesconto(self):
        self.clearFiltersContainer()
        self.showTable()
        
        self.listPriceInicialLabel = Label(self.containerFiltros, text="List Price Inicial: ", font=self.fonte)
        self.listPriceInicialLabel.pack(side=LEFT)
        self.listPriceInicialEntry = Entry(self.containerFiltros,validate="key")
        self.listPriceInicialEntry["width"] = 30
        self.listPriceInicialEntry["font"] = self.fonte
        self.listPriceInicialEntry.pack(side=LEFT)

        self.listPriceFinalLabel = Label(self.containerFiltros, text="List Price Final: ", font=self.fonte)
        self.listPriceFinalLabel.pack(side=LEFT)
        self.listPriceFinalEntry = Entry(self.containerFiltros)
        self.listPriceFinalEntry["width"] = 30
        self.listPriceFinalEntry["font"] = self.fonte
        self.listPriceFinalEntry.pack(side=LEFT)

        self.descontoDesejadoLabel = Label(self.containerFiltros, text="Desconto Desejado: ", font=self.fonte)
        self.descontoDesejadoLabel.pack(side=LEFT)
        self.descontoDesejadoEntry = Entry(self.containerFiltros)
        self.descontoDesejadoEntry["width"] = 30
        self.descontoDesejadoEntry["font"] = self.fonte
        self.descontoDesejadoEntry.pack(side=LEFT)

        self.novoArquivoLabel = Label(self.containerFiltros, text="Nome do Novo Arquivo: ", font=self.fonte)
        self.novoArquivoLabel.pack(side=LEFT)
        self.novoArquivoEntry = Entry(self.containerFiltros)
        self.novoArquivoEntry["width"] = 30
        self.novoArquivoEntry["font"] = self.fonte
        self.novoArquivoEntry.pack(side=LEFT)

        if (self.filtrarButton != None):
            self.filtrarButton.destroy()
        self.filtrarButton = Button(self.containerFiltros, text='Filtrar', font=self.fonte)
        self.filtrarButton["command"] = self.applyDiscount
        self.filtrarButton.pack()
    
    def enableContagemRating(self):
        self.clearFiltersContainer()
        if (self.filtrarButton != None):
            self.filtrarButton.destroy()
        self.ratingCount()

    def loadData(self, filePath):
        self.showTable()
        arquivo = open(filePath)
        reader = csv.reader(arquivo)
        for line in list(reader)[1::]:
            rec = Record(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
            self.records.append(rec)
        arquivo.close()
        self.showRecordOnTable()

    def showTable(self):
        if (self.tree != None):
            self.tree.destroy()
        
        self.tree = ttk.Treeview(self.containerTable, columns=("Date", "Brand", "LaptopName", "Display Size", "Processor", "Graphics Card", "Disk Space", "Discount", "List Price", "Rating"), height=20, selectmode="extended")
        self.tree.heading('Date', text="Date", anchor=W)
        self.tree.heading('Brand', text="Brand", anchor=W)
        self.tree.heading('LaptopName', text="LaptopName", anchor=W)
        self.tree.heading('Display Size', text="Display Size", anchor=W)
        self.tree.heading('Processor', text="Processor", anchor=W)
        self.tree.heading('Graphics Card', text="Graphics Card", anchor=W)
        self.tree.heading('Disk Space', text="Disk Space", anchor=W)
        self.tree.heading('Discount', text="Discount", anchor=W)
        self.tree.heading('List Price', text="List Price", anchor=W)
        self.tree.heading('Rating', text="Rating", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=110)
        self.tree.column('#4', stretch=NO, minwidth=0, width=160)
        self.tree.column('#5', stretch=NO, minwidth=0, width=160)
        self.tree.column('#6', stretch=NO, minwidth=0, width=160)
        self.tree.column('#7', stretch=NO, minwidth=0, width=160)
        self.tree.column('#8', stretch=NO, minwidth=0, width=160)
        self.tree.column('#9', stretch=NO, minwidth=0, width=160)
        self.tree.pack()

    def showRecordOnTable(self):
        self.total['text'] = self.totalFiltered()
        for i in self.tree.get_children():
            self.tree.delete(i)
        for record in self.records:
            if (record.filtered):
                self.tree.insert('', END, values=(
                    record.dateYmd,
                    record.brand,
                    record.laptopName,
                    record.displaySize,
                    record.processorType,
                    record.graphicsCard,
                    record.diskSpace,
                    record.discountPrice,
                    record.listPrice,
                    record.rating
                ))

    def findByLaptopName(self):
        laptopName = self.laptopNameEntry.get()
        self.clearFilters()
        if (laptopName != ''):
            for record in self.records:
                if (record.filtered):
                    if (laptopName.upper() not in record.laptopName.upper()):
                        record.filtered = False
        self.showRecordOnTable()
        self.hideColumns('laptopFilter')

    def findByDiskSpace(self):
        diskSpace = self.diskSpaceEntry.get()
        self.clearFilters()
        if (diskSpace != ''):
            for record in self.records:
                if (record.filtered):
                    if (diskSpace.upper() not in record.diskSpace.upper()):
                        record.filtered = False
        self.createTableDiskSpace()
        self.showRecordOnTableDiskSpace()
        self.hideColumns('diskFilter')

    def createTableDiskSpace(self):
        self.tree.destroy()
        self.tree = ttk.Treeview(self.containerTable, columns=("Brand", "LaptopName", "Discount", "List Price", "Discount Amount"), height=20, selectmode="extended")
        self.tree.heading('Brand', text="Brand", anchor=W)
        self.tree.heading('LaptopName', text="LaptopName", anchor=W)
        self.tree.heading('Discount', text="Discount", anchor=W)
        self.tree.heading('List Price', text="List Price", anchor=W)
        self.tree.heading('Discount Amount', text="Discount Amount", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.column('#2', stretch=NO, minwidth=0, width=100)
        self.tree.column('#3', stretch=NO, minwidth=0, width=110)
        self.tree.column('#4', stretch=NO, minwidth=0, width=110)
        self.tree.pack()

    def showRecordOnTableDiskSpace(self):
        for record in self.records:
            if (record.filtered):
                discountAmount = record.listPrice - record.discountPrice
                self.tree.insert('', END, values=(
                    record.brand,
                    record.laptopName,
                    record.discountPrice,
                    record.listPrice,
                    discountAmount
                ))

    def findByDateYmdAndBrand(self):
        dateYmd = self.dateYmdEntry.get()
        brand = self.brandEntry.get()
        self.clearFilters()
        if (dateYmd != '' or brand != ''):
            for record in self.records:
                if (record.filtered):
                    if (record.dateYmd != dateYmd or brand.upper() not in record.brand.upper()):
                        record.filtered = False
        self.hideColumns('dateBrandFilter')
        self.records.sort(key=lambda x: x.laptopName)
        self.showRecordOnTable()

    def clearFilters(self):
        for record in self.records:
            record.filtered = True

    def ratingCount(self):
        rating = [0,0,0,0,0,0]
        for record in self.records:
            recordRating = record.preparateRating()
            if (recordRating >= 0 and recordRating <= 0.9):
                rating[0] += 1
            elif (recordRating >= 1 and recordRating <= 1.9):
                rating[1] += 1
            elif (recordRating >= 2 and recordRating <= 2.9):
                rating[2] += 1
            elif (recordRating >= 3 and recordRating <= 3.9):
                rating[3] += 1
            elif (recordRating >= 4 and recordRating <= 4.9):
                rating[4] += 1
            else:
                rating[5] += 1
        self.tree.destroy()
        self.tree = ttk.Treeview(self.containerTable, columns=("Rating", "Total"), height=20, selectmode="extended")
        self.tree.heading('Rating', text="Rating", anchor=W)
        self.tree.heading('Total', text="Total", anchor=W)
        self.tree.column('#0', stretch=NO, minwidth=0, width=0)
        self.tree.column('#1', stretch=NO, minwidth=0, width=100)
        self.tree.pack()
        self.tree.insert('', END, values=(
            '0.0 - 0.9',
            rating[0]
        ))
        self.tree.insert('', END, values=(
            '1.0 - 1.9',
            rating[1]
        ))
        self.tree.insert('', END, values=(
            '2.0 - 2.9',
            rating[2]
        ))
        self.tree.insert('', END, values=(
            '3.0 - 3.9',
            rating[3]
        ))
        self.tree.insert('', END, values=(
            '4.0 - 4.9',
            rating[4]
        ))
        self.tree.insert('', END, values=(
            '5.0',
            rating[5]
        ))

    def applyDiscount(self):
        try:
            self.clearFilters()
            valorInicial = self.listPriceInicialEntry.get()
            valorFinal = self.listPriceFinalEntry.get()
            desconto = self.descontoDesejadoEntry.get()
            novoArquivo = self.novoArquivoEntry.get()
            if (valorInicial != '' and valorFinal != '' and desconto != ''):
                valorInicial = float(valorInicial)
                valorFinal = float(valorFinal)
                desconto = float(desconto)
                novoArquivo = self.novoArquivoEntry.get()
                for record in self.records:
                    if (record.filtered):
                        if (record.listPrice >= valorInicial and record.listPrice <= valorFinal):
                            record.discountPrice = record.listPrice - (record.listPrice * (desconto/100))
                        else:
                            record.filtered = False
                self.showRecordOnTable()
                self.saveNewFile(novoArquivo)
                self.hideColumns('laptopFilter')
        except ValueError:
            print('Valor invalido')     

    def showAllFields(self):
        for record in self.records:
            if (record.filtered):
                print(record.listPrice)
                print(record.discountPrice)
                print('--------------')

    def saveNewFile(self, newFileName):
        arquivo = open(newFileName, 'w')
        arquivo.write('date_ymd,brand,laptop_name,display_size,processor_type,graphics_card,disk_space,discount_price,list_price,rating\n')
        for record in self.records:
            if (record.filtered):
                arquivo.write(record.toString())
                arquivo.write('\n')
        arquivo.close()

    def hideColumns(self, opc):
        displaycolumns = []
        if (opc == 'laptopFilter'):
            displaycolumns = ['Date','Brand','LaptopName','Display Size','Processor','Graphics Card','Disk Space','Discount','List Price','Rating']
        elif (opc == 'diskFilter'):
            displaycolumns = ['Brand','LaptopName','Discount', 'List Price', 'Discount Amount']
        elif (opc == 'dateBrandFilter'):
            displaycolumns = ['LaptopName','Display Size','Disk Space','Discount','Rating']
        self.tree["displaycolumns"] = displaycolumns

    def totalFiltered(self):
        total = 0
        for record in self.records:
            if (record.filtered):
                total += 1
        return total

root = Tk()
Application(root)
root.mainloop()
