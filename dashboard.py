import streamlit as st
import pandas as pd
import numpy as np

# Nastavení základního nadpisu
st.title("Ukázkový dashboard - Interaktivní graf")

# Generování náhodných dat pro graf
data = pd.DataFrame({
    'x': np.arange(1, 101),
    'y': np.random.randn(100).cumsum()
})

# Zobrazení grafu s posuvníkem
st.line_chart(data)

# Možnost zadat uživatelské vstupy
st.write("Upravte počet bodů grafu")
num_points = st.slider("Počet bodů:", min_value=10, max_value=100, value=50)
st.line_chart(data.head(num_points))