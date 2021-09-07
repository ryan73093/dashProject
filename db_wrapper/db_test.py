import pandas as pd
from db_wrapper.db_wrapper import Stock

dfA = pd.read_csv(
    "https://storage.googleapis.com/learn_pd_like_tidyverse/gapminder.csv")

dfB = pd.DataFrame({
    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas", "Apples",
              "Oranges", "Bananas"],
    "Amount": [4, 1, 2, 2, 4, 5, 4, 2, 3, 4, 3, 3],
    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal", 'YF', 'YF', 'YF', 'ZF', 'ZF', 'ZF']
})

stock_ID = ['2330.TW', '2324.TW', '0050.TW', '4938.TW']
data_sheet = Stock(stock_ID)
dfC = data_sheet.prices().reset_index()
