import streamlit as st


def display_rating(
    min_value: float | None,
    max_value: float | None,
    current_value: float | None,
) -> None:
    if None in (min_value, max_value, current_value):
        return

    st.slider(
        label="rating",
        min_value=min_value,
        max_value=max_value,
        value=current_value,
        disabled=True,
    )
