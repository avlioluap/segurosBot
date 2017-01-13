from tkinter import *
import acessodb as db
from fidelidadeVeiculos import FidelidadeVeiculos

class SimuladorGui:
    def __init__(self, master):
        #baseado em https://github.com/slauzinho/caixa.py/blob/master/caixa.py
        self.master = master
        master.title("Simulador GUI")
        master.minsize(width=800, height=400)

        # agrupar butoes do lado direito
        groupLeft = LabelFrame(master, text="Menu", padx=5, pady=5)
        groupLeft.pack(padx=10, pady=10, side=LEFT, fill=BOTH)

        # default size dos butoes
        self.btnSize = 20

        # inicar btn
        self.init_button = Button(groupLeft, text="Iniciar", width=self.btnSize, command=self.iniciar)
        self.init_button.pack()

        # fechar btn
        self.close_button = Button(groupLeft, text="Fechar", width=self.btnSize, command=master.quit)
        self.close_button.pack()

        # caixa de texto com scroll
        self.caixaTexto(master)

    def iniciar(self):
        db.get_database_version()

        FidelidadeVeiculos()

    def caixaTexto(self, master):
        # add a frame and put a text area into it
        textPad = Frame(master)
        self.text = Text(textPad, height=50, width=90)

        # add a vertical scroll bar to the text area
        scroll = Scrollbar(textPad)
        self.text.configure(yscrollcommand=scroll.set)

        # pack everything
        self.text.pack(side=LEFT, fill=BOTH, expand=YES)
        scroll.pack(side=RIGHT, fill=Y)
        textPad.pack(side=TOP)


root = Tk()
my_gui = SimuladorGui(root)
root.mainloop()
