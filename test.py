from tkinter import *
import json
import threading
import sys
from eventos import Eventos
from seguradoras import Seguradoras
from fidelidadeVeiculos import FidelidadeVeiculos


class SimuladorGui:
    seguradoras = None
    t = None

    def __init__(self, master):
        # baseado em https://github.com/slauzinho/caixa.py/blob/master/caixa.py
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
        self.close_button = Button(groupLeft, text="Fechar", width=self.btnSize, command=self.fechar)
        self.close_button.pack()

        # caixa de texto com scroll
        self.caixaTexto(master)

        # procurar list de seguradoras
        self.seguradoras = Seguradoras().procurarSeguradoras()

    def iniciar(self):
        # Acessodb.get_database_version(self)
        self.procurarEventos()
        # loop para voltar a procurar eventos de 10 em 10 segundos
        global t
        t = threading.Timer(10, self.iniciar, ())
        t.name = "procura eventos"
        t.start()

    def fechar(self):
        for t in threading.enumerate():
            if t.name == "procura eventos":
                t.cancel()
        # fechar aplicação
        sys.exit(0)

    def procurarEventos(self):
        # verificar eventos
        eventoDados = Eventos()

        if eventoDados:
            # verificar que bots tem de abrir
            # "seguradoras":{"1":"true"}
            json_decoded = json.loads(json.dumps(eventoDados.data))

            for id in json_decoded['seguradoras']:
                # if json_decoded['seguradoras'][id]:
                # procurar dados da seguradora
                for seguradora in self.seguradoras:
                    if int(id) == seguradora[0][0]:
                        # encaminhar para a respectiva seguradora
                        if seguradora[0][2] == "Fidelidade Mundial":
                            FidelidadeVeiculos(json_decoded, seguradora)
                            return True

                        if seguradora[0][2] == "Tranquilidade":
                            # Tranquilidade(eventoDados)
                            return True
        else:
            print("não existe eventos activos")

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
