import streamlit as st


def search_info_bar(results_quantity: int, time_spent: int) -> str:
    hits_col, time_spent_col, view_col = st.columns(3)

    with view_col:
        view_mode = st.radio("view mode", ["default", "json", "code"], horizontal=True)

    with hits_col:
        st.text(f"🔍 results: {results_quantity}")

    with time_spent_col:
        st.text(f"⏱️ time spent: {time_spent}")

    return view_mode
