import pandas as pd
from dotenv import load_dotenv 
load_dotenv()
import os

filename = os.environ["FILENAME"]
def get_cpf():
    xls = pd.read_excel(f"./sheet/{filename}.xlsx", dtype={'CPF': str})
    xls = xls[["CPF"]]
    return list(xls['CPF'])

