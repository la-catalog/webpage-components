import pandas as pd
import streamlit as st
from text_utility import stringfy


def display_measurements(
    main_length: float | None,
    main_width: float | None,
    main_height: float | None,
    main_unit: str | None,
    package_length: float | None,
    package_width: float | None,
    package_height: float | None,
    package_unit: str | None,
) -> None:
    dataframe = pd.DataFrame(
        data=[
            [
                stringfy(main_length),
                stringfy(main_width),
                stringfy(main_height),
                stringfy(main_unit),
            ],
            [
                stringfy(package_length),
                stringfy(package_width),
                stringfy(package_height),
                stringfy(package_unit),
            ],
        ],
        index=["🧸", "📦"],
        columns=["🇨", "🇱", "🇦", "📐"],
    )

    st.table(data=dataframe)
