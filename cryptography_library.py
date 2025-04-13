import streamlit as st
import hashlib

if 'stored_data' not in st.session_state:
    st.session_state.stored_data = {}
if 'failed_attempts' not in st.session_state:
    st.session_state.failed_attempts = {}

MAX_ATTEMPTS = 3


def hash_passkey(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

def store_data():
    username = st.text_input("Username")
    data = st.text_area("Data")
    passkey = st.text_input("Passkey", type="password")
    
    if st.button("Store"):
        if username and data and passkey:
            
            st.session_state.stored_data[username] = {'data': data, 'passkey': hash_passkey(passkey)}
            st.success("Data stored!")
        else:
            st.warning("Please fill all fields.")


def retrieve_data():
    username = st.text_input("Username")
    passkey = st.text_input("Passkey", type="password")
    
    
    if username not in st.session_state.failed_attempts:
        st.session_state.failed_attempts[username] = 0
    
    if st.session_state.failed_attempts[username] >= MAX_ATTEMPTS:
        st.warning("Too many failed attempts. Please log in again.")
        return

    if st.button("Retrieve"):
        
        user_data = st.session_state.stored_data.get(username)
        
        if user_data:
        
            if user_data['passkey'] == hash_passkey(passkey):
                st.success(f"Data: {user_data['data']}")
                st.session_state.failed_attempts[username] = 0  
            else:
                st.session_state.failed_attempts[username] += 1
                st.error(f"Wrong passkey! Attempts left: {MAX_ATTEMPTS - st.session_state.failed_attempts[username]}")
        else:
            st.warning("No data found for this username.")


st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Store Data", "Retrieve Data"])

if page == "Store Data":
    store_data()
elif page == "Retrieve Data":
    retrieve_data()

