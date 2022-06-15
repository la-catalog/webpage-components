import streamlit as st


def display_images(images: list[str]) -> None:
    if not images:
        return

    index = st.number_input(
        label="Images",
        min_value=0,
        max_value=len(images) - 1,
        step=1,
    )

    st.image(
        image=images[int(index)],
        width=250,
    )
