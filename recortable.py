# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2023

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_principal   = 'DATOS/IMAGENES/ieo.jpg'    
archivo_recortable   = 'DATOS/PLANO_LURA_A3.pdf'


#st.title("**Monta el barco del Centro Oceanográfico en tu propia casa!**")

titulo_principal = '<p style="text-align: center;font-family:Gothic Bold; font-size: 35px;">Monta el barco del Oceanográfico</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)
titulo_principal = '<p style="text-align: center;font-family:Gothic Light; font-size: 35px;"> de A Coruña en tu propia casa !!</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)


titulo_secundario = '<p style="text-align: center;font-family:Gothic Light; font-size: 20px;"> Imprime los planos en un A3, monta el barco y comienza a navegar</p>'
st.markdown(titulo_secundario, unsafe_allow_html=True)
    
with open(archivo_recortable, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

col1, col2, col3, col4, col5 = st.columns(5,gap="small")

with col3:

    st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_LURA_IEO.pdf",
                    mime='application/octet-stream')



titulo_fotos = '<p style="text-align: center;font-family:Gothic; font-size: 20px;"> Aquí tienes unas fotos del barco terminado, para que te ayuden en el montaje</p>'
st.markdown(titulo_fotos, unsafe_allow_html=True)


# Despliega la extensión para subir los archivos .btl y .cnv
col1, col2 = st.columns(2,gap="small")

with col1:
    imagen_pagina = Image.open(logo_IEO_principal) 
    st.image(imagen_pagina)   
    st.caption('Vista general del barco terminado')
    
    imagen_pagina = Image.open(logo_IEO_principal) 
    st.image(imagen_pagina)   
    st.caption('Detalle de la zona de popa')    
    
with col2:
    imagen_pagina = Image.open(logo_IEO_principal) 
    st.image(imagen_pagina)   
    st.caption('Vista general del barco terminado')
    
    imagen_pagina = Image.open(logo_IEO_principal) 
    st.image(imagen_pagina)   
    st.caption('Detalle de la zona de proa')    
     
