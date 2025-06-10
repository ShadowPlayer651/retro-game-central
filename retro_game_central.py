import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Retro Game Central", page_icon="🕹️", layout="wide")

st.title("🕹️ Welcome to Retro Game Central")
st.write("Dive into the golden age of gaming — pick an era, find a classic, press start!")

# --- Sample Game Data ---
games = {
    "🟨 8-bit / NES": [
        {"title": "Super Mario Bros.", "desc": "Run, jump, and stomp your way through the Mushroom Kingdom.", "img": "https://upload.wikimedia.org/wikipedia/en/0/03/Super_Mario_Bros._box.png"},
        {"title": "The Legend of Zelda", "desc": "Explore dungeons, collect rupees, save Hyrule.", "img": "https://upload.wikimedia.org/wikipedia/en/0/0c/Zelda_1_box_art.png"}
    ],
    "🟥 16-bit / SNES": [
        {"title": "Chrono Trigger", "desc": "Time-traveling RPG with rich storylines and turn-based battles.", "img": "https://upload.wikimedia.org/wikipedia/en/a/a1/Chrono_Trigger.jpg"},
        {"title": "Mega Man X", "desc": "High-speed action with futuristic robot bosses.", "img": "https://upload.wikimedia.org/wikipedia/en/8/89/Mega_Man_X_Coverart.png"}
    ],
    "💿 DOS / CD-ROM": [
        {"title": "DOOM", "desc": "The FPS that started it all. Rip and tear!", "img": "https://upload.wikimedia.org/wikipedia/en/5/57/Doom_cover_art.jpg"},
        {"title": "Monkey Island 2", "desc": "Point-and-click humor and swashbuckling puzzles.", "img": "https://upload.wikimedia.org/wikipedia/en/0/03/MonkeyIsland2.jpg"}
    ]
}

# --- Sidebar Era Selection ---
era = st.sidebar.selectbox("Choose your era:", list(games.keys()))

# --- Game Cards Display ---
cols = st.columns(2)
for idx, game in enumerate(games[era]):
    with cols[idx % 2]:
        st.image(game["img"], width=200)
        st.subheader(game["title"])
        st.caption(game["desc"])
        st.button(f"🎮 Play {game['title']}", key=game["title"])  # Button placeholder

