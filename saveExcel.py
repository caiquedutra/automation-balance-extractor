import pandas as pd
from dotenv import load_dotenv 
import os
load_dotenv()

filename = os.getenv("FILENAME")
def save_balance(balances):
    xls = pd.read_excel(f"./sheet/{filename}.xlsx", dtype={'CPF': str})
    xls = xls.assign(saldo_dinamico=balances)
    xls.to_excel("./sheet/automation.xlsx" )