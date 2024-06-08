# STREAMLIT WIDGETS

import streamlit as st
import pandas as pd

# TEXT INPUT
name = st.text_input('Tu Nombre: ')
if name:
    st.write(f'Hola {name}!')

# NUMBER INPUT
x = st.number_input('Ingresa un número', min_value=1, max_value=99, step=1)
st.write(f'El número es {x}')

st.divider()  # draw a horizontal line

# BUTTON
clicked = st.button('Click me!')
if clicked:
    st.write(':ghost:' * 3)

st.divider()

# CHECKBOX
agree = st.checkbox('De acuerdo')
if agree:
    'Grandioso, estas de acuerdo!'

checked = st.checkbox('Continua', value=True)
if checked:
    ':+1:' * 5

df = pd.DataFrame({'Nombre': ['Anne', 'Mario', 'Douglas'],
                   'Edad': [30, 25, 40]
                   })
if st.checkbox('Muestra'):
    st.write(df)

st.divider()

# RADIO BUTTONS
pets = ['gato', 'perro', 'pez', 'tortuga']
pet = st.radio('mascota favorita', pets, index=2, key='your_pet')
st.write(f'Tu mascota favorita: {pet}')
st.write(f'Tu mascota favorita: {st.session_state.your_pet * 1}')

st.divider()

# SELECT BOXES
cities = ['Londres', 'Berlin', 'Paris', 'Madrid']
city = st.selectbox('tu ciudad', cities, index=1)
st.write(f'Vives en {city}')

st.divider()

# SLIDER
x = st.slider('x', value=15, min_value=12, max_value=78, step=3)
st.write(f'x is {x}')

st.divider()

# FILE UPLOADER
uploaded_file = st.file_uploader('Carga un archivo:', type=['txt', 'csv', 'xlsx'])
if uploaded_file:
    st.write(uploaded_file)
    if uploaded_file.type == 'text/plain':
        from io import StringIO
        stringio = StringIO(uploaded_file.getvalue().decode('utf-8'))
        string_data = stringio.read()
        st.write(string_data)
    elif uploaded_file.type == 'text/csv':
        import pandas as pd
        df = pd.read_csv(uploaded_file)
        st.write(df)
    else:
        import pandas as pd
        df = pd.read_excel(uploaded_file)
        st.write(df)


# CAMERA INPUT
camera_photo = st.camera_input('Toma una foto')
if camera_photo:
    st.image(camera_photo)

# Run it: streamlit run .\file.py
