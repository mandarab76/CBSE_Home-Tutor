import streamlit as st
import random
import pandas as pd

def render_dashboard(name, grade):
    """
    The Global Dashboard for any CBSE Student (Class 1-10).
    Features:
    1. Subject Selection
    2. The Think Tank (Critical Thinking Generator)
    3. Natural Fact (Nature Connection)
    4. Quick Tools
    """
    
    # --- 1. HEADER & SUBJECTS ---
    st.subheader(f"🏫 Standard Dashboard: {grade}")
    
    # Define subjects based on grade level
    if "Class 1" in grade or "Class 2" in grade or "Class 3" in grade or "Class 4" in grade:
        subjects = ["Mathematics", "English", "Hindi", "EVS"]
    else:
        subjects = ["Mathematics", "Science", "Social Science", "English", "AI & Coding"]

    col1, col2 = st.columns([3, 1])
    
    with col1:
        selected_subject = st.selectbox("📚 Select Subject:", subjects)
        chapter_name = st.text_input(f"Which chapter of {selected_subject} are you studying?", placeholder="e.g., Force, Nouns, Democracy...")

    # --- 2. THE THINK TANK (Global Version) ---
    # Based on Source: Assessment Resources
    st.divider()
    st.markdown("### 🧠 The Think Tank")
    st.info("Use this tool to test your understanding beyond the textbook.")

    if chapter_name:
        if st.button("Generate Critical Thinking Question"):
            # A pool of generic 'Deep Thinking' questions applicable to any topic
            questions = [
                f"How would you explain '{chapter_name}' to a 5-year-old?",
                f"Can you find a connection between '{chapter_name}' and Nature? (Natural Fact)",
                f"Which UN Sustainable Development Goal (SDG) is related to '{chapter_name}'?",
                f"If you could invent a machine using the concept of '{chapter_name}', what would it do?",
                f"Why do you think the government wants students to learn about '{chapter_name}'?",
                f"Draw a mind map of '{chapter_name}' on paper. Done?",
                "What is the 'Tech Funda' (Technical Tip) you would write for this chapter?"
            ]
            
            # Pick a random question
            q = random.choice(questions)
            
            st.markdown(f"**🤔 Your Challenge:**")
            st.success(f"**{q}**")
            
            # Interactive Reflection Box
            st.text_area("Write your thought process here:", height=100)
    else:
        st.caption("👈 Enter a chapter name above to unlock the Think Tank.")

    # --- 3. NATURAL FACT (Nature Connection) ---
    # Based on Source: Assessment Resources
    with st.expander("🌿 Natural Fact of the Day"):
        facts = [
            "Despite living in a digital era, nature is the original engineer.",
            "Did you know? Trees communicate via underground fungal networks (like the Internet!).",
            "Bees use geometry to build honeycombs for maximum storage with minimum wax.",
            "Velcro was invented by observing how burrs stick to dog fur."
        ]
        st.write(random.choice(facts))
        st.caption("Connect what you learn today to the world outside!")

    # --- 4. QUICK UTILITIES ---
    st.divider()
    st.subheader("🚀 Student Toolkit")
    
    u_col1, u_col2, u_col3 = st.columns(3)
    
    with u_col1:
        st.markdown("**📝 To-Do List**")
        st.checkbox("Read NCERT Chapter")
        st.checkbox("Solve 'Exercise' Questions")
        st.checkbox("Try 'Hands-On' Activity")

    with u_col2:
        st.markdown("**🔗 External Links**")
        st.markdown("• [ePathshala (Books)](https://epathshala.nic.in/)")
        st.markdown("• [Diksha (Videos)](https://diksha.gov.in/)")
        st.markdown("• [Swayam (Courses)](https://swayam.gov.in/)")

    with u_col3:
        st.markdown("**🏆 Progress**")
        st.progress(random.randint(30, 90))
        st.caption("Weekly Learning Goal")