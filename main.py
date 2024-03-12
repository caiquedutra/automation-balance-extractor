from selenium import webdriver
from  selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import pyautogui as tempoPausaComputador
from startAutomation import get_balance
from getCPF import get_cpf

from saveExcel import save_balance

balances = []
cpfs = get_cpf()
for  cpf in  cpfs:
    print(f"CPF processado: {cpf}")
    balance = get_balance(cpf)
    balances.append(balance)
    print(f"Saldo obtido: {balance}")
save_balance(balances)
print("Todos os cpfs foram processados com sucesso!")