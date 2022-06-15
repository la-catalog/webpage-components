import pandas as pd
import streamlit as st
from text_utility import stringfy


def display_prices(prices: list[tuple(float, str)]) -> None:
    values = [stringfy(amount) for amount, _ in prices]
    currencies = [currency for _, currency in prices]
    dataframe = pd.DataFrame(
        data=values,
        columns=["💲"],
        index=currencies,
    )

    st.table(data=dataframe)
