from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class FidelidadeVeiculos:
    def __init__(self):
        # TODO: criar ficheiro com caminho do driver
        self.driver = webdriver.Chrome('C:/Users/paulo/Downloads/chromedriver_win32/chromedriver.exe')
        # TODO: vai buscar o link a BD
        self.driver.get('https://www.adn.imperiobonanca.pt/Mediacao_Common/LoginPage_SGUP.aspx')
        timeout = 2
        try:
            element_present = EC.presence_of_element_located((By.ID, 'loginIfrm'))
            WebDriverWait(self.driver, timeout).until(element_present)
            self.login()
        except TimeoutException:
            print
            "Timed out waiting for page to load"

        """
        timeout = 2
        try:
            element_present = EC.presence_of_element_located((By.LINK_TEXT, 'AU-TO-IB MultiPlanos'))
            WebDriverWait(self.driver, timeout).until(element_present)

            self.driver.find_element_by_link_text('AU-TO-IB MultiPlanos').click()
            self.iniciar()
        except TimeoutException:
            print
            "Timed out waiting for page to load"
        """

    def login(self):
        # dados de login TODO: ir buscar a base dados os valores
        username = 'XMD2168'
        password = 'fpgf2015'
        self.driver.switch_to.frame(self.driver.find_element_by_id('loginIfrm'))
        self.driver.find_element_by_id('fUserName').send_keys(username)
        self.driver.find_element_by_id('fPassword').send_keys(password)
        self.driver.find_element_by_id('Button1').click()
        # TODO: apanhar erro de login

        self.driver.switch_to.default_content()
        self.driver.get('https://www.adn.imperiobonanca.pt/Simulador_AUTMP/Simulador.aspx')
        self.iniciar()


    def iniciar(self):
        # clicar em empresa ou particular TODO: obter tipo da BD
        tipo = "particular"

        if tipo == "particular":
            self.driver.find_element_by_id('CAN_Common_Layout_wt18_block_wtbody_SimuladorAUTMP_ComUI_wtMxClientType_block_P').click()

        if tipo == "empresa":
            self.driver.find_element_by_id('CAN_Common_Layout_wt18_block_wtbody_SimuladorAUTMP_ComUI_wtMxClientType_block_C').click()

        self.quantosVeiculos()

    def quantosVeiculos(self):
        # limite é de 10 TODO numVeiculos BD
        numVeiculos = 7
        timeout = 2
        try:
            element_present = EC.presence_of_element_located((By.ID, 'CAN_Common_Layout_wt19_block_wtbody_wtContent'))
            WebDriverWait(self.driver, timeout).until(element_present)

            if numVeiculos < 6:
                self.driver.find_element_by_id('CAN_Common_Layout_wt19_block_wtbody_SimuladorAUTMP_ComUI_wtmxCtrVeicCount_block_' + str(numVeiculos)).click()
            else:
                for x in range(5, numVeiculos):
                    self.driver.find_element_by_class_name('fa-caret-up').click()

                self.driver.find_element_by_id('CAN_Common_Layout_wt19_block_wtbody_wtbtnContinueVehicleCount')

                self.veiculosNaApolice()

        except TimeoutException:
            print
            "Timed out waiting for page to load"

    def veiculosNaApolice(self):
        print("sopas")
