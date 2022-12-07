import streamlit as st
import requests
from settings import *

#  query teh api for the number of people who want to die
#  and display it on the page

#  get req on /count
#  get the number of people who want to die

server_dest = f"http://{BACKEND_IP}:{BACKEND_PORT}/count"

st.write("# welcome to the DVIC death wish list")

st.write("## number of people who want to die")

st.write(requests.get(server_dest).text)


st.write("contribute to the project on github: ")
st.write("https://github.com/COLVERTYETY/DVIC_deathWish")