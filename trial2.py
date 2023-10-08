# -*- coding: utf-8 -*-
"""
Created on Sat Oct  7 19:31:05 2023

@author: siddi
"""

import streamlit as st
import firebase_admin

from firebase_admin import credentials 
from firebase_admin import auth

cred = credentials.Certificate('hackuta2023-a3ddb-0209903e3290.json')


def app():
    st.title(':red[:lock: User Authentication Service]')

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    
    def f():
        try:
            user = auth.get_user_by_email(email)
           #  print(user.uid)
            st.success("Account Created Successfully!")
            
        except:
            st.warning('Login Failed')
    

    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        
        st.button('Login', on_click=f())
            
        
    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')
        
        if st.button('Create My Account'):
            user = auth.create_user(email = email, password = password, uid=username)
            st.success("Account Created Successfully!")
            st.markdown("Please Login using email and password")
            st.balloons()

if __name__ == "__main__":
    app()
