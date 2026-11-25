import streamlit as st

st.set_page_config(page_title="Levigate Alloys", page_icon="🏭")

st.title("🏭 Levigate Alloys")
st.write("Welcome to Levigate Alloys!")

st.header("About Us")
st.write("We build smart and simple technology solutions.")

name = st.text_input("Ungal peru enna?")
if name:
    st.success(f"Vanakkam {name}! Levigate Alloys ku welcome!")

st.header("Our Services")
st.write("✅ Web Development")
st.write("✅ App Development")
st.write("✅ AI Solutions")

if st.button("Contact Us"):
    st.balloons()
    st.write("Thank you! We will contact you soon.")
