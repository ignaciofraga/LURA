# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2023

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_principal   = 'DATOS/IMAGENES/LOGOS.jpg' 
logo_centro_coruna   = 'DATOS/IMAGENES/logo_IEO_Coru.jpg' 

foto_1               = 'DATOS/IMAGENES/ieo.jpg'    
archivo_recortable   = 'DATOS/PLANO_LURA_A3.pdf'


# # LOGOS INICIO
imagen_pagina = Image.open(logo_IEO_principal) 
st.image(imagen_pagina) 

# col1, col2 = st.columns(2,gap="small")

# with col1:
#     imagen_pagina = Image.open(logo_centro_coruna) 
#     st.image(imagen_pagina)     
    
# with col2:
#     imagen_pagina = Image.open(logo_IEO_principal) 
#     st.image(imagen_pagina)   


# TITULO PRINCIPAL
titulo_principal = '<p style="text-align: center;font-family:Gothic Bold; font-size: 35px;">Monta el barco del Oceanográfico</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)
titulo_principal = '<p style="text-align: center;font-family:Gothic Light; font-size: 35px;"> de A Coruña en tu propia casa !!</p>'
st.markdown(titulo_principal, unsafe_allow_html=True)

# DESCARGA RECORTABLE
#titulo_secundario = '<p style="text-align: center;font-family:Gothic Light; font-size: 20px;"> Imprime los planos en un A3, monta el barco y comienza a navegar</p>'
titulo_secundario = '<p style="text-align: center;font-family:Bahnschrift; font-size: 20px;"> Imprime los planos en un A3, monta el barco y comienza a navegar</p>'

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
titulo_fotos = '<p style="text-align: center;font-family:Gothic; font-size: 20px;"> Aquí tienes unas fotos del barco terminado, para que te ayuden en el montaje</p>'
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
     
