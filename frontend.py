import streamlit as st
import requests
from settings import *

#  query teh api for the number of people who want to die
#  and display it on the page

#  get req on /count
#  get the number of people who want to die

server_dest = f"http://{BACKEND_IP}:{BACKEND_PORT}/count"

st.write("# welcome to the DVIC death wish list")

st.write("## number of people who want to die: ")
try:
    st.write(f"# {requests.get(server_dest).text}")
except:
    st.write("error connecting to the server")

st.write("## list of people who want to die: ")

#  get req on /wishes
#  get the list of people who want to die
#  display it on the page

server_dest = f"http://{BACKEND_IP}:{BACKEND_PORT}/wishes"

try:
    response = requests.get(server_dest)
    res = response.text
    res = res.replace("{", "")
    res = res.replace("}", "")
    res = res.replace('"', "")
    res = res.replace("(", "")
    res = res.replace(")", "\n")
    res = res.replace(":", "")
    res = res.replace(",", "\n")
    st.write(res)

except:
    st.write("error connecting to the server")


st.write("## add your name to the list !!")
#  add a text input to the page
#  when the user presses enter, send a post request to the server
#  with the text input as the body of the request
#  the server should add the text to the list of death wishes
#  and return "OK"
#  if the server returns "OK", display a message saying "your name has been added to the list"
#  if the server returns anything else, display a message saying "there was an error adding your name to the list"

#  add a text input to the page
text = st.text_input("enter your name here", key="deathWish")

st.button("submit", key="submit")

if st.session_state.submit:
    server_dest = f"http://{BACKEND_IP}:{BACKEND_PORT}/wishes"
    try:
        response = requests.post(server_dest, data=str(text))
        if response.text == "OK":
            st.write("your name has been added to the list")
        else:
            st.write("there was an error adding your name to the list")
    except:
        st.write("there was an error adding your name to the list")



#  add to the bottom of the page a link to the github repo
st.write("## contribute to the project")
st.write("https://github.com/COLVERTYETY/DVIC_deathWish")