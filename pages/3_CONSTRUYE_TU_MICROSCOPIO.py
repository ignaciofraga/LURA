# -*- coding: utf-8 -*-
"""
Created on Tue Jun  4 10:29:46 2024

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_reducido    = 'DATOS/IMAGENES/ieo.ico'
logo_IEO_principal   = 'DATOS/IMAGENES/LOGOS.jpg' 

foto_red             = 'DATOS/IMAGENES/red_casera.PNG'

archivo_red          = 'DATOS/RED_PLANCTON.pdf'


imagen_logo   = Image.open(logo_IEO_reducido)
st.set_page_config(page_title="DIVULGACION CORUÑA",page_icon=logo_IEO_reducido)  # , layout="wide"

logo_cabecera = Image.open(logo_IEO_principal) 
st.image(logo_cabecera)


# TEXTOS 
texto = 'Construye un microscopio y sumérgete en el mundo de los organismos más pequeños!.'
titulo_principal = '<p style="text-align:  center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

imagen_pagina = Image.open(foto_red) 
st.image(imagen_pagina)   

texto = 'Descarga el PDF en el enlace que encontrarás más abajo. Sigue las intrucciones y construye un microscopio como el que utilizan los científicos marinos.'
titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

col1, col2, col3 = st.columns(3,gap="small")

with open(archivo_red, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

with col2:

    st.download_button(label="DESCARGAR INSTRUCCIONES",
                data=PDFbyte,
                file_name="MICROSCOPIO_IEO.pdf",
                mime='application/octet-stream')
    