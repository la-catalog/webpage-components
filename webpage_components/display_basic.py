import streamlit as st


def display_basic(field: str, value: str):
    st.caption(body=field)
    st.code(body=value)
