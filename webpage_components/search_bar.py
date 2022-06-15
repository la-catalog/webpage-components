from collections.abc import Iterator

import streamlit as st


def search_bar(marketplaces: list) -> Iterator[str]:
    search_col, marketplace_col = st.columns([3, 1])

    with search_col:
        yield st.text_input(label="", placeholder="Write something here")

    with marketplace_col:
        yield st.selectbox(label="", options=marketplaces)
