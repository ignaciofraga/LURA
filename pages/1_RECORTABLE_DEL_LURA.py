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
archivo_recortable   = 'DATOS/RECORTABLE_LURA.pdf'


imagen_logo   = Image.open(logo_IEO_reducido)
st.set_page_config(page_title="CONOCE EL LURA",page_icon=logo_IEO_reducido)  # , layout="wide"


# TITULO PRINCIPAL
texto = 'Monta el barco del Centro Oceanográfico de A Coruña de A Coruña en tu propia casa !!'
titulo_principal = '<p style="text-align:  center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

# DESCARGA RECORTABLE
#titulo_secundario = '<p style="text-align: center;font-family:Gothic Light; font-size: 20px;"> Imprime los planos en un A3, monta el barco y comienza a navegar</p>'
titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Imprime los planos, monta el barco y comienza a navegar</p>'

st.markdown(titulo_secundario, unsafe_allow_html=True)
    
with open(archivo_recortable, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

col1, col2, col3, col4, col5 = st.columns(5,gap="small")

with col3:

    st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_LURA_IEO.pdf",
                    mime='application/octet-stream')



# FOTOS GUIA
titulo_fotos = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Aquí tienes unas fotos del barco terminado, para que te ayuden en el montaje</p>'
st.markdown(titulo_fotos, unsafe_allow_html=True)


# Despliega la extensión para subir los archivos .btl y .cnv
col1, col2 = st.columns(2,gap="small")

with col1:
    imagen_pagina = Image.open(foto_1) 
    st.image(imagen_pagina)   
    st.caption('Vista general del barco terminado')
    
    imagen_pagina = Image.open(foto_1) 
    st.image(imagen_pagina)   
    st.caption('Detalle de la zona de popa')    
    
with col2:
    imagen_pagina = Image.open(foto_1) 
    st.image(imagen_pagina)   
    st.caption('Vista general del barco terminado')
    
    imagen_pagina = Image.open(foto_1) 
    st.image(imagen_pagina)   
    st.caption('Detalle de la zona de proa')    
 

