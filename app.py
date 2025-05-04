import streamlit as st

# Set page configuration
st.set_page_config(page_title="Happy Birthday Minahil", page_icon="💖")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
        padding: 20px;
        border-radius: 15px;
    }
    h1 {
        color: #ff1493;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    h2 {
        color: #c71585;
        text-align: center;
    }
    .heart {
        color: #ff0000;
        font-size: 24px;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        padding: 10px;
        font-size: 16px;
    }
    </style>
""", unsafe_allow_html=True)

# Title and header
st.title("💖 Happy Birthday, Minahil! 💖")
st.header("To My Amazing Girlfriend 🎉")

# Personalized birthday message
st.markdown(f"""
    ## 🎂 Dearest Minahil, My Love 💞
    Happy Birthday, my sweetheart! Today is all about celebrating you – the most beautiful, kind, and incredible girl in the world. 
    You make every moment brighter, and I'm so lucky to have you as my girlfriend. Here's to a day filled with love, laughter, and all your favorite things!
""")

# Balloons animation
st.balloons()

# Love note section
st.subheader("A Little Love Note for You 💌")
st.write("Minahil, you are my everything. Your smile lights up my world, and your heart is my home. I love you more than words can ever express. Happy Birthday, my forever love! ❤️")

# Special message reveal button
if st.button("Click for a Special Surprise!"):
    st.markdown("""
        ### My Promise to You 🌸
        Minahil, I promise to make this year the best yet – filled with adventures, cozy nights, and endless love. You're my dream come true, and I'll always be by your side. Happy Birthday, my princess! 😘
    """)
    st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", caption="You make my heart skip a beat! 💓")

# Footer
st.markdown("---")
st.write("Made with all my love for you, Minahil ❤️ | Powered by Streamlit")