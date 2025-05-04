import streamlit as st
import random

# Set page configuration
st.set_page_config(page_title="Happy Birthday Minahil", page_icon="💝", layout="wide")

# Custom CSS for a vibrant, romantic design
st.markdown("""
    <style>
    .main {
        background: linear-gradient(180deg, #ffccd5, #ffb3e6, #ccffcc);
        padding: 40px;
        border-radius: 25px;
        box-shadow: 0 8px 16px rgba(0, 0, 0, 0.2);
        animation: fadeIn 1.5s ease-in-out;
    }
    h1 {
        color: #ff3399;
        text-align: center;
        font-family: 'Brush Script MT', cursive;
        font-size: 48px;
        text-shadow: 3px 3px #ff99cc;
        animation: glow 2s infinite;
    }
    h2 {
        color: #ff0066;
        text-align: center;
        font-family: 'Verdana', sans-serif;
        font-size: 28px;
    }
    .stButton>button {
        background: linear-gradient(to right, #ff3399, #ff66cc);
        color: white;
        border: none;
        border-radius: 20px;
        padding: 15px 30px;
        font-size: 20px;
        font-family: 'Verdana', sans-serif;
        transition: transform 0.3s, box-shadow 0.3s;
        margin: 15px;
        box-shadow: 0 4px 10px rgba(0, 0, 0, 0.3);
    }
    .stButton>button:hover {
        transform: scale(1.15);
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.4);
    }
    .heart {
        color: #ff1a1a;
        font-size: 35px;
        animation: heartbeat 1.5s infinite;
    }
    .surprise-box {
        background: #fff0f5;
        padding: 25px;
        border-radius: 20px;
        margin: 20px 0;
        text-align: center;
        font-size: 20px;
        color: #333;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.2);
        animation: slideIn 0.5s ease-in;
    }
    .gallery-img {
        border-radius: 20px;
        box-shadow: 0 6px 12px rgba(0, 0, 0, 0.3);
        transition: transform 0.4s;
        max-width: 80%;
        margin: 0 auto;
    }
    .gallery-img:hover {
        transform: scale(1.1);
    }
    .spin-heart {
        font-size: 50px;
        animation: spin 2s linear infinite;
    }
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    @keyframes glow {
        0% { text-shadow: 3px 3px #ff99cc; }
        50% { text-shadow: 3px 3px #ff4da6; }
        100% { text-shadow: 3px 3px #ff99cc; }
    }
    @keyframes heartbeat {
        0% { transform: scale(1); }
        50% { transform: scale(1.3); }
        100% { transform: scale(1); }
    }
    @keyframes slideIn {
        from { transform: translateY(20px); opacity: 0; }
        to { transform: translateY(0); opacity: 1; }
    }
    @keyframes spin {
        from { transform: rotate(0deg); }
        to { transform: rotate(360deg); }
    }
    </style>
""", unsafe_allow_html=True)

# Function to trigger confetti
def trigger_confetti():
    st.markdown("""
        <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.5.1/dist/confetti.browser.min.js"></script>
        <script>
        confetti({
            particleCount: 150,
            spread: 80,
            origin: { y: 0.6 },
            colors: ['#ff3399', '#ff66cc', '#ff99cc']
        });
        </script>
    """, unsafe_allow_html=True)

# Title and header
st.title("🎂 Happy Birthday, Minahil! 🎂")
st.header("My Princess, My Heart 💝")

# Personalized birthday message
st.markdown("""
    ### 💖 My Sweetest Minahil 💞
    hAPPY Birthday, my darling! You're the sparkle in my eyes and the beat in my heart. Today is YOUR day, filled with love, surprises, and all the joy you deserve! 
    I’m so grateful to have you as my girlfriend. Let’s make this birthday magical! 😘
""")
st.balloons()

# Love note
st.subheader("A Kiss from My Heart 💋")
st.write("Minahil, you’re my dream girl. Your smile makes my world brighter, and your love makes every day perfect. Happy Birthday, my one and only! 💕")

# Interactive heart animation
st.subheader("Catch My Love! 💓")
if st.button("💝 Send a Heart!", key="heart_button"):
    trigger_confetti()
    st.markdown("<p class='heart'>💖 I’m crazy about you, Minahil! 😍</p>", unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/l0MYt5jPRbr0acqFI/giphy.gif", caption="My love for you is endless! 💋")

# Surprise Quote Pop-up
st.subheader("A Love Note for You 💬")
quotes = [
    "Minahil, you’re my heart’s home. Happy Birthday, my love! 🏡",
    "Every moment with you is a treasure, Minahil. Shine today! ✨",
    "My heart sings for you, Minahil. Happy Birthday, my angel! 🎶",
    "You’re my forever, Minahil. Have the sweetest birthday! 💖",
    "Minahil, you light up my life. Happy Birthday, my star! 🌟"
]
if st.button("Pop a Love Quote!", key="quote_button"):
    trigger_confetti()
    quote = random.choice(quotes)
    st.markdown(f"<div class='surprise-box'>💞 {quote}</div>", unsafe_allow_html=True)

# Surprise Gift Pop-up
st.subheader("Your Birthday Surprise! 🎁")
gifts = [
    "A scrapbook of our love story 💌",
    "A moonlit dinner just for us 🌙",
    "A locket with our picture inside 💞",
    "A weekend escape to a dreamy spot 🏖️",
    "A day of pampering for my queen 💅"
]
if st.button("Unwrap a Gift!", key="gift_button"):
    trigger_confetti()
    gift = random.choice(gifts)
    st.markdown(f"<div class='surprise-box'>🎀 {gift}</div>", unsafe_allow_html=True)
    st.write("For you, my love, anything! 😍")

# Interactive Picture Gallery
st.subheader("Our Love in Pictures 📷")
st.write("Slide through our moments, Minahil! 💕")
images = [
    {"url": "https://images.unsplash.com/photo-1507525428034-b723cf961d3e?q=80&w=2070", "caption": "Our love is as vast as the sea! 🌊"},
    {"url": "https://images.unsplash.com/photo-1516727003471-7ab364f7b474?q=80&w=2070", "caption": "You make my heart bloom! 🌸"},
    {"url": "https://images.unsplash.com/photo-1538947151057-d9f0b7044da3?q=80&w=2070", "caption": "Under the stars with you! 🌟"}
]
if 'gallery_index' not in st.session_state:
    st.session_state.gallery_index = 0
slider = st.slider("Slide to see our memories!", 0, len(images)-1, st.session_state.gallery_index, key="gallery_slider")
st.session_state.gallery_index = slider
current_image = images[st.session_state.gallery_index]
st.image(current_image["url"], caption=current_image["caption"], use_column_width=True)
col1, col2, col3 = st.columns([1, 2, 1])
with col1:
    if st.button("⬅️ Back", key="gallery_back"):
        trigger_confetti()
        st.session_state.gallery_index = (st.session_state.gallery_index - 1) % len(images)
with col3:
    if st.button("Next ➡️", key="gallery_next"):
        trigger_confetti()
        st.session_state.gallery_index = (st.session_state.gallery_index + 1) % len(images)

# Spin the Heart Game
st.subheader("Spin the Heart! 💖")
if st.button("Spin for a Surprise!", key="spin_button"):
    trigger_confetti()
    surprises = [
        "A big hug from me! 🤗",
        "A sweet kiss for you! 😘",
        "A dance under the stars! 💃",
        "A love poem just for you! 📜",
        "A day full of cuddles! 🥰"
    ]
    surprise = random.choice(surprises)
    st.markdown(f"<div class='surprise-box'><p class='spin-heart'>💖</p> {surprise}</div>", unsafe_allow_html=True)

# Special Message
st.subheader("My Vow to You 🌺")
if st.button("Hear My Heart!", key="vow_button"):
    trigger_confetti()
    st.markdown("""
        <div class='surprise-box'>
        Minahil, my sweetheart, I promise to love you fiercely, cherish every moment with you, and make every day special. 
        Work may keep me busy, but you’re my heart’s home – my love, my everything. Happy Birthday, my princess! 💝
        </div>
    """, unsafe_allow_html=True)
    st.image("https://media.giphy.com/media/3o7btPCcdNniyf0ArS/giphy.gif", caption="Forever yours, Minahil! 💓")

# Romantic Playlist
st.subheader("Dance to Our Love 🎵")
st.write("These songs are for you, my Minahil! 💃")
st.markdown("""
    <iframe width="100%" height="315" src="https://www.youtube.com/embed/videoseries?list=PL55713C70BA91BD6F" 
    title="Romantic Playlist" frameborder="0" allow="autoplay; encrypted-media" allowfullscreen></iframe>
""", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<p style='text-align: center; font-size: 18px;'>Made with endless love for you, Minahil 💝 | Powered by Streamlit</p>", unsafe_allow_html=True)