import pandas as pd
import numpy as np

"""
 В заданном DataFrame: 
 df = pd.DataFrame({"k1" : ["a", "b" , None, "b" "a", "c"], "k2" : pd.Series([1, 1, 2, 2, None, 2], dtype = "Int64"),
  "data1" : np.random.standard_normal(6), 
 "data2": np.random.standard_normal(6)}) 
 вычислить среднее по столбцу data1 и data2 с использованием метки групп в столбце k1.

"""

df = pd.DataFrame(
    {
        "k1": ["a", "b", None, "b", "a", "c"],
        "k2": pd.Series([1, 1, 2, 2, None, 2], dtype="Int64"),
        "data1": np.random.standard_normal(6),
        "data2": np.random.standard_normal(6)
    }
)
print(df)
print(df.groupby("k1")[["data1", "data2"]].mean())
