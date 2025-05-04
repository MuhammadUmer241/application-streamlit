import streamlit as st
import random

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
        cursor: pointer;
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
    .quote-box {
        background-color: #ffe4e1;
        padding: 15px;
        border-radius: 10px;
        margin-top: 10px;
        text-align: center;
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
        particleCount: 150,
        spread: 80,
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

# Interactive heart animation
st.subheader("Tap the Heart for Love! 💓")
if st.button("💖 Click Me!", key="heart_button"):
    st.markdown("<p class='heart'>💕 Love you forever, Minahil! 💕</p>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/LpJTL7X2T3nYk/giphy.gif", caption="My heart beats for you! 😘")

# Special message reveal button
st.subheader("A Surprise Just for You! 🌸")
if st.button("Click for a Special Surprise!"):
    st.markdown("""
        ### My Promise to You 🌸
        Minahil, I promise to make this year the best yet – filled with adventures, cozy nights, and endless love. You're my dream come true, and I'll always be by your side. Happy Birthday, my princess! 😘
        Maybe I am busy in my job and all other things. But you mean a lot to me. You are my love, my sweetheart!
    """)
    st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", caption="You make my heart skip a beat! 💓")

# Romantic Quote Generator
st.subheader("A Sweet Quote for You 💬")
quotes = [
    "Minahil, you're the melody to my heart's song. Happy Birthday, my love! 🎶",
    "Every day with you feels like a gift, Minahil. Here's to your special day! 🎉",
    "My love for you grows stronger every moment, Minahil. Happy Birthday! 💞",
    "You're my forever and always, Minahil. Have the best birthday ever! 🌟",
    "Minahil, you're my sunshine on every cloudy day. Happy Birthday, sweetheart! ☀️"
]
if st.button("Get a Romantic Quote!"):
    quote = random.choice(quotes)
    st.markdown(f"<div class='quote-box'>💕 {quote}</div>", unsafe_allow_html=True)

# Gift Reveal Section
st.subheader("A Gift for My Princess 🎁")
gifts = [
    "A personalized love letter book with our story 💌",
    "A romantic dinner date under the stars 🌟",
    "A custom necklace with our initials 💞",
    "A weekend getaway to a cozy cabin 🏡",
    "A spa day to pamper my queen 💆‍♀️"
]
if st.button("Reveal a Special Gift!"):
    gift = random.choice(gifts)
    st.markdown(f"<div class='gift-item'>🎀 {gift}</div>", unsafe_allow_html=True)
    st.write("I can't wait to spoil you, Minahil! 😍")

# Romantic Playlist
st.subheader("Your Birthday Playlist 🎶")
st.write("Enjoy these romantic tunes curated just for you, Minahil!")
st.markdown("""
    <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PL55713C70BA91BD6F" 
    title="Romantic Playlist" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.write("Made with all my love for you, Minahil ❤️ | Powered by Streamlit")