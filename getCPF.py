import pandas as pd
from dotenv import load_dotenv 
import os
load_dotenv()


filename = os.getenv("FILENAME")
def get_cpf():
    xls = pd.read_excel(f"./sheet/{filename}.xlsx", dtype={'CPF': str})
    xls = xls[["CPF"]]
    return list(xls['CPF'])

