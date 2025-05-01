# app.py

import streamlit as st
from utils import (
    validate_email,
    validate_phone,
    generate_questions
)


# Initialize session state
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.candidate_info = {}
    st.session_state.tech_stack = []
    st.session_state.questions = []

st.title("🤖 TalentScout Hiring Assistant")

# Step 0: Greeting
if st.session_state.step == 0:
    st.write("Hello and welcome to TalentScout! I'm here to guide you through the initial screening. Type 'exit' anytime to end the chat.")
    if st.button("Start Interview"):
        st.session_state.step = 1

# Step 1: Collect Candidate Info
elif st.session_state.step == 1:
    with st.form("candidate_info"):
        name = st.text_input("Full Name")
        email = st.text_input("Email Address")
        phone = st.text_input("Phone Number")
        experience = st.number_input("Years of Experience", min_value=0, max_value=50, step=1)
        position = st.text_input("Desired Position(s)")
        location = st.text_input("Current Location")
        submitted = st.form_submit_button("Next")

        if submitted:
            if not validate_email(email):
                st.error("Invalid email format.")
            elif not validate_phone(phone):
                st.error("Invalid phone number format.")
            else:
                if 'candidate_info' not in st.session_state:
                    st.session_state.candidate_info = {
                        "name": "",
                        "email": "",
                        "skills": []
                        }
                '''st.session_state.candidate_info = {
                    "name": name,
                    "email": email,
                    "phone": phone,
                    "experience": experience,
                    "position": position,
                    "location": location
                }'''
                st.session_state.step = 2

# Step 2: Collect Tech Stack
elif st.session_state.step == 2:
    tech_stack_input = st.text_input(
        "List the programming languages, frameworks, databases, and tools you're proficient in (comma-separated):"
    )
    if st.button("Generate Questions"):
        if not tech_stack_input.strip():
            st.error("Please enter at least one technology.")
        else:
            st.session_state.tech_stack = [tech.strip() for tech in tech_stack_input.split(",") if tech.strip()]
            st.session_state.questions = generate_questions(st.session_state.tech_stack)
            st.session_state.step = 3

# Step 3: Display Questions
elif st.session_state.step == 3:
    st.subheader("Technical Questions Based on Your Tech Stack")
    for tech, questions in st.session_state.questions.items():
        st.markdown(f"### {tech}")
        for i, q in enumerate(questions, start=1):
            st.markdown(f"**Q{i}:** {q}")

    if st.button("Finish Interview"):
        st.session_state.step = 4

# Step 4: End Conversation
elif st.session_state.step == 4:
    name = st.session_state.candidate_info.get("name", "Candidate")
    st.success(f"Thank you, {name}! Your information has been recorded. Our team will reach out to you soon.")
    st.write("You may now close this window.")
