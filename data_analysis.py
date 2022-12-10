# %%
import pandas as pd
import web3

# %%
jacked_ape = pd.read_csv('data/jacked_ape.csv')
moonbirds = pd.read_csv('data/moonbirds.csv')

# %%
def clean_data(df):
    df = df.drop(['DateTime', 'TxnFee(ETH)'], axis=1)

def calc_avg_sale(df):
    mean = round2(df["value"].mean())
    median = round2(df["value"].median())
    max = round2(df["value"].max())
    min = round2(df["value"].min())
    return [mean, median, max, min]

# helper functions 
def round2(num):
    return str(round(num), 2)

# %%
if __name__=="__main__":
    calc_avg_sale(jacked_ape)

# %%
