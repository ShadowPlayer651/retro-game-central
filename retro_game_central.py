import streamlit as st

# --- Page Setup ---
st.set_page_config(page_title="Retro Game Central", page_icon="🕹️", layout="wide")

st.title("🕹️ Retro Game Central")
st.write("Explore classic games. Pick your era. Press play!")

# --- Sample Game Data with working links ---
games = {
    "🟨 8-bit / NES": [
        {
            "title": "Super Mario Bros.",
            "desc": "Classic platformer adventure through the Mushroom Kingdom.",
            "img": "https://upload.wikimedia.org/wikipedia/en/0/03/Super_Mario_Bros._box.png",
            "link": "https://www.retrogames.cc/nes-games/super-mario-bros.html"
        },
        {
            "title": "The Legend of Zelda",
            "desc": "Epic quest to save Hyrule in the original action-RPG.",
            "img": "https://upload.wikimedia.org/wikipedia/en/0/0c/Zelda_1_box_art.png",
            "link": "https://www.retrogames.cc/nes-games/legend-of-zelda-the.html"
        }
    ],
    "🟥 16-bit / SNES": [
        {
            "title": "Chrono Trigger",
            "desc": "Legendary RPG with time travel, teamwork, and destiny.",
            "img": "https://upload.wikimedia.org/wikipedia/en/a/a1/Chrono_Trigger.jpg",
            "link": "https://www.youtube.com/watch?v=YBb5NmoaDqA"
        },
        {
            "title": "Mega Man X",
            "desc": "Futuristic side-scroller packed with fast action and robot bosses.",
            "img": "https://upload.wikimedia.org/wikipedia/en/8/89/Mega_Man_X_Coverart.png",
            "link": "https://www.retrogames.cc/snes-games/mega-man-x.html"
        }
    ]
}

# --- Sidebar Era Selection ---
era = st.sidebar.selectbox("Choose your era:", list(games.keys()))

# --- Game Display ---
cols = st.columns(2)
for idx, game in enumerate(games[era]):
    with cols[idx % 2]:
        st.image(game["img"], width=200)
        st.subheader(game["title"])
        st.caption(game["desc"])
        if st.button(f"🎮 Launch {game['title']}", key=game["title"]):
            st.success(f"{game['title']} is ready!")
            st.markdown(f"[▶️ Click here to play]({game['link']})", unsafe_allow_html=True)
