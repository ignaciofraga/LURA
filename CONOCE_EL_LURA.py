# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2023

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_principal   = 'DATOS/IMAGENES/LOGOS.jpg' 
logo_centro_coruna   = 'DATOS/IMAGENES/logo_IEO_Coru.jpg' 
foto_Lura_1          = 'DATOS/IMAGENES/LURA.jpg'
foto_roseta          = 'DATOS/IMAGENES/roseta_red.jpg'
logo_IEO_reducido    = 'DATOS/IMAGENES/ieo.ico'
foto_1               = 'DATOS/IMAGENES/ieo.jpg'    
archivo_recortable   = 'DATOS/PLANO_LURA_A3.pdf'



imagen_logo   = Image.open(logo_IEO_reducido)
st.set_page_config(page_title="CONOCE EL LURA",page_icon=logo_IEO_reducido)  # , layout="wide"


# Texto
texto = 'Qué es el Lura?'
titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

# Texto
texto = 'El Lura es el barco que utilizan los investigadores del Centro Oceanográfico de A Coruña para estudiar la costa cercana a la ciudad. Se trata de un antiguo buque de pesca, de 14 metros de eslora (longitud) y 4 de manga (anchura) acondicionado para trabajos científicos.'
titulo_principal = '<p style="text-align:  justify;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

imagen_pagina = Image.open(foto_Lura_1) 
st.image(imagen_pagina)
st.caption('Fotografía del Lura tomada por Mar Nieto, una de las investigadoras del Centro Oceanográfico')

texto = 'Cuando el tiempo lo permite, los investigadores y marineros del IEO se embarcan en el Lura y salen a muestrear una serie de puntos concretos en el mar. Se miden diferentes variables físicas (temperatura, salinidad,...), químicas (oxígeno disuelto, pH,...) y biológicas (biomasa de plancton, concentración de clorofila,...). El IEO lleva casi 40 años haciendo estos muestreos, lo que le ha permitido recopilar una información que es fundamental para estudiar el cambio climático o conocer la salud de nuestra costa.' 
titulo_principal = '<p style="text-align:  justify;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

texto = 'Para tomar muestras del agua, el Lura tiene una roseta oceanográfica. La roseta es una estructura metálica con varias botellas de plástico a su alrededor. Desde una grúa situada a bordo del Lura se sumerge la roseta a distintas profundidades, y en cada una de ellas se cierra una botella, atrapando el agua del mar que se recupera al volver a subir la roseta al barco. Las muestras recogidas se analizan en nuestros laboratorios una vez el barco vuelve al puerto.'
titulo_principal = '<p style="text-align:  justify;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

imagen_pagina = Image.open(foto_roseta) 
st.image(imagen_pagina)   
st.caption('Fotografía de una roseta oceanográfica')

texto = 'Para recoger muestras de plancton se utilizan unas redes especiales. Se trata de redes muy finas, que atrapan los organismos más grandes que el tamaño (la "luz") de la malla y los concentran en un extremo de la red. Las redes se arrastran desde el barco cuando éste se desplaza.'
titulo_principal = '<p style="text-align:  justify;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

imagen_pagina = Image.open(foto_1) 
st.image(imagen_pagina)   
st.caption('Fotografía de una red de plancton')

texto = 'También se estudian los bancos de peces de la zona, una información muy útil en una región como Galicia, donde la pesca es una actividad tan importante. Para capturar los peces y estudiarlos se utilizan redes de pesca, con luces mucho mayores que las de plancton.'
titulo_principal = '<p style="text-align:  justify;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

imagen_pagina = Image.open(foto_1) 
st.image(imagen_pagina)   
st.caption('Fotografía de una red de pesca')


texto = 'Dónde está el Lura?'
titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

texto = 'El Lura tiene su base en el puerto de A Coruña, pero mucho días lo puedes ver navegando por nuestras costas. En el siguiente enlace puedes conocer dónde se encuentra en cada momento!.'
titulo_principal = '<p style="text-align:  justify;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

st.write("Descubre dónde está el Lura pinchando [aquí](https://www.vesselfinder.com/es/?mmsi=224000100)")




