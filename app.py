
import streamlit as st
import pymongo
import pandas as pd
import pymongo
from pymongo import MongoClient
import streamlit.components.v1 as components
import matplotlib.pyplot as plt
import requests
import streamlit.components.v1 as components
import numpy as np
from datetime import datetime, timezone
import statsmodels 
from statsmodels.tsa.seasonal import seasonal_decompose
import plotly.tools
from twilio.rest import Client #Twilio is a service that delivers SMS
import scipy
import seaborn as sns

def main():
    page = st.sidebar.selectbox("Select a Page",["Project", "raw data","analysed data"])

    #First Page
    if page == "Project":
        homepage()

    #Second Page
    elif page == "raw data":
        analyseddata()
    
    #Third Page
    elif page == "analysed data":
        information()
        
def homepage():
    
    st.title('Project')
    st.write('xxxx')
 
def homepage():
    
    st.title('Raw data')
    st.write('xx')
 
    
def homepage():
    
    st.title('Analysed data')
    st.write('xxx')
 
    
    
    
