import pandas as pd
import streamlit as st


def display_attributes(attributes: list[tuple[str, str]], id_: str) -> None:
    if st.checkbox(label="👁️ attributes", key=f"{id_}_attributes"):
        names = [name for name, _ in attributes]
        values = [value for _, value in attributes]
        dataframe = pd.DataFrame(data={"name": names, "value": values})

        st.table(data=dataframe)
