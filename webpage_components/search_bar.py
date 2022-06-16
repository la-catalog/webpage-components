from collections.abc import Iterator

import streamlit as st


def search_bar(marketplaces: list, search_label: str = "") -> Iterator[str]:
    search_col, marketplace_col = st.columns([7, 1])

    with search_col:
        yield st.text_input(label=search_label)

    with marketplace_col:
        yield st.selectbox(label="Marketplace", options=marketplaces)
