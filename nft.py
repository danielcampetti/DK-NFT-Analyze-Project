import streamlit as st
import requests, json

endpoint = st.sidebar.selectbox("Endpoints",['Assets','Events','Rarity'])
st.header(f"DK NFT API Analyze - {endpoint}")

st.sidebar.write("Some sidebar")

if endpoint =="Assets":

    params = {
        'collection': 'the-wanderers',
        'limit':1
    }

    r= requests.get("https://api.opensea.io/api/v1/assets")

    st.write(r.json())
