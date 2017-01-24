from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import json


class FidelidadeVeiculos:
    def __init__(self, eventoDados, seguradora):
        #Dados
        self.botDados = eventoDados
        self.seguradoraDados = seguradora
        # timeout para dar uma pausa entre os loads
        self.timeout = 5
        # TODO: criar ficheiro com caminho do driver
        self.driver = webdriver.Chrome('C:/Users/paulo/Downloads/chromedriver_win32/chromedriver.exe')
        # link da pagina da seguradora
        self.driver.get(self.seguradoraDados[0][5])
        try:
            element_present = EC.presence_of_element_located((By.ID, 'loginIfrm'))
            WebDriverWait(self.driver, self.timeout).until(element_present)
            self.login()
        except TimeoutException:
            print("Timed out waiting for page to load")

    def login(self):
        # dados de login
        username = self.seguradoraDados[0][3]
        password = self.seguradoraDados[0][4]
        self.driver.switch_to.frame(self.driver.find_element_by_id('loginIfrm'))
        self.driver.find_element_by_id('fUserName').send_keys(username)
        self.driver.find_element_by_id('fPassword').send_keys(password)
        self.driver.find_element_by_id('Button1').click()
        # TODO: apanhar erro de login

        self.driver.switch_to.default_content()
        self.driver.get('https://www.adn.imperiobonanca.pt/Simulador_AUTMP/Simulador.aspx')
        self.iniciar()

    def iniciar(self):
        # clicar em empresa ou particular
        tipo = self.botDados["tipoCliente"]
        if tipo == "I":
            self.driver.find_element_by_id(
                'CAN_Common_Layout_wt18_block_wtbody_SimuladorAUTMP_ComUI_wtMxClientType_block_P').click()

        if tipo == "C":
            self.driver.find_element_by_id(
                'CAN_Common_Layout_wt18_block_wtbody_SimuladorAUTMP_ComUI_wtMxClientType_block_C').click()

        self.quantosVeiculos()

    def quantosVeiculos(self):
        # limite é de 10
        numVeiculos = int(self.botDados["numVeiculos"])
        try:
            element_present = EC.text_to_be_present_in_element((By.ID, 'CAN_Common_Layout_wt19_block_wtballoon_wtct1'),
                                                               'Quantos veículos quer simular?')
            WebDriverWait(self.driver, self.timeout).until(element_present)

            if numVeiculos < 6:
                self.driver.find_element_by_id(
                    'CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrVeicCount_block_' + str(
                        numVeiculos)).click()
            else:
                for x in range(5, numVeiculos):
                    self.driver.find_element_by_class_name('fa-caret-up').click()

                self.driver.find_element_by_id('CAN_Common_Layout_wt19_block_wtbody_wtbtnContinueVehicleCount').click()

            self.veiculosNaApolice()

        except TimeoutException:
            print
            "Timed out waiting for page to load"
            self.quantosVeiculos()

    def veiculosNaApolice(self):
        numVeiculosApolice = int(self.botDados["numVeiculosApolice"])
        try:
            element_present = EC.text_to_be_present_in_element((By.ID, 'CAN_Common_Layout_wt19_block_wtballoon_wtct1'),
                                                               'Nº de veículos já seguros na apólice?')
            WebDriverWait(self.driver, self.timeout).until(element_present)
            if numVeiculosApolice > 3:
                self.driver.find_element_by_id(
                    'CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrNVeic_block_4').click()
            else:
                self.driver.find_element_by_id(
                    'CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrNVeic_block_' + str(
                        numVeiculosApolice)).click()
            self.usoProfissional()
        except TimeoutException:
            print
            "Timed out waiting for page to load"
            self.veiculosNaApolice()

    def usoProfissional(self):
        usoProfissional = self.botDados["tipoUso"]
        try:
            element_present = EC.text_to_be_present_in_element((By.ID, 'CAN_Common_Layout_wt19_block_wtballoon_wtct1'),
                                                               'O(s) veículo(s) é(são) para uso profissional?')
            WebDriverWait(self.driver, self.timeout).until(element_present)
            if usoProfissional == "S":
                self.driver.find_element_by_id(
                    'CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrProfUse_block_S').click()
                # se for som vai para a classe do tomador de seguro
                self.classeTomadorSeguro()
            else:
                self.driver.find_element_by_id(
                    'CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrProfUse_block_N').click()
                # se for nao vai para a data de inicio de seguro
                self.dataInicioSeguro()
        except TimeoutException:
            print("Timed out waiting for page to load")
            self.usoProfissional()

    def classeTomadorSeguro(self):
        # value sao Publico em geral (03) ou entenidade isaenta imposto selo (01)
        tomadorSeguro = self.botDados["tomadorSeguro"]
        try:
            element_present = EC.text_to_be_present_in_element((By.ID, 'CAN_Common_Layout_wt19_block_wtballoon_wtct1'),
                                                               'Classe de Tomador de Seguro')
            WebDriverWait(self.driver, self.timeout).until(element_present)
            if self.usoProfissional == "01":
                self.driver.find_element_by_id(
                    'CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrlPolicyHolder_block_01').click()
            else:
                self.driver.find_element_by_id(
                    'CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrlPolicyHolder_block_03').click()
            self.dataIniciSeguro()
        except TimeoutException:
            print("Timed out waiting for page to load")
            self.classeTomadorSeguro()

    def dataInicioSeguro(self):

        self.dataInicioSeguro()

    def __del__(self):
        del self