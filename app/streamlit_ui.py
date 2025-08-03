from story_agents import story_ender_agent
import streamlit as st
import textwrap

# --- STREAMLIT UI ---
st.set_page_config(page_title="Story Ender", page_icon="📚", layout="centered")
st.title("📚 Story Ender")
st.subheader("Finish your story with the perfect ending — genre-aware, satisfying, and fun!")
genre_options = {
    "🌀 Totally Twisted Surprise (Absurd Ending)": "twist",
    "🎬 Bollywood Style Masala": "bollywood",
    "🕵️ Mystery / Thriller": "mystery",
    "💘 Romance": "romance",
    "👽 Science Fiction": "science fiction",
    "👻 Horror": "horror",
    "🧙‍♂️ Fantasy": "fantasy",
    "😂 Comedy": "comedy",
}


genre = st.selectbox("Choose your story's genre:", list(genre_options.keys()), index=0)

story = st.text_area("Paste your story setup or fragment below:", height=250)

if st.button("✍️ Generate Ending"):
    if not story.strip():
        st.warning("Please enter a story first.")
    else:
        prompt = textwrap.dedent(f"""
            You're a skilled storyteller. Write ONLY the ending (2–4 vivid paragraphs) of the following story.

            Genre: {genre_options[genre].title()}

            ✦ Do not rewrite or summarize the story.
            ✦ Stick to the genre’s mood, tone, and expectations.
            ✦ Make the ending fun, thrilling, emotional, or deep — depending on the genre.
            ✦ Focus on reader satisfaction and leave a lasting impression.

            Story Setup:
            \"\"\"
            {story}
            \"\"\"

            Now, write the ending.
        """)

        st.info("Generating ending using genre-specialist AI...")
        response = story_ender_agent.run(prompt)

        if response and response.content:
            st.markdown("### 🧠 Generated Ending:")
            st.markdown(response.content.strip())
        else:
            st.error("❌ No response generated. Please try again.")