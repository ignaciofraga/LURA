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

foto_1               = 'DATOS/IMAGENES/ieo.jpg'    
archivo_recortable   = 'DATOS/PLANO_LURA_A3.pdf'






# # LOGOS INICIO
imagen_pagina = Image.open(logo_IEO_principal) 
st.image(imagen_pagina) 


# Despliega un botón lateral para seleccionar el tipo de página      
acciones     = ['Conoce el Lura', 'Descargar recortable','Consruye tu red de plancton']
tipo_entrada = st.sidebar.radio("Explora!",acciones)



# PAGINA PARA CONCER EL LURA   
if tipo_entrada == acciones[0]:

    # Texto
    texto = 'Qué es el Lura?'
    titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
    st.markdown(titulo_principal, unsafe_allow_html=True)

    # Texto
    texto = 'El Lura es el barco que utilizan los investigadores del Centro Oceanográfico de A Coruña para estudiar la costa cercana a la ciudad. Se trata de un antiguo buque de pesca, de 14 metros de eslora (longitud) y 4 de manga (anchura) acondicionado para trabajos científicos'
    titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
    st.markdown(titulo_principal, unsafe_allow_html=True)
    
    imagen_pagina = Image.open(foto_Lura_1) 
    st.image(imagen_pagina) 
    
    texto = 'Cuando el tiempo lo permite, los investigadores y marineros del IEO muestrean la columna de agua en una serie de puntos concretos. Se miden diferentes variables físicas (temperatura, salinidad,...), químicas (oxígeno disuelto, pH,...) y biológicas (biomasa de plancton, concentración de clorofila). El IEO lleva casi 40 años haciendo estos estudios, lo que le ha permitido recopilar mucha información, fundamental para estudiar el cambio climático o conocer la salud de nuestra costa.' 
    titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
    st.markdown(titulo_principal, unsafe_allow_html=True)

    texto = 'El IEO también estudia los bancos de peces de la zona, una información muy útil en una región como Galicia, donde la pesca es una actividad muy importante'
    titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">' + texto + '</p>'
    st.markdown(titulo_principal, unsafe_allow_html=True)

'Esta información es la base de estudios como los relacionados con el cambio climático'

if tipo_entrada == acciones[1]:

    # TITULO PRINCIPAL
    titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;">Monta el barco del Oceanográfico</p>'
    st.markdown(titulo_principal, unsafe_allow_html=True)
    titulo_principal = '<p style="text-align: center;font-family:Bahnschrift; font-size: 35px;"> de A Coruña en tu propia casa !!</p>'
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
     
