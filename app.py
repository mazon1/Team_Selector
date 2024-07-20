import streamlit as st
import pandas as pd

# Function to recommend the role based on user input
def recommend_role(data):
    role_recommendations = {
        "Coding": data.get("Coding", "Novice"),
        "Documentation & Research": data.get("Documentation & Research", "Novice"),
        "Presentation": data.get("PPT/Story Development", "Novice"),
        "Communication": data.get("Public Speaking", "Novice"),
    }

    lead_role = max(role_recommendations, key=role_recommendations.get)
    return lead_role

# Function to save user input to CSV file
def save_input_to_csv(input_data, filename="user_inputs.csv"):
    df = pd.DataFrame([input_data])
    try:
        existing_df = pd.read_csv(filename)
        df = pd.concat([existing_df, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_csv(filename, index=False)

# Streamlit UI
st.title("Team Selection App")
st.image("teamselectorapp.jpg", width=200)

# Input fields
name = st.text_input("Name")
project_management = st.selectbox("Project Management", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"])
public_speaking = st.selectbox("Public Speaking", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"])
ppt_story_dev = st.selectbox("PPT/Story Development", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"])
database_management = st.selectbox("Database Management", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"])
coding = st.selectbox("Coding", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"])
deployment = st.selectbox("Deployment", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"])
passion = st.selectbox("Passion", ["Coding", "Documentation & Research", "Presentation", "Communication"])

# Button to recommend lead role
if st.button("Recommend Lead Role"):
    user_data = {
        "Name": name,
        "Project Management": project_management,
        "Public Speaking": public_speaking,
        "PPT/Story Development": ppt_story_dev,
        "Database Management": database_management,
        "Coding": coding,
        "Deployment": deployment,
        "Passion": passion
    }

    recommended_role = recommend_role(user_data)
    st.markdown(f"### Recommended Role: {recommended_role}")

    # Save user input to CSV
    save_input_to_csv(user_data)

