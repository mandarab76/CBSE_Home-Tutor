import streamlit as st
import matplotlib.pyplot as plt

def render_zone():
    """
    VIP Zone for Mrunal (Class 4).
    Includes:
    1. The Pizza Party (Fractions)
    2. English Syllabus (The Turkish Cap)
    3. Hindi Syllabus (Naya Ujiyara)
    """
    st.header("🧒 Mrunal's VIP Learning World")
    st.info("Status: Term 1 Syllabus Active | Level: Class 4")

    # TAB SELECTION
    tab1, tab2, tab3 = st.tabs(["🍕 Math: Fractions", "📚 English: Turkish Cap", "🇮🇳 Hindi: Naya Ujiyara"])

    # --- TAB 1: THE PIZZA PARTY (Math) ---
    with tab1:
        st.subheader("The Fraction Pizza Party")
        st.write("Mrunal, let's learn fractions by sharing a pizza!")
        
        friends = st.number_input("How many friends are eating? (Type a number like 2, 4, 8)", min_value=1, max_value=12, value=4)
        
        if friends > 0:
            st.write(f"You need to cut the pizza into **{friends}** equal slices.")
            st.write(f"Each person gets **1/{friends}** of the pizza.")
            
            # Matplotlib Pie Chart
            labels = [f'Slice {i+1}' for i in range(friends)]
            sizes = [1/friends] * friends
            
            fig, ax = plt.subplots(figsize=(3, 3))
            ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=90, colors=plt.cm.Pastel1.colors)
            st.pyplot(fig)

    # --- TAB 2: ENGLISH (Syllabus: The Turkish Cap) ---
    with tab2:
        st.subheader("Chapter: The Turkish Cap")
        [span_0](start_span)st.write("Let's practice **Collective Nouns**[span_0](end_span)!")
        
        col1, col2 = st.columns(2)
        with col1:
            st.image("https://img.icons8.com/color/96/group.png", caption="A Group of...")
        
        with col2:
            answer = st.radio("What do we call a group of Soldiers?", 
                            ["A Bunch", "A Regiment", "A School"])
            
            if st.button("Check English Answer"):
                if answer == "A Regiment":
                    st.success("✅ Correct! A Regiment of Soldiers.")
                    st.balloons()
                else:
                    st.error("Oops! Try again.")

    # --- TAB 3: HINDI (Syllabus: Naya Ujiyara) ---
    with tab3:
        st.subheader("कविता: नया उजियारा (Naya Ujiyara)")
        st.write("Match the word to its meaning:")
        
        word_choice = st.selectbox("Choose a word:", ["Ujiyara (उजियारा)", "Mati (माटी)"])
        
        if word_choice == "Ujiyara (उजियारा)":
            user_meaning = st.text_input("Type the meaning in English:")
            if "light" in user_meaning.lower() or "bright" in user_meaning.lower():
                st.success("✨ Sahi Jawab! (Correct)")
            elif user_meaning:
                st.warning("Hint: It comes from the Sun.")