import streamlit as st
import json

# Load the JSON file
json_file_path = "selected_clients.json"  # Adjust this path if needed

try:
    with open(json_file_path, "r") as json_file:
        selected_clients_dict = json.load(json_file)
except FileNotFoundError:
    st.error("⚠️ JSON file not found! Please ensure the file is in the correct location.")
    selected_clients_dict = {}

# Streamlit app layout
st.title("🎯 Event Client Invitation Viewer")
st.write("Select an event category to view the clients to invite.")

# Check if dictionary is loaded correctly
if selected_clients_dict:
    # Dropdown selection for event category
    selected_event = st.selectbox("Choose an Event Category:", list(selected_clients_dict.keys()))

    # Display client IDs for the selected event
    if selected_event:
        st.subheader(f"📌 Clients to Invite for: {selected_event}")

        # Search functionality
        search_query = st.text_input("🔍 Search for a client ID:")

        # Filter client IDs based on search input
        filtered_clients = [
            client for client in selected_clients_dict[selected_event] if search_query.lower() in client.lower()
        ]

        # Display client IDs
        st.write(filtered_clients if filtered_clients else "No clients match your search.")
else:
    st.warning("⚠️ No data available. Please upload a valid JSON file.")

