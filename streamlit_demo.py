import streamlit as st
import time
import pandas as pd

# set page title
st.title('Prueba Streamlit-Mario Torres')

my_select_box = st.sidebar.selectbox('Selecciona País:', list(['US', 'UK', 'DE', 'FR', 'JP']))
my_slider = st.sidebar.slider('Temperatura en Celsius')
st.sidebar.write(f'Temperatura a Fahrenheit: {my_slider * 1.8 + 32}')

def miles_to_km():
	if "miles" not in st.session_state:
		st.session_state.miles = 0  # Inicializa 'miles' con un valor predeterminado
	st.session_state.km = st.session_state.miles * 1.609

def km_to_miles():
	st.session_state.millas = st.session_state.km * 0.621

col1, buff, col2 = st.columns([2, 0.2, 2])

with col1:
	millas = st.number_input('Millas:', key='millas', on_change=miles_to_km)

with col2:
	km = st.number_input('Km:', key='km', on_change=km_to_miles)

if "foto" not in st.session_state:
	st.session_state["foto"] = "not listo"

def change_photo_state():
	st.session_state["foto"] = "listo"

col1, col2, col3 = st.columns([1, 1, 0.5])  # second column is 2 times larger
with col1:
	df = pd.DataFrame({'1_columna': [1, 2, 3, 4], '2_columna': [10, 20, 30, 40]})
	df

# upload photo
uploaded_photo = col2.file_uploader("Cargar una foto:", on_change=change_photo_state)

# take a photo using the camera
camera_photo = col2.camera_input("Take a photo", on_change=change_photo_state)

with col3:
	# display a list
	l1 = [1, 2, 3]
	st.write(l1)
	
	# display a dict
	l2 = list('abc')
	d1 = dict(zip(l1, l2))
	st.write(d1)

if st.session_state["foto"] == "listo":
	# progress bar
	progress_bar = col2.progress(0)
	for i in range(100):
		time.sleep(0.03)
		progress_bar.progress(i)
	
	col2.success("Foto Cargada exitosamente!")
	
	with st.expander("Click para leer mas"):
		st.write("Hola, aquí hay más detalle sobre el tema que estas interesado en leer.")
		
		if uploaded_photo is None:
			st.image(camera_photo)
		else:
			st.image(uploaded_photo)

# Run it: streamlit run .\file.py