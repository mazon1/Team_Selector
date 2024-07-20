import streamlit as st
import pandas as pd
import os

# Predefined rules for recommending the Delivery Accountability role
def recommend_role(skills):
    roles = {
        "Coding": ["Advanced", "Expert"],
        "Documentation & Research": ["Proficient", "Expert"],
        "Presentation & Communication": ["Proficient", "Expert"]
    }
    
    for role, levels in roles.items():
        if skills.get(role, "") in levels:
            return role
    return "No specific role recommended"

def save_input_to_csv(skills, filename="user_skills.csv"):
    # Check if the file exists
    file_exists = os.path.isfile(filename)
    
    # Create a DataFrame from the skills dictionary
    df = pd.DataFrame([skills])
    
    # Append the data to the CSV file
    df.to_csv(filename, mode='a', index=False, header=not file_exists)

st.title("Team Selection App")

# Input form for user skills
st.sidebar.header("Enter Your Skills")
project_management = st.sidebar.selectbox("Project Management:", ["Novice", "Competent", "Proficient", "Advanced", "Expert"])
public_speaking = st.sidebar.selectbox("Public Speaking:", ["Novice", "Competent", "Proficient", "Advanced", "Expert"])
ppt_story = st.sidebar.selectbox("PPT/Story Development:", ["Novice", "Competent", "Proficient", "Advanced", "Expert"])
database_management = st.sidebar.selectbox("Database Management:", ["Novice", "Competent", "Proficient", "Advanced", "Expert"])
coding = st.sidebar.selectbox("Coding:", ["Novice", "Competent", "Proficient", "Advanced", "Expert"])
deployment = st.sidebar.selectbox("Deployment:", ["Novice", "Competent", "Proficient", "Advanced", "Expert"])
passion = st.sidebar.selectbox("Passion:", ["Project Management", "Coding", "Documentation & Research", "Presentation & Communication"])

skills = {
    "Project Management": project_management,
    "Public Speaking": public_speaking,
    "PPT/Story Development": ppt_story,
    "Database Management": database_management,
    "Coding": coding,
    "Deployment": deployment,
    "Passion": passion
}

# Recommend role based on the entered skills
recommendation = recommend_role(skills)
skills["Recommended Role"] = recommendation

# Save user input to CSV
save_input_to_csv(skills)

st.write(f"### Your Skills:")
for skill, level in skills.items():
    st.write(f"- **{skill}:** {level}")

st.write(f"### Recommended Delivery Accountability role: {recommendation}")
