from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoPausaComputador
import time
from dotenv import load_dotenv 
import os
load_dotenv()


USERNAME = os.getenv("USERNAME")
PASSWORD = os.getenv("PASSWORD")
INITIALDATE = os.getenv("INITIALDATE")
FINAL_DATE = os.getenv("FINALDATE")
def get_balance(cpf):
    chrome = webdriver.Chrome()
    chrome.get("https://sbe.curitiba.pr.gov.br/sbe-web/login/login.html")
    chrome.find_element(By.NAME, "nomeUsuario").send_keys(USERNAME)
    chrome.find_element(By.NAME, "senha").send_keys(PASSWORD,Keys.ENTER) 
    chrome.find_element(By.XPATH, '//*[@id="menu_19"]/div/p[1]/a').click()  
    chrome.find_element(By.XPATH, '//*[@id="formPagamento"]/center/table/tbody/tr[4]/td[1]/input').click()
    chrome.find_element(By.NAME, "liTermo").click()
    chrome.find_element(By.NAME, "continuar").click()
    chrome.find_element(By.NAME, "documentoNacional").send_keys(cpf,Keys.ENTER)
    try:
        get_value = chrome.find_element(By.NAME, "usuario").get_attribute('value')
    except Exception as err:
        return 0
    chrome.find_element(By.XPATH, '//*[@id="tabelaConteudo"]/tbody/tr[10]/td/a/img').click()
    chrome.find_element(By.XPATH, '//*[@id="menu_19"]/div/p[3]/a').click()
    chrome.find_element(By.XPATH, '//*[@id="formConsultarInformacaoUsurio"]/table/tbody/tr[4]/td/input').click()
    change_value = chrome.find_element(By.ID,"idUsuario")
    chrome.execute_script(f"arguments[0].value='{get_value}';", change_value)

    def handling_balance(attempts = 0):
        if attempts == 3:
            chrome.quit()  
            return 0
            
        get_periodo_inicial = INITIALDATE
        get_periodo_final = FINAL_DATE
        periodo_inicio = chrome.find_element(By.ID,"periodoInicio")
        periodo_final = chrome.find_element(By.ID,"periodoFim")
        chrome.execute_script(f"arguments[0].value='{get_periodo_inicial}';", periodo_inicio)
        chrome.execute_script(f"arguments[0].value='{get_periodo_final}';", periodo_final)
        chrome.find_element(By.XPATH, '//*[@id="buttonPesquisarContaCorrente"]').click()
        tempoPausaComputador.sleep(10)
        time.sleep(5)    
        try:    
            filter_table = chrome.find_elements(By.XPATH, '//*[@id="divContaCorrente"]/table/tbody/tr')
            lines = len(filter_table) - 1
            print(lines)

            if  lines == -1:
                return handling_balance(attempts + 1) 
            if lines == 0:
                chrome.quit()

                return 0
            balance = filter_table[lines].find_elements(By.TAG_NAME,'td')[7].text
            index = 1            
            if balance == "--":
                while balance == "--":
                    index += 1
                    lines = len(filter_table) - index
                    if lines == 0:
                        chrome.quit()
                        return 0
                    balance = filter_table[lines].find_elements(By.TAG_NAME,'td')[7].text
                chrome.quit()
                return balance
            chrome.quit()
            return balance
            
        except Exception as err: 
            print(err)

            return handling_balance()

    return handling_balance()


