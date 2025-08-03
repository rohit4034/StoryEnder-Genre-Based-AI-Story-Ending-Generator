from app.story_agents import story_ender_agent
import streamlit as st
import textwrap

def get_user_input():
    genres = {
        "1": "mystery",
        "2": "romance",
        "3": "science fiction",
        "4": "horror"
    }

    print("Welcome to 🧠 StoryEnder!\n")
    print("Choose your story genre:")
    for key, value in genres.items():
        print(f"  {key}. {value.title()}")

    selected = input("\nEnter the number of your genre: ").strip()
    genre = genres.get(selected)
    if not genre:
        print("❌ Invalid selection. Please try again.")
        return get_user_input()
    
    print("\nNow paste your story setup or fragment below (3–10 lines is ideal):\n")
    story = input("Story:\n")
    return genre, story


def generate_ending(genre, story):
    prompt = textwrap.dedent(f"""
        You're a skilled storyteller. Write ONLY the ending (2–4 vivid paragraphs) of the following story.
        
        Genre: {genre.title()}
        
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
    return story_ender_agent.run(prompt)


