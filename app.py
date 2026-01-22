import Streamlit as st
st.title("LoginSystem")
name  = st.text_input("Enter name:")
if st.button("Check"):
 if name strip() == "":
  st.warniong("Please enter text.")
 elif not name is apha():
  st.warning("Warning!")
else st.success("The text is corect!")
