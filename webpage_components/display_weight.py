import pandas as pd
import streamlit as st

from webpage_components.utility import stringfy


def display_weight(
    main_weight: float | None,
    main_weight_unit: str | None,
    package_weight: float | None,
    package_weight_unit: str | None,
) -> None:
    dataframe = pd.DataFrame(
        data=[
            [
                stringfy(main_weight),
                stringfy(main_weight_unit),
            ],
            [
                stringfy(package_weight),
                stringfy(package_weight_unit),
            ],
        ],
        index=["🧸", "📦"],
        columns=["🇵", "⚖️"],
    )

    st.table(data=dataframe)
