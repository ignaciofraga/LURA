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


# TITULO PRINCIPAL
texto = 'Monta una red de plancton para hacer tus propios muestreos!.'
titulo_principal = '<p style="text-align:  center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

imagen_pagina = Image.open(foto_1) 
st.image(imagen_pagina)   
st.caption('Detalle de la zona de popa')  
    

