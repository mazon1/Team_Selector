import streamlit as st
import pandas as pd
import os

# Save user input to CSV function
def save_to_csv(data, filename="user_data.csv"):
    df = pd.DataFrame([data])
    if not os.path.isfile(filename):
        df.to_csv(filename, index=False)
    else:
        df.to_csv(filename, mode='a', header=False, index=False)

# Function to recommend role based on skills
def recommend_role(project_management, public_speaking, ppt_development, database_management, coding, deployment, passion):
    skill_map = {
        "Coding": coding,
        "Documentation & Research": ppt_development,
        "Presentation": public_speaking,
        "Communication": public_speaking
    }
    role = max(skill_map, key=skill_map.get)
    if skill_map[role] == "Novice":
        role = passion  # Default to the passion if no high skill is found
    return role

# App Layout
st.title("Team Selection App")
st.image("teamselectorapp.jpg", width=200)

# User input
name = st.text_input("Name")
project_management = st.selectbox("Project Management", ["Novice", "Competent", "Proficient", "Expert"])
public_speaking = st.selectbox("Public Speaking", ["Novice", "Competent", "Proficient", "Expert"])
ppt_development = st.selectbox("PPT/Story Development", ["Novice", "Competent", "Proficient", "Expert"])
database_management = st.selectbox("Database Management", ["Novice", "Competent", "Proficient", "Expert"])
coding = st.selectbox("Coding", ["Novice", "Competent", "Proficient", "Expert"])
deployment = st.selectbox("Deployment", ["Novice", "Competent", "Proficient", "Expert"])
passion = st.selectbox("Passion", ["Coding", "Documentation & Research", "Presentation", "Communication"])

# Button to recommend role
if st.button("Recommend Lead Role"):
    recommended_role = recommend_role(project_management, public_speaking, ppt_development, database_management, coding, deployment, passion)
    # st.write(f"Recommended Role: {recommended_role}")
    st.markdown(f"### Recommended Role: {recommended_role}")

    # Save user input to CSV
    user_data = {
        "Name": name,
        "Project Management": project_management,
        "Public Speaking": public_speaking,
        "PPT/Story Development": ppt_development,
        "Database Management": database_management,
        "Coding": coding,
        "Deployment": deployment,
        "Passion": passion,
        "Recommended Role": recommended_role
    }
    save_to_csv(user_data)
