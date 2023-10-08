import streamlit as st
import subprocess

def app():
    st.title(':lock: User Authentication Service')

    choice = st.selectbox('Login/Signup', ['Login', 'Sign Up'])
    
    if choice == 'Login':
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        
        if st.button('Login'):
           try:
                user = auth.get_user_by_email(email)
                st.success("Login Successful!")
                # Redirect to the dashboard app
                subprocess.Popen(["streamlit", "run", "test3.py"])
           except auth.UserNotFoundError:
                st.warning('Login Failed: User not found.')
           except auth.AuthError:
                st.warning('Login Failed: Incorrect password.')
        
    else:
        email = st.text_input('Email Address')
        password = st.text_input('Password', type='password')
        username = st.text_input('Enter your unique username')
        
        if st.button('Create My Account'):
            try:
                # Create a new user with Firebase Authentication
                user = auth.create_user(email=email, password=password, uid=username)
                st.success("Account Created Successfully!")
                st.markdown("Please Login using email and password")
                st.balloons()
            except auth.EmailAlreadyExistsError:
                st.warning('Account creation failed: Email already exists.')

if __name__ == "__main__":
    app()
