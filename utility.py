import pandas as pd
import numpy as np

def clean_up_data(df: pd.DataFrame, data_name: str = None) -> pd.DataFrame:
    df = df.iloc[:, 0:-2]
    # print(df)
    dname = lambda x: f"{data_name}_{x}" if data_name else x
    df.columns = ["Date", dname("Close"), dname("Open"), dname("High"), dname("Low")]
    df.index = df["Date"]
    df.index = pd.to_datetime(df.index, format="%b %d, %Y")
    df = df.loc[:, [dname("Close"), dname("Open"), dname("High"), dname("Low")]]
    for i in range(len(df.columns)):
        try:
            df.iloc[:, i] = pd.to_numeric(df.iloc[:, i])
        except:
            df.iloc[:, i] = pd.to_numeric(df.iloc[:, i].apply(lambda x: x.replace(',','')))
    return df.copy(deep=True)

def rma(x, n, y0):
    a = (n-1) / n
    ak = a**np.arange(len(x)-1, -1, -1)
    return np.r_[np.full(n, np.nan), y0, np.cumsum(ak * x) / ak / n + y0 * a**np.arange(1, len(x)+1)]


# if __name__ ==  "__main__":
#     vix = pd.read_csv("vix.csv")
#     vix = clean_up_data(vix)
#     print(vix)