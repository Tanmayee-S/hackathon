# -*- coding: utf-8 -*-
import streamlit as st
import requests

# Enter your API key here
api_key = "5b90c2c2928233d20227be68c77953fd"

# base_url variable to store the URL
base_url = "http://api.openweathermap.org/data/2.5/weather?"

# Streamlit app title
st.title('Weather Information')

# Input for city name
city_name = st.text_input('Enter city name:')

if st.button('Get Weather'):
    # Check if the user entered a city name
    if city_name:
        # Complete URL for the API request
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name

        # Send a GET request to the API
        response = requests.get(complete_url)

        # Check the status code of the response
        if response.status_code == 200:
            # Convert the response data to JSON
            data = response.json()

            # Extract and display weather information
            temperature = data['main']['temp']
            pressure = data['main']['pressure']
            humidity = data['main']['humidity']
            description = data['weather'][0]['description']

            st.write(f"Temperature: {temperature} K")
            st.write(f"Atmospheric Pressure: {pressure} hPa")
            st.write(f"Humidity: {humidity} %")
            st.write(f"Description: {description}")
        else:
            st.write("City Not Found")

    else:
        st.write("Please enter a city name.")
