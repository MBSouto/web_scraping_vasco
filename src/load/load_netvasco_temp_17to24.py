import pandas as pd
import sqlite3

# Carregando dados em um dataframe pandas

df = pd.read_json(
    '../../data/data_netvasco_temp_17to24_clean.json')

print(df)