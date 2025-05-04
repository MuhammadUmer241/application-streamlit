import streamlit as st

# Set page configuration
st.set_page_config(page_title="Happy Birthday Minahil", page_icon="💖")

# Custom CSS for styling
st.markdown("""
    <style>
    .main {
        background-color: #fff0f5;
        padding: 25px;
        border-radius: 15px;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
    }
    h1 {
        color: #ff1493;
        text-align: center;
        font-family: 'Georgia', serif;
    }
    h2, h3 {
        color: #c71585;
        text-align: center;
        font-family: 'Arial', sans-serif;
    }
    .heart {
        color: #ff0000;
        font-size: 24px;
    }
    .stButton>button {
        background-color: #ff69b4;
        color: white;
        border-radius: 10px;
        padding: 12px;
        font-size: 16px;
        transition: background-color 0.3s;
    }
    .stButton>button:hover {
        background-color: #ff3e8d;
    }
    .memory-box {
        background-color: #ffe4e1;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
    }
    .gift-item {
        padding: 10px;
        background-color: #f8f1f1;
        border-radius: 8px;
        margin: 5px 0;
        text-align: center;
    }
    </style>
""", unsafe_allow_html=True)

# Add confetti animation using canvas-confetti
st.markdown("""
    <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
    <script>
    confetti({
        particleCount: 100,
        spread: 70,
        origin: { y: 0.6 }
    });
    </script>
""", unsafe_allow_html=True)

# Title and header
st.title("💖 Happy Birthday, Minahil! 💖")
st.header("To My Amazing Girlfriend 🎉")

# Personalized birthday message
st.markdown("""
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
        Maybe I am busy in my job and all other things. But you mean a lot to me. You are my love, my sweetheart!
    """)
    st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", caption="You make my heart skip a beat! 💓")

# Favorite Memories Section
st.subheader("Our Favorite Memories Together 📸")
memory = st.text_area("Share a special memory with Minahil:", height=100)
if memory:
    st.markdown(f"<div class='memory-box'>💕 **Our Special Memory**: {memory}</div>", unsafe_allow_html=True)
    st.write("Let's make more unforgettable moments, my love!")

# Gift Ideas Carousel
st.subheader("Gift Ideas for My Princess 🎁")
gift_ideas = [
    "A personalized love letter book with our story 💌",
    "A romantic dinner date under the stars 🌟",
    "A custom necklace with our initials 💞",
    "A weekend getaway to a cozy cabin 🏡",
    "A spa day to pamper my queen 💆‍♀️"
]
selected_gift = st.selectbox("Pick a gift idea for Minahil:", gift_ideas)
st.markdown(f"<div class='gift-item'>🎀 {selected_gift}</div>", unsafe_allow_html=True)

# Romantic Playlist
st.subheader("A Playlist for Your Special Day 🎶")
st.write("Enjoy these romantic tunes curated just for you, Minahil!")
st.markdown("""
    <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PL55713C70BA91BD6F" 
    title="Romantic Playlist" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Made with all my love for you, Minahil ❤️ | Powered by Streamlit")