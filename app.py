import streamlit as st

st.set_page_config(page_title="AgriSmartIncome", page_icon="🌾")

st.title("🌾 AgriSmartIncome")
st.subheader("Grow Smart. Earn More.")

st.write("This is an AI-powered farming assistant to help farmers:")
st.markdown("""
- 📈 Choose crops with higher **market demand**  
- 🌦 Get **weather insights** for better planning  
- 🦠 Detect **crop diseases** instantly  
- 💧 Get **soil & irrigation advisory**  
""")

crop = st.text_input("Enter your crop name:")
if st.button("Check Market Trend"):
    st.success(f"✅ {crop} is currently in high demand! (sample data)")
