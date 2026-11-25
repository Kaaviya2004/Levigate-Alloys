import streamlit as st

st.set_page_config(page_title="Unicorn Technology", page_icon="🦄")

st.title("🦄 Unicorn Technology")
st.write("Welcome to Unicorn Technology!")

st.header("About Us")
st.write("We build smart and simple technology solutions.")

name = st.text_input("Ungal peru enna?")
if name:
    st.success(f"Vanakkam {name}! Unicorn Technology ku welcome!")

st.header("Our Services")
st.write("✅ Web Development")
st.write("✅ App Development")
st.write("✅ AI Solutions")

if st.button("Contact Us"):
    st.balloons()
    st.write("Thank you! We will contact you soon.")
