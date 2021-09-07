import os
from dotenv import load_dotenv
import pandas as pd
import ffn

class Stock:
    def __init__(self, lst_stock):
        self.lst_stock = lst_stock

    def prices(self):
        df = pd.DataFrame()
        for i in self.lst_stock:
            df_ = ffn.get(i).reset_index()
            df_.columns = ['Date', 'Price']
            df_['Code'] = i
            df = pd.concat([df, df_], axis=0)
        return df





