import streamlit as st

import requests

import geopy

 

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
            #if
         

            # Extract and display weather information

            temperature = data['main']['temp']
           
            temperaturef = (temperature - 273.15) * 9/5 + 32

            pressure = data['main']['pressure']

            humidity = data['main']['humidity']

            description = data['weather'][0]['description']

            wind = data['wind']['speed']

            st.write(f"Temperature: {temperaturef} F")

            st.write(f"Atmospheric Pressure: {pressure} hPa")

            st.write(f"Humidity: {humidity} %")

            st.write(f"Description: {description}")
           
            st.write(f"Wind speed: {wind}")
           
            #try damaging winds
            #wind = 70
           
            if wind>50:
                st.write(f"Damaging winds, get to secure structure")
                st.write(f"For more information click this link")
                url = 'https://www.statefarm.com/simple-insights/residence/ways-to-stay-safe-during-a-severe-wind-event'
                st.markdown(f'''<a href={url}><button style="background-color:Red;">Damaging Winds</button></a>''',unsafe_allow_html=True)
               
            #try red flag warning
            #wind = 16
            #humidity = 0
            if wind>15 and humidity<25:
                st.write(f"Red Flag Warning")
                st.write(f"For more information click this link")
                url = 'https://www.statefarm.com/simple-insights/safety/wildfire'
                st.markdown(f'''<a href={url}><button style="background-color:Red;">Red Flag Warning</button></a>''',unsafe_allow_html=True)
            
            if temperaturef<32:
                st.write(f"Freeze Warning")
                st.write(f"For more information click this link")
                url = 'https://www.statefarm.com/simple-insights/safety/winter-storm'
                st.markdown(f'''<a href={url}><button style="background-color:Red;">Freeze Warning</button></a>''',unsafe_allow_html=True)
               
               
               
               
               

        else:

            st.write("City Not Found")

 

    else:

        st.write("Please enter a city name.")

