import pandas as pd
import numpy as np

df=pd.read_csv(r'https://raw.githubusercontent.com/maniram3112/stock-vs-crypto-risk-return-analysis/refs/heads/master/data/Raw_Data/raw_crypto.csv')
df.drop_duplicates(inplace=True,ignore_index=True)
df.to_csv('output.csv', index=False)