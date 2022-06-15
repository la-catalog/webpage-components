import pandas as pd
import streamlit as st


def display_segments(segments: list[str]) -> None:
    if segments:
        dataframe = pd.DataFrame(data=segments, columns=["segments"])
        st.table(data=dataframe)
