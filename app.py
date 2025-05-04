import streamlit as st

# Set page configuration
st.set_page_config(page_title="Happy Birthday Wisher", page_icon="🎉")

# Title and header
st.title("🎂 Happy Birthday Wisher 🎈")
st.header("Send a Special Birthday Wish!")

# Input for the recipient's name
name = st.text_input("Enter the name of the birthday person:", "")

# Display the birthday message
if name:
    st.markdown(f"## 🎉 Happy Birthday, {name}! 🎉")
    st.write("Wishing you a fantastic year ahead filled with joy, love, and adventure!")
    st.balloons()  # Streamlit's built-in balloons animation
else:
    st.write("Enter a name to see a personalized birthday message!")

# Add some styling with markdown and custom CSS
st.markdown("""
    <style>
    .main {
        background-color: #f0f8ff;
        padding: 20px;
        border-radius: 10px;
    }
    h1 {
        color: #ff4500;
        text-align: center;
    }
    h2 {
        color: #1e90ff;
    }
    </style>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Made with ❤️ using Streamlit")