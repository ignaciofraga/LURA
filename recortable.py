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

st.markdown('<div style="text-align: center;font-size: 3rem !important;">Monta el barco del Centro Oceanográfico en tu propia casa!</div>', unsafe_allow_html=True)

st.text('Descarga el recortable pulsando en el botón inferior. Imprime los planos en un A3, monta el barco y comienza a navegar!!')
        
#{font-size: 3rem !important;}
    
with open(archivo_recortable, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

st.download_button(label="DESCARGAR RECORTABLE",
                    data=PDFbyte,
                    file_name="RECORTABLE_LURA_IEO.pdf",
                    mime='application/octet-stream')

st.text('Aquí tienes unas fotos del barco terminado, para que te ayuden en el montaje')


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
     
