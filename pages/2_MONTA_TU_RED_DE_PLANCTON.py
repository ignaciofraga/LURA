# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2023

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_reducido    = 'DATOS/IMAGENES/ieo.ico'
logo_IEO_principal   = 'DATOS/IMAGENES/LOGOS.jpg' 

foto_red             = 'DATOS/IMAGENES/red_casera.PNG'

archivo_red          = 'DATOS/RED_PLANCTON.pdf'


imagen_logo   = Image.open(logo_IEO_reducido)
st.set_page_config(page_title="CONOCE EL LURA",page_icon=logo_IEO_reducido)  # , layout="wide"

logo_cabecera = Image.open(logo_IEO_principal) 
st.image(logo_cabecera)


# TEXTOS 
texto = 'Monta una red de plancton para hacer tus propios muestreos!.'
titulo_principal = '<p style="text-align:  center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

imagen_pagina = Image.open(foto_red) 
st.image(imagen_pagina)   
st.caption('Cabina y tejado montados')

texto = 'Descarga el pdf en el enlace que encontrarás más abajo. Sigue las intrucciones y construye una red de plancton como la que utiliza el Lura en sus muestreos'
titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

col1, col2, col3, col4, col5 = st.columns(5,gap="small")

with col3:

    with open(archivo_red, "rb") as pdf_file:
        PDFbyte = pdf_file.read()

    st.download_button(label="DESCARGAR INSTRUCCIONES",
                data=PDFbyte,
                file_name="RED_PLANCTON_IEO.pdf",
                mime='application/octet-stream')
    

