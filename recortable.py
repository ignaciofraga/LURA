# -*- coding: utf-8 -*-
"""
Created on Mon Apr 24 11:13:13 2023

@author: ifraga
"""

import streamlit as st
from PIL import Image

logo_IEO_principal    = 'DATOS/IMAGENES/logo-CSIC.jpg'    

st.title("Plataforma de datos biogeoquímicos del C.O de A Coruña")

# Añade el logo del IEO
imagen_pagina = Image.open(logo_IEO_principal) 
st.image(imagen_pagina)
