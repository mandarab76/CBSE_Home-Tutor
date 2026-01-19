import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def render_zone():
    """
    VIP Zone for Gargi (Class 8).
    Includes:
    1. SDG Activity: Zero Hunger
    2. Simulation: Crop Production (Flood vs Drip)
    3. The Think Tank (Critical Thinking)
    """
    st.header("👩‍🎓 Gargi's Science Lab")
    st.info("Module: Crop Production & Management | Aligned with NCF 2023")

    st.write("### 🌾 Mission: Zero Hunger (SDG 2)")
    st.markdown("Compare **Traditional Irrigation** vs. **Modern Methods**.")
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown("**⚙️ Simulation Controls**")
        water_level = st.slider("Select Irrigation Water Level (Liters/Hectare)", 
                              min_value=1000, max_value=10000, step=500, value=5000)
        
        st.metric(label="Selected Water Usage", value=f"{water_level} L")

    with col2:
        # Dynamic Feedback Logic
        if water_level > 7000:
            st.warning("⚠️ High Water Usage! This mimics Flood Irrigation.")
            yield_percent = 80
            method_name = "Flood Irrigation"
        elif water_level < 3000:
            st.error("⚠️ Too Dry! Crops are stressed.")
            yield_percent = 40
            method_name = "Drought Conditions"
        else:
            st.success("✅ Optimal Range (Drip/Sprinkler).")
            yield_percent = 95
            method_name = "Drip Irrigation"

        # Simple Bar Chart for Analysis
        chart_data = pd.DataFrame({
            'Method': [method_name, 'Ideal Target'],
            'Yield Efficiency %': [yield_percent, 100]
        })
        st.bar_chart(chart_data, x='Method', y='Yield Efficiency %')

    # --- THE THINK TANK (Critical Thinking) ---
    st.divider()
    [span_1](start_span)with st.expander("🧠 Enter The Think Tank[span_1](end_span)"):
        st.markdown("### Challenge Question")
        st.write("**Why is Drip Irrigation preferred for Sandy Soil specifically?**")
        st.write("*(Hint: Think about water retention capacity)*")
        
        student_hypothesis = st.text_area("Write your hypothesis:", height=100)
        
        if st.button("Submit to Tutor Bot"):
            if "drain" in student_hypothesis.lower() or "hold" in student_hypothesis.lower() or "absorb" in student_hypothesis.lower():
                 st.success("🌟 Excellent critical thinking! Sandy soil drains water too fast, so dripping it slowly allows roots to catch it.")
            else:
                 st.info("Good attempt! Consider this: Sandy soil has large particles, so water runs through it quickly (like a sieve). Drip irrigation solves this by adding water drop-by-drop.")

    # --- TECH FUNDA TIP ---
    st.info("💡 **Tech Funda:** Modern Drip systems use IoT sensors to detect soil moisture automatically!")