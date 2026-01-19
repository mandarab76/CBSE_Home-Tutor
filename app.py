import streamlit as st
from modules import mrunal_legacy, gargi_legacy, cbse_standard

# ==========================================
# ⚙️ GLOBAL APP CONFIG
# ==========================================
st.set_page_config(
    page_title="CBSE Tutor Hub",
    page_icon="🎓",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 🔐 SIDEBAR: THE UNIVERSAL LOGIN
# ==========================================
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/9/95/Digital_India_logo.svg/1200px-Digital_India_logo.svg.png", width=100)
st.sidebar.title("Student Login")

# 1. Inputs
first_name = st.sidebar.text_input("First Name:")
last_name = st.sidebar.text_input("Last Name / Father's Name:")
student_grade = st.sidebar.selectbox("Select your Class:", 
                                     ["Class 1", "Class 2", "Class 3", "Class 4", 
                                      "Class 5", "Class 6", "Class 7", "Class 8", 
                                      "Class 9", "Class 10"])

# OPTIONAL: A simple VIP Code to prevent accidental name clashes
# You can tell the girls: "Always put 'VIP' in the code box."
secret_code = st.sidebar.text_input("School/VIP Code (Optional):", type="password")

# 2. Login Button
login_clicked = st.sidebar.button("Enter Classroom 🚀")

# 3. External Resource Links
st.sidebar.markdown("---")
st.sidebar.subheader("📚 Quick Resources")
st.sidebar.markdown("[📖 NCERT eBooks](https://ncert.nic.in/textbook.php)")
st.sidebar.markdown("[🏫 ePathshala](https://epathshala.nic.in/)")
st.sidebar.markdown("[🖥️ Diksha Portal](https://diksha.gov.in/)")

# ==========================================
# 🚦 THE ROUTER LOGIC
# ==========================================
def main():
    # Construct the Full Name ID
    full_name_id = f"{first_name.strip()} {last_name.strip()}".lower()
    
    # A. WELCOME SCREEN (Wait for Login)
    if not login_clicked:
        st.title("🎓 Welcome to CBSE Tutor Hub")
        st.markdown("""
        ### AI-Powered Learning for the Future
        Aligned with **NEP 2020** & **NCF 2023**.
        
        This platform provides:
        * **Standard CBSE Modules:** For all students (Class 1-10).
        * **Personalized Learning:** For registered students.
        
        👈 **Please enter your details in the sidebar to begin.**
        """)
        return

    # B. MRUNAL'S VIP ZONE (Check Name + Code)
    # Checks if name is 'mrunal mandar' AND code is 'VIP' (or whatever you choose)
    if full_name_id == "mrunal mandar" and secret_code == "VIP":
        st.success(f"👋 Welcome back, **Mrunal**! Loading your Term 1 Syllabus...")
        mrunal_legacy.render_zone() 

    # C. GARGI'S VIP ZONE
    elif full_name_id == "gargi mandar" and secret_code == "VIP":
        st.success(f"👋 Welcome back, **Gargi**! Opening Science Lab...")
        gargi_legacy.render_zone() 

    # D. THE GLOBAL STUDENT ZONE (For everyone else)
    else:
        # If they tried to login as Mrunal/Gargi but forgot the password
        if "mrunal" in full_name_id or "gargi" in full_name_id:
             if secret_code != "VIP":
                 st.warning("⚠️ Accessing Standard Dashboard (VIP Code missing).")

        st.title(f"👋 Hi {first_name}!")
        st.write(f"You are in the **{student_grade}** Dashboard.")
        
        # Load the Generic CBSE Module
        # We pass the grade so the module knows which subjects to show
        cbse_standard.render_dashboard(first_name, student_grade)

if __name__ == "__main__":
    main()
