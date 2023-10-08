import streamlit as st
import pymongo
import datetime
import pandas as pd
from sklearn.linear_model import LinearRegression
import subprocess

# Streamlit configuration
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

# Colors
primary_color = "#ED1D24"   # Red
secondary_color = "#f5f5f5"  # Beige
background_color = "#FFFFFF" # White

# Sidebar
st.sidebar.image('https://logos-world.net/wp-content/uploads/2021/10/State-Farm-Symbol.png', width=80)
st.sidebar.header('Welcome, John Smith')
st.sidebar.write("Member since 2023")

# Main title
st.title("Asset Management")

# Home Information
home_info = {
    "Location": "1234 Elm Street, Springfield, IL",
    "Year Built": 1990,
    "Heating Type": "Gas",
    "Security System": "Yes",
    "Insurance Plan": "State Farm Homeowners Insurance",
}

st.header("My Home")
st.write(f"**Location:** {home_info['Location']}")
st.write(f"**Year Built:** {home_info['Year Built']}")
st.write(f"**Heating Type:** {home_info['Heating Type']}")
st.write(f"**Security System:** {home_info['Security System']}")
st.write(f"**Insurance Plan:** {home_info['Insurance Plan']}")

# Home Maintenance
home_maintenance_data = []
st.header("Home Maintenance")
st.subheader("Add Home Maintenance Task")
task_name = st.text_input("Task Name:")
task_due_date = st.date_input("Due Date:", datetime.date.today())

if st.button("Add Task"):
    home_maintenance_data.append({"Task Name": task_name, "Due Date": task_due_date})
    st.success("Task added successfully!")

for task in home_maintenance_data:
    st.write(f"- {task['Task Name']} (Due on: {task['Due Date']})")

# Vehicle Information
vehicle_info = {
    "Make": "Toyota",
    "Model": "Camry",
    "Year": 2020,
    "Mileage": 15000,
    "Fuel Type": "Gasoline",
    "Transmission": "Automatic",
    "Engine Type": "4-cylinder",
    "License Plate": "ABC123",
    "Insurance Provider": "State Farm",
    "Last Oil Change": "",
    "Last Tire Rotation": "",
}

st.header("My Vehicle")
st.subheader("Vehicle Information")
st.write(f"**Make:** {vehicle_info['Make']}")
st.write(f"**Model:** {vehicle_info['Model']}")
st.write(f"**Year:** {vehicle_info['Year']}")
st.write(f"**Mileage:** {vehicle_info['Mileage']} miles")
st.write(f"**Fuel Type:** {vehicle_info['Fuel Type']}")
st.write(f"**Transmission:** {vehicle_info['Transmission']}")
st.write(f"**Engine Type:** {vehicle_info['Engine Type']}")
st.write(f"**License Plate:** {vehicle_info['License Plate']}")
st.write(f"**Insurance Provider:** {vehicle_info['Insurance Provider']}")

# Vehicle Maintenance Data
vehicle_data = pd.DataFrame({
    'Mileage': [1000, 2000, 3000, 4000, 5000],
    'Last_Oil_Change_Months': [2, 4, 6, 8, 10]
})

st.header("Vehicle Maintenance Data")
st.dataframe(vehicle_data)

vehicle_data['Recommended_Oil_Change_Months'] = vehicle_data['Mileage'] / 1000 * 3

X = vehicle_data[['Mileage']]
y = vehicle_data['Recommended_Oil_Change_Months']
model = LinearRegression()
model.fit(X, y)

current_mileage = st.number_input("Enter your current mileage:", min_value=0)
recommended_months = model.predict([[current_mileage]])[0]

st.subheader("Recommended Oil Change")
st.write(f"Based on your current mileage, it is recommended to change the oil every {recommended_months:.2f} months.")

st.subheader("Maintenance History")
vehicle_info["Last Oil Change"] = st.date_input("Last Oil Change:")
vehicle_info["Last Tire Rotation"] = st.date_input("Last Tire Rotation:")

st.subheader("Maintenance Schedule")
st.write("- Oil Change: Every 3,000 miles or 3 months")
st.write("- Tire Rotation: Every 6,000 miles or 6 months")

st.subheader("Vehicle Sensors")
st.subheader("Vehicle Maintenance Tips & Tutorials")

# Preventative Services
if st.button('Weather'):
    try:
        user = auth.get_user_by_email(email)
        st.success("Login Successful!")
        # Redirect to the dashboard app
        subprocess.Popen(["streamlit", "run", "weather.py"])
    except:
        st.warning('Login Failed: User not found.')