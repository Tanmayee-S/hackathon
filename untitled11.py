# -*- coding: utf-8 -*-
"""
Created on Sun Oct  8 01:41:28 2023

@author: siddi
"""

import pandas as pd
import requests
import pygwalker as pyg
import streamlit as st

# US Data Collection from Wikipedia
url_us = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States'
req_us = requests.get(url_us)
data_list_us = pd.read_html(req_us.text)
target_df_us = data_list_us[0]

# Cleaning Data Set

# Changing Column Names
target_df_us.columns = ['Data Types', 'Data Numbers']

# Removing Unnecessary Rows
target_df_us = target_df_us.drop([0, 1, 2, 3, 4, 5, 6, 11, 13, 14, 15])

# Reset the index and drop the old index
target_df_us = target_df_us.reset_index(drop=True)

# Extracting the Numbers
target_df_us['Data Numbers'] = target_df_us['Data Numbers'].str.extract(
    r'(\d+\D+\d+\D+\d+)')

target_df_us['Data Numbers'] = target_df_us['Data Numbers'].str.replace(
    ',', '', regex=True)

# Changing str to int Data Type
target_df_us['Data Numbers'] = pd.to_numeric(target_df_us['Data Numbers'])

# Exporting Data to csv
target_df_us.to_csv('covid_dataset_in_US.csv', index=False)

df_us = pd.read_csv('covid_dataset_in_US.csv')

# NA Data Collection from Wikipedia

url_na = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_North_America'
req_na = requests.get(url_na)
data_list_na = pd.read_html(req_na.text)
target_df_na = data_list_na[2]

# Cleaning Data Set

# Changing Column Names
target_df_na.columns = ['Country/Territory', 'Cases', 'Deaths', 'Recoveries', 'col6']

# Extracting Only Necessary Columns
target_df_na = target_df_na[['Country/Territory', 'Cases', 'Deaths', 'Recoveries']]

# Replacing "no data" with 0
target_df_na['Recoveries'] = target_df_na['Recoveries'].str.replace('no data', '0')

# Changing str to int Data Type
target_df_na['Cases'] = pd.to_numeric(target_df_na['Cases'])
target_df_na['Deaths'] = pd.to_numeric(target_df_na['Deaths'])
target_df_na['Recoveries'] = pd.to_numeric(target_df_na['Recoveries'])

# Exporting Data to csv
target_df_na.to_csv('covid_dataset_in_NA.csv', index=False)

df_na = pd.read_csv('covid_dataset_in_NA.csv')

# Setting Up Streamlit Page
st.set_page_config(
    page_title="Visualize Covid Data",
    page_icon=":snake:",
    layout="wide",
    initial_sidebar_state="expanded",
)

# Set Title and Subtitle
st.title('Visualize Covid Data')
st.subheader('Play with data extracted from Wikipedia to visualize data about Covid in the US and compare with the rest of North America')

# Implementing first pygwalk (US Data)
def load_config_us(file_path):
    with open(file_path, 'r') as config_file:
        config_str_us = config_file.read()
    return config_str_us

config_us = load_config_us('covid_data_us_config.json')
pyg.walk(df_us, env='Streamlit', dark='dark', spec=config_us)

# Implementing second pygwalk (NA Data)
def load_config_na(file_path):
    with open(file_path, 'r') as config_file:
        config_str_na = config_file.read()
    return config_str_na

config_na = load_config_na('covid_data_na_config.json')
pyg.walk(df_na, env='Streamlit', dark='dark', spec=config_na)
