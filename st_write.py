# Displaying data on the screen:
# 1. st.write()
# 2. Magic 🙂

import streamlit as st
import pandas as pd

st.title('Prueba en Streamlit por Mario Torres :100:')

st.write('Streamlit!')

l1 = [1, 2, 3]
st.write(l1)

l2 = list('abc')
d1 = dict(zip(l1, l2))
st.write(d1)

# using magic
'Mostrando usando magica :sonrisa'

df = pd.DataFrame({
    '1_columna': [1, 2, 3, 4],
    '2_columna': [10, 20, 30, 40]
})

df # st.write(df)

# Run it: streamlit run .\file.py