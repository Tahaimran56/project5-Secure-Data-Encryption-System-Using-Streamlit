# Streamlit Data Storage and Retrieval App

This Streamlit app allows users to store and retrieve data securely with a passkey. The app supports the following features:

- **Store Data**: Users can store data under a username with a passkey.
- **Retrieve Data**: Users can retrieve the stored data by providing the correct passkey for their username.

## Features

- **Data Storage**: You can store data with a specific username and protect it with a hashed passkey.
- **Data Retrieval**: Users can retrieve their data by entering the correct passkey. If the passkey is incorrect, users will have limited attempts to enter the correct one.
- **Security**: Passkeys are hashed using SHA256, ensuring that passkey data is stored securely and not in plaintext.
- **Failed Attempts**: Users are allowed a maximum of 3 failed login attempts before being locked out.

## Installation

To run this app, you'll need to have Python and the following libraries installed:

- Streamlit
- hashlib (part of Python's standard library)

### Requirements

- Python 3.x
- Streamlit

You can install the required dependencies using pip:

```bash
pip install streamlit
