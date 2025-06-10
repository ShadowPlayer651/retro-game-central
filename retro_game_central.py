import streamlit as st
import webbrowser

# --- Page Setup ---
st.set_page_config(page_title="Retro Game Central", page_icon="🕹️", layout="wide")

st.title("🕹️ Retro Game Central")
st.write("Explore classic games. Press play. Relive the nostalgia!")

# --- Sample Game Data with working links ---
games = {
    "🟨 8-bit / NES": [
        {
            "title": "Super Mario Bros.",
            "desc": "Classic side-scrolling platformer by Nintendo.",
            "img": "https://upload.wikimedia.org/wikipedia/en/0/03/Super_Mario_Bros._box.png",
            "link": "https://www.retrogames.cc/nes-games/super-mario-bros.html"
        },
        {
            "title": "The Legend of Zelda",
            "desc": "Adventure through Hyrule to rescue Princess Zelda.",
            "img": "https://upload.wikimedia.org/wikipedia/en/0/0c/Zelda_1_box_art.png",
            "link": "https://www.retrogames.cc/nes-games/legend-of-zelda-the.html"
        }
    ],
    "🟥 16-bit / SNES": [
        {
            "title": "Chrono Trigger",
            "desc": "Time-traveling RPG with epic storytelling.",
            "img": "https://upload.wikimedia.org/wikipedia/en/a/a1/Chrono_Trigger.jpg",
            "link": "https://www.youtube.com/watch?v=YBb5NmoaDqA"  # YouTube longplay
        },
        {
            "title": "Mega Man X",
            "desc": "Battle robot bosses in futuristic action.",
            "img": "https://upload.wikimedia.org/wikipedia/en/8/89/Mega_Man_X_Coverart.png",
            "link": "https://www.retrogames.cc/snes-games/mega-man-x.html"
        }
    ]
}

# --- Sidebar Selection ---
era = st.sidebar.selectbox("Choose your era:", list(games.keys()))

# --- Display Games ---
cols = st.columns(2)
for idx, game in enumerate(games[era]):
    with cols[idx % 2]:
        st.image(game["img"], width=200)
        st.subheader(game["title"])
        st.caption(game["desc"])
        if st.button(f"🎮 Play {game['title']}", key=game["title"]):
            st.markdown(f"Launching **{game['title']}**...")
            st.markdown(f"[Click here if it didn't open automatically]({game['link']})")
            webbrowser.open_new_tab(game["link"])
