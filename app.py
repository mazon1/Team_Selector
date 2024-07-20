import streamlit as st
import pandas as pd

# Function to recommend a role based on skill levels
def recommend_role(skills):
    roles = {
        "Coding": ["Advanced", "Expert"],
        "Documentation & Research": ["Proficient", "Expert"],
        "Presentation & Communication": ["Proficient", "Expert"]
    }
    
    for role, levels in roles.items():
        if skills.get(role, "") in levels:
            return role
    
    # If no exact match is found, determine the closest match
    closest_role = None
    highest_level = 0
    
    levels_map = {"Novice": 1, "Advanced Beginner": 2, "Competent": 3, "Proficient": 4, "Expert": 5}
    
    for role, levels in roles.items():
        user_level = levels_map.get(skills.get(role, ""), 0)
        if user_level > highest_level:
            highest_level = user_level
            closest_role = role
    
    return skills.get("Passion", "Coding")  # Default to "Passion" if no roles match

# Initialize the Streamlit app
st.title("Team Role Recommendation App")

# Create input fields for the user to enter their skill levels
user_data = {
    "Name": st.text_input("Enter your name:"),
    "Project Management": st.selectbox("Project Management skill level:", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"]),
    "Public Speaking": st.selectbox("Public Speaking skill level:", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"]),
    "PPT/Story Development": st.selectbox("PPT/Story Development skill level:", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"]),
    "Database Management": st.selectbox("Database Management skill level:", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"]),
    "Coding": st.selectbox("Coding skill level:", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"]),
    "Deployment": st.selectbox("Deployment skill level:", ["Novice", "Advanced Beginner", "Competent", "Proficient", "Expert"]),
    "Passion": st.text_input("What are you passionate about?")
}

# Recommend a role based on the entered skill levels
recommended_role = recommend_role(user_data)
st.write(f"Recommended Role for Delivery Accountability: {recommended_role}")

# Save user input and recommendation to a CSV file
if st.button("Save"):
    df = pd.DataFrame([user_data])
    df["Recommended Role"] = recommended_role
    df.to_csv("user_data.csv", mode="a", header=False, index=False)
    st.success("Data saved successfully!")
