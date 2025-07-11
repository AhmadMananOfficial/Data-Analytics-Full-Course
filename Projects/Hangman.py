# ======================================================
# 💡 Features:
# 🎶 Background music (looped)
# 🗣️ Voice feedback (emoji-free)
# 🎉 Emojis & fun messages
# 🧠 Smart directory fix
# 🔁 Play again option
# 🧑‍🎨 Cool ASCII hangman
# 🗂️ Word category selection
# 💾 Clean + pro-looking code
# ======================================================

import random
import pyttsx3
import pygame
import os
import time
import sys
import re

# ========== SETUP ==========

os.chdir(os.path.dirname(os.path.abspath(__file__)))

engine = pyttsx3.init()
engine.setProperty('rate', 150)

pygame.mixer.init()
try:
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)
except:
    print("🎵 Background music not found!")

def strip_emojis(text):
    return re.sub(r'[^\w\s.,!?]', '', text)

def speak(text):
    print(f"🗣️ {text}")
    clean = strip_emojis(text)
    engine.say(clean)
    engine.runAndWait()

# ========== ASCII ART ==========

HANGMAN_PICS = [
    """
     +---+
     |   |
         |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
         |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
         |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    /    |
         |
    =======""",
    """
     +---+
     |   |
     O   |
    /|\\  |
    / \\  |
         |
    ======="""
]

# ========== WORD CATEGORIES ==========

CATEGORIES = {
    "animals": ["elephant", "tiger", "rabbit", "giraffe", "penguin"],
    "fruits": ["banana", "apple", "mango", "papaya", "cherry"],
    "countries": ["pakistan", "canada", "brazil", "egypt", "germany"],
    "tech": ["python", "laptop", "keyboard", "server", "internet"]
}

# ========== GAME START ==========

speak("Welcome... to Hangman! 💀")
speak("Guess the word, one letter at a time.")
speak("You have 6 wrong tries before the game ends.")

for i in range(3, 0, -1):
    speak(f"{i}...")
    time.sleep(0.2)
speak("Let’s go! 🎯")

# ========== GAME FUNCTION ==========

def play_game():
    print("\n📁 Categories:", ", ".join(CATEGORIES.keys()))
    while True:
        category = input("🧠 Choose a category: ").lower()
        if category in CATEGORIES:
            break
        speak("Please choose a valid category.")
    
    word = random.choice(CATEGORIES[category])
    guessed = set()
    wrong_guesses = 0
    display = ["_" for _ in word]

    while wrong_guesses < len(HANGMAN_PICS) - 1 and "_" in display:
        print(HANGMAN_PICS[wrong_guesses])
        print("\n🔤 Word:", " ".join(display))
        print(f"❌ Wrong guesses left: {len(HANGMAN_PICS) - 1 - wrong_guesses}")
        guess = input("👉 Your letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            speak("Please enter a single letter.")
            continue

        if guess in guessed:
            speak("You already tried that letter.")
            continue

        guessed.add(guess)

        if guess in word:
            speak("Nice! Letter found. ✅")
            for i, char in enumerate(word):
                if char == guess:
                    display[i] = guess
        else:
            wrong_guesses += 1
            speak("Nope! Wrong guess. ❌")

    print(HANGMAN_PICS[wrong_guesses])

    if "_" not in display:
        speak("🎉 Congratulations! You guessed the word.")
        print("🥳 Word was:", word)
    else:
        speak("💀 Game over. You're out of guesses.")
        print("😭 The word was:", word)

    pygame.mixer.music.fadeout(3000)
    speak("Thanks for playing Hangman with me, legend.")

    again = input("🔁 Play again? (y/n): ").lower()
    if again == "y":
        os.execl(sys.executable, sys.executable, *sys.argv)

# ========== START GAME ==========

play_game()
