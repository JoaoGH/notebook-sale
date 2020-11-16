import csv
##import tkinter
from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk

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

        master.geometry('900x800')
        self.fonte = ("Verdana", "8")   
        
        self.containerGeral = Frame(master)
        self.containerGeral.pack(fill=BOTH, expand=YES)
        
        self.containerSelectFile = Frame(self.containerGeral)
        #self.containerSelectFile["pady"] = 10
        self.containerSelectFile.pack()
        
        self.containerMenu = Frame(self.containerGeral)
        #self.containerMenu["padx"] = 20
        #self.containerMenu["pady"] = 5
        self.containerMenu.pack(side=LEFT, anchor='nw', fill=Y, expand=YES)
        
        self.containerBotoes = Frame(self.containerMenu)
        #self.containerBotoes["padx"] = 20
        #self.containerBotoes["pady"] = 5
        self.containerBotoes.pack(fill=X, anchor='nw')
        #self.containerFiltros = Frame(self.containerMenu)
        #self.containerFiltros.pack()
        #self.containerFiltros = Frame(self.containerMenu)
        #self.containerFiltros.pack()
        #self.containerFiltros = Frame(self.containerMenu)
        #self.containerFiltros.pack()
        
        self.containerTable = Frame(self.containerGeral)
        self.containerTable.pack()
        self.container6 = Frame(master)
        self.container6["padx"] = 20
        self.container6["pady"] = 5
        self.container6.pack()
        self.container7 = Frame(master)
        self.container7["padx"] = 20
        self.container7["pady"] = 5
        self.container7.pack()
        self.container8 = Frame(master)
        self.container8["padx"] = 20
        self.container8["pady"] = 10
        self.container8.pack()
        self.container9 = Frame(master)
        self.container9["pady"] = 15
        self.container9.pack()
            
        self.sair = Button(self.container9)
        self.sair["text"] = "Sair"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 5
        self.sair["command"] = self.container9.quit
        self.sair.pack()
        
        self.titulo = Label(self.containerSelectFile, text="Selecione o arquivo")
        self.titulo["font"] = ("Calibri", "9", "bold")
        self.titulo.pack()
        self.btnBuscar = Button(self.containerSelectFile, text="Buscar", font=self.fonte, width=10)
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
    
    def enableLaptoNameFilter(self):
        self.clearFiltersContainer()
        self.laptopNameLabel = Label(self.containerFiltros, text="Laptop Name: ", font=self.fonte)
        self.laptopNameLabel.pack(side=LEFT)
        self.laptopNameEntry = Entry(self.containerFiltros)
        self.laptopNameEntry["width"] = 30
        self.laptopNameEntry["font"] = self.fonte
        self.laptopNameEntry.pack(side=LEFT)

    def enableDiskSpaceFilter(self):
        self.clearFiltersContainer()
        self.diskSpaceLabel = Label(self.containerFiltros, text="Disk Space: ", font=self.fonte)
        self.diskSpaceLabel.pack(side=LEFT)
        self.diskSpaceEntry = Entry(self.containerFiltros)
        self.diskSpaceEntry["width"] = 30
        self.diskSpaceEntry["font"] = self.fonte
        self.diskSpaceEntry.pack(side=LEFT)

    def enableDateBrandFilter(self):
        self.clearFiltersContainer()
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

    def enableAplicarDesconto(self):
        self.clearFiltersContainer()
        print('ed')
    def enableContagemRating(self):
        self.clearFiltersContainer()
        print('ed')

    def loadData(self, filePath):
        arquivo = open(filePath)
        reader = csv.reader(arquivo)
        for line in list(reader)[1::]:
            rec = Record(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
            self.records.append(rec)
        arquivo.close()

    def findByLaptopName(self, laptopName):
        for record in self.records:
            if (record.filtered):
                if (laptopName.upper() not in record.laptopName.upper()):
                    record.filtered = False

    def findByDiskSpace(self, diskSpace):
        for record in self.records:
            if (record.filtered):
                if (diskSpace.upper() not in record.diskSpace.upper()):
                    record.filtered = False

    def findByDateYmdAndBrand(self, dateYmd, brand):
        for record in self.records:
            if (record.filtered):
                if (record.dateYmd != dateYmd or brand.upper() not in record.brand.upper()):
                    record.filtered = False

    def totalFiltered(self):
        total = 0
        for record in self.records:
            if (record.filtered):
                total += 1
        return total
    
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
        print('Total de 0.0 - 0.9: ' + str(rating[0]))
        print('Total de 1.0 - 1.9: ' + str(rating[1]))
        print('Total de 2.0 - 2.9: ' + str(rating[2]))
        print('Total de 3.0 - 3.9: ' + str(rating[3]))
        print('Total de 4.0 - 4.9: ' + str(rating[4]))
        print('Total de 5.0: ' + str(rating[5]))

    def applyDiscount(self, valorInicial, valorFinal, desconto):
        for record in self.records:
            if (record.filtered):
                if (record.listPrice >= valorInicial and record.listPrice <= valorFinal):
                    record.discountPrice = record.listPrice - (record.listPrice * (desconto/100))
                else:
                    record.filtered = False

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


root = Tk()
Application(root)
root.mainloop()
##root = tkinter.Tk()
##janela = tkinter.Tk()
##janela.title("Pynder")
##janela.geometry("400x700")
##janela.mainloop()

#sistema = Sistema('notebooks_sale.csv')
#sistema.loadData()
#print(sistema.totalFiltered())
#sistema.findByLaptopName('VoStRo')
#sistema.showAllFields()
#print(sistema.totalFiltered())
#sistema.clearFilters()
#print(sistema.totalFiltered())
#sistema.applyDiscount(1000, 5000, 10)
#sistema.showAllFields()
#sistema.saveNewFile('notebook_1.csv')
#sistema.ratingCount()

