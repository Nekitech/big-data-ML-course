import pandas as pd

"""

. Использовать индексы в обеих частях слияния для двух заданных
DataFrame:
    data1 = pd.DataFrame([[1, 4, 6], [2, 7, 1]], index = ["a","c"],
    columns = ["RMA", "JSV", "KNL"]).astype("Int64"),
    data2 = pd.DataFrame(
        [[3, 5, 6], [2, 3, 1], [1, 8, 8]],
        index = ["b", "a", "c"],
        columns = ["MAC", "OTB", "DAW"]
        ).astype("Int64").

Выполнить слияние с использованием метода - join.
"""

data1 = pd.DataFrame(
    [[1, 4, 6], [2, 7, 1]],
    index=["a", "c"],
    columns=["RMA", "JSV", "KNL"]).astype("Int64")

data2 = pd.DataFrame(
    [[3, 5, 6], [2, 3, 1], [1, 8, 8]],
    index=["b", "a", "c"],
    columns=["MAC", "OTB", "DAW"]
).astype("Int64")

print(data1.join(data2, how="outer"))
