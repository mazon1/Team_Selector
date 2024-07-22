import streamlit as st
from google.cloud import firestore
import firebase_admin
from firebase_admin import credentials
import json

# Initialize Firebase
firebase_credentials = {
    "type": "service_account",
    "project_id": "your_project_id",
    "private_key_id": "your_private_key_id",
    "private_key": "-----BEGIN PRIVATE KEY-----\nyour_private_key_content\n-----END PRIVATE KEY-----\n",
    "client_email": "your_client_email",
    "client_id": "your_client_id",
    "auth_uri": "https://accounts.google.com/o/oauth2/auth",
    "token_uri": "https://oauth2.googleapis.com/token",
    "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
    "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/your_client_email"
}

cred = credentials.Certificate(firebase_credentials)
firebase_admin.initialize_app(cred)

# Initialize Firestore DB
db = firestore.client()

# Function to save data to Firestore
def save_to_firestore(data):
    db.collection('user_inputs').add(data)

# Streamlit app
st.title("Team Selection App")

# Load and display the logo
st.image("teamselectorapp.jfif", width=100)

# Input fields
name = st.text_input("Name")
project_management = st.selectbox("Project Management", ["Novice", "Competent", "Proficient", "Expert"])
public_speaking = st.selectbox("Public Speaking", ["Novice", "Competent", "Proficient", "Expert"])
ppt_development = st.selectbox("PPT/Story Development", ["Novice", "Competent", "Proficient", "Expert"])
database_management = st.selectbox("Database Management", ["Novice", "Competent", "Proficient", "Expert"])
coding = st.selectbox("Coding", ["Novice", "Competent", "Proficient", "Expert"])
deployment = st.selectbox("Deployment", ["Novice", "Competent", "Proficient", "Expert"])
passion = st.selectbox("Passion", ["Coding", "Documentation & Research", "Presentation & Communication"])

# Function to recommend role based on inputs
def recommend_role(data):
    if data["coding"] == "Expert":
        return "Lead Developer"
    elif data["project_management"] == "Expert":
        return "Lead Project Manager"
    elif data["ppt_development"] == "Expert":
        return "Lead Presenter"
    elif data["public_speaking"] == "Expert":
        return "Lead Speaker"
    elif data["database_management"] == "Expert":
        return "Lead Database Manager"
    elif data["deployment"] == "Expert":
        return "Lead Deployment Specialist"
    else:
        return data["passion"]

# Button to save input and recommend role
if st.button("Submit"):
    data = {
        "name": name,
        "project_management": project_management,
        "public_speaking": public_speaking,
        "ppt_development": ppt_development,
        "database_management": database_management,
        "coding": coding,
        "deployment": deployment,
        "passion": passion,
    }
    recommended_role = recommend_role(data)
    data["recommended_role"] = recommended_role
    save_to_firestore(data)
    st.success(f"Data saved to Firebase Firestore! Recommended Role: {recommended_role}")

# Button to recommend lead role
if st.button("Recommend Lead Role"):
    data = {
        "project_management": project_management,
        "public_speaking": public_speaking,
        "ppt_development": ppt_development,
        "database_management": database_management,
        "coding": coding,
        "deployment": deployment,
        "passion": passion,
    }
    recommended_role = recommend_role(data)
    st.write(f"Recommended Lead Role: {recommended_role}")
