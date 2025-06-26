import random
import time
import google.generativeai as genai
from IPython.display import clear_output, display, Markdown

# Initialize Gemini
genai.configure(api_key="AIzaSyCaVdOkYqC2QQe855cljGbsAonqnfKch3Q")  
model = genai.GenerativeModel("gemini-1.5-flash")

# Game elements
suspects = ['Mr. Green', 'Ms. Scarlet', 'Professor Plum', 'Mrs. Peacock']
locations = ['Library', 'Ballroom', 'Kitchen', 'Conservatory']
weapons = ['Candlestick', 'Dagger', 'Revolver', 'Rope']

# Secret answer
culprit = random.choice(suspects)
crime_scene = random.choice(locations)
weapon_used = random.choice(weapons)

# Generate smart AI clue using Gemini
def generate_clue(suspect, location, weapon):
    prompt = (
        f"A crime has been committed in a mansion. The culprit is {suspect}, "
        f"they committed the crime in the {location} with a {weapon}. "
        "Give me 3 creative, mysterious clues that help the player figure out who the culprit is, "
        "without giving away the full answer."
    )
    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        return f"Error generating clue: {str(e)}"

# Intro
def intro():
    clear_output()
    display(Markdown("## 🤖 AI Mystery Game Master with Gemini"))
    print("Solve the mystery by guessing the suspect, location, and weapon!")
    input("\nPress Enter to receive AI-generated clues...")

# Show clues
def give_clues():
    clear_output()
    print("🧠 Gemini is thinking...\n")
    time.sleep(2)
    clues = generate_clue(culprit, crime_scene, weapon_used)
    print("🔎 AI Clues:\n")
    print(clues)

# Take user guess
def get_guess():
    guess_suspect = input("👤 Suspect: ").strip()
    guess_location = input("📍 Location: ").strip()
    guess_weapon = input("🗡️ Weapon: ").strip()
    return guess_suspect, guess_location, guess_weapon

# Check guess
def check_guess(s, l, w):
    return s == culprit and l == crime_scene and w == weapon_used

# Play the game
def play_game():
    intro()
    give_clues()
    attempts = 3
    while attempts > 0:
        print(f"\n💡 Attempts left: {attempts}")
        s, l, w = get_guess()
        if check_guess(s, l, w):
            print(f"\n🎉 Correct! It was {culprit} in the {crime_scene} with the {weapon_used}!")
            return
        else:
            print("❌ Wrong guess. Try again.\n")
            attempts -= 1
    print(f"\n😞 Out of tries! The truth: {culprit} in the {crime_scene} with the {weapon_used}.")

# Start the game
play_game()
