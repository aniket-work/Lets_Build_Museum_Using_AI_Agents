import sys
sys.stdout = sys.__stdout__

import streamlit as st
import requests
from time import sleep
import logging

# Configure logging to print logs in the command prompt
root_logger = logging.getLogger()
root_logger.setLevel(logging.INFO)  # Set the logging level to INFO
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
console_handler.setFormatter(formatter)
root_logger.addHandler(console_handler)

# Set up the Streamlit page configuration with title, icon, and wide layout
st.set_page_config(
    page_title="Dinosaur Gallery",
    page_icon=":sauropod:",
    layout="wide"
)

# Display a background image
background_image = "images/road_map.jpg"
st.image(background_image, use_column_width=True)

# Dictionary containing dinosaur names and their corresponding image file paths
dinosaurs = {
    "Tyrannosaurus Rex": "images/trex.jpg",
    "Velociraptor": "images/velociraptor.jpg",
    "Triceratops": "images/triceratops.jpg",
    "Brachiosaurus": "images/brachiosaurus.jpg",
    "Stegosaurus": "images/stegosaurus.jpg",
    "Diplodocus": "images/diplodocus.jpg",
    "Pteranodon": "images/pteranodon.jpg",
}

def send_post_request(query, selected_dino):
    """
    Sends a POST request to the specified URL with the user's query and selected dinosaur.

    Args:
        query (str): The user's input query.
        selected_dino (str): The name of the selected dinosaur.

    Returns:
        dict: The response data from the API.
    """
    url = "http://127.0.0.1:8080/llm"
    payload = {"query": query, "selected_dino": selected_dino}
    st.write(f"Payload: {payload}")
    response = requests.post(url, json=payload)

    # Wait for the response to be received
    while response.status_code != 200:
        sleep(0.1)

    response_data = response.json()
    st.write(f"Response: {response_data}")
    return response_data

# Set the title of the Streamlit app
st.title("Dinosaur Gallery")

# Add blurred background image with green background color and dark font color
st.markdown(
    """
    <style>
        .stApp {
            background-image: url('images/road_map.jpg');
            background-size: cover;
            background-attachment: fixed;
            background-color: rgba(0, 128, 0, 0.6);
            color: black;
        }
        .stMarkdown, .stTitle, .stTextInput > label, .stCheckbox > label {
            color: black;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Organize the images into rows
row1_dinos = list(dinosaurs.items())[:3]
row2_dinos = list(dinosaurs.items())[3:6]
row3_dinos = list(dinosaurs.items())[6:]

# Display the first row with spacing
col1, col2, col3 = st.columns(3)
with col1:
    st.image(row1_dinos[0][1], caption=row1_dinos[0][0], use_column_width=True)
    selected_dino = None
    if st.checkbox(f"Select {row1_dinos[0][0]}"):
        selected_dino = row1_dinos[0][0]
        user_input = st.text_input("Enter your query:")
        if st.button("Submit"):
            response = send_post_request(user_input, selected_dino)
with col2:
    st.image(row1_dinos[1][1], caption=row1_dinos[1][0], use_column_width=True)
    selected_dino = None
    if st.checkbox(f"Select {row1_dinos[1][0]}"):
        selected_dino = row1_dinos[1][0]
        user_input = st.text_input("Enter your query:")
        if st.button("Submit"):
            response = send_post_request(user_input, selected_dino)
with col3:
    st.image(row1_dinos[2][1], caption=row1_dinos[2][0], use_column_width=True)
    selected_dino = None
    if st.checkbox(f"Select {row1_dinos[2][0]}"):
        selected_dino = row1_dinos[2][0]
        user_input = st.text_input("Enter your query:")
        if st.button("Submit"):
            response = send_post_request(user_input, selected_dino)

# Add spacing between rows
st.write("")
st.write("")

# Display the second row with spacing
col1, col2, col3 = st.columns(3)
with col1:
    st.image(row2_dinos[0][1], caption=row2_dinos[0][0], use_column_width=True)
    selected_dino = None
    if st.checkbox(f"Select {row2_dinos[0][0]}"):
        selected_dino = row2_dinos[0][0]
        user_input = st.text_input("Enter your query:")
        if st.button("Submit"):
            response = send_post_request(user_input, selected_dino)
with col2:
    st.image(row2_dinos[1][1], caption=row2_dinos[1][0], use_column_width=True)
    selected_dino = None
    if st.checkbox(f"Select {row2_dinos[1][0]}"):
        selected_dino = row2_dinos[1][0]
        user_input = st.text_input("Enter your query:")
        if st.button("Submit"):
            response = send_post_request(user_input, selected_dino)
with col3:
    st.image(row2_dinos[2][1], caption=row2_dinos[2][0], use_column_width=True)
    selected_dino = None
    if st.checkbox(f"Select {row2_dinos[2][0]}"):
        selected_dino = row2_dinos[2][0]
        user_input = st.text_input("Enter your query:")
        if st.button("Submit"):
            response = send_post_request(user_input, selected_dino)

# Add spacing between rows
st.write("")
st.write("")

# Display the third row
col1, _ = st.columns([3, 1])
with col1:
    st.image(row3_dinos[0][1], caption=row3_dinos[0][0], use_column_width=True)
    selected_dino = None
    if st.checkbox(f"Select {row3_dinos[0][0]}"):
        selected_dino = row3_dinos[0][0]
        user_input = st.text_input("Enter your query:")
        if st.button("Submit"):
            response = send_post_request(user_input, selected_dino)

# Display the background image again
background_image = "images/road_map.jpg"
st.image(background_image, use_column_width=True)
