# %%
import pandas as pd
import numpy as np
import web3

# %%
jacked_ape = pd.read_csv('data/jacked_ape.csv', low_memory=False, index_col=False)
moonbirds = pd.read_csv('data/moonbirds.csv', low_memory=False, index_col=False)

# %%
def clean_data(df):
    df = df.drop(['UnixTimestamp', 'Status', 'ContractAddress', 'Txhash', 'Blockno', 'Historical $Price/Eth', 'ErrCode', 'TxnFee(ETH)', 'Value_IN(ETH)', 'Value_OUT(ETH)'], axis=1)
    df.rename(columns={'CurrentValue @ $1272.79/Eth':'Value_USD'}, inplace = True)
    df['DateTime'] = pd.to_datetime(df['DateTime'])
    return df


def calc_avg_sale(df):
    mean = round2(df["Value_USD"].mean())
    median = round2(df["Value_USD"].median())
    max = round2(df["Value_USD"].max())
    min = round2(df["Value_USD"].min())
    cap = round2(df["Value_USD"].sum())
    return [mean, median, min, max, cap]

def aggregate_daily(df):
    df = df.groupby([df['DateTime'].dt.date]).mean(numeric_only=True)
    return df

def calc_percentage_change(df):
    df['Percent_Change'] = df['Value_USD'].pct_change()
    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.replace(-1.0, np.nan, inplace=True)
    df.dropna(subset=["Percent_Change"], how='all', inplace=True)
    df['Percent_Change'] = df['Percent_Change']
    return round2(df["Percent_Change"].max()*100)

def buyer_analysis(df):
    top_3 = jac_df['From'].value_counts().head(3)
    unique_pct = round2(df.nunique().From*100/df.count().From)
    first = round2(top_3[0]*100/df.count().From)
    second = round2(top_3[1]*100/df.count().From)
    third = round2(top_3[2]*100/df.count().From)
    return[df.count().From, unique_pct, first, second, third]

def ape_mint(df):
    minted_df = df[df["Method"] == "Mint"]
    return minted_df

def mb_mint(df):
    minted_df = df[df["Method"] == "Mint Public"]
    return minted_df

# helper functions 
def round2(num):
    return str(round(num, 3))


def generate_summary(name, avg, agg, buyer):
    print(f"""
    Report for NFT-{name}:

    Basic Statistics (unit: USD): 
        The Average Value is: {avg[0]};
        The Median Value is: {avg[1]};
        The Min Value is: {avg[2]};
        The Max Value is: {avg[3]};
        The Market Cap is: {avg[4]};
        The Max One Day Change is: {agg} %
    
    Buyer Analysis:
        Total Buyers: {buyer[0]}
        Percent of Unique Buyers: {buyer[1]}%
        Top 1 Buyer Owns: {buyer[2]}%
        Top 2 Buyer Owns: {buyer[3]}%
        Top 3 Buyer Owns: {buyer[4]}%
    """)

# %%
if __name__=="__main__":
    jac_df = clean_data(jacked_ape)
    mb_df = clean_data(moonbirds)

    jac_minted = ape_mint(jac_df)
    moonbirds_minted = mb_mint(mb_df)

    print("#"*46)
    generate_summary('Jacked Ape Club', 
                    calc_avg_sale(jac_df), 
                    calc_percentage_change(aggregate_daily(jac_df)),
                    buyer_analysis(jac_minted))

    print("#"*48)

    generate_summary('Moonbirds', 
                    calc_avg_sale(mb_df), 
                    calc_percentage_change(aggregate_daily(mb_df)),
                    buyer_analysis(moonbirds_minted))
    