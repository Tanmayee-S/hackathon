# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 18:13:40 2023

@author: siddi
"""

import streamlit as st

def app():
    
    st.title(':red[User Authentication Service]')
    
    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    if choice=='Login':
        
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        
        st.button('Login')
        
    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        
        username = st.text_input('Enter your unique username')
        
        st.button('Create My Account')

