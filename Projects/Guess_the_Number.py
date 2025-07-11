# ======================================================
# 💡 Features:
# 🎶 Background music (looped)
# 🗣️ Voice feedback (emoji-free)
# 🎉 Emojis & fun messages (for terminal only)
# 🧠 Smart directory fix
# 🔁 Play again option
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

# Auto switch to current script folder
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Text-to-speech engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)  # Speed of voice

# Music setup
pygame.mixer.init()
try:
    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(-1)  # Loop music
except:
    print("🎵 Background music not found!")

# Remove emojis from spoken text
def strip_emojis(text):
    return re.sub(r'[^\w\s.,!?]', '', text)

def speak(text):
    print(f"🗣️ {text}")
    clean_text = strip_emojis(text)
    engine.say(clean_text)
    engine.runAndWait()

# ========== GAME START ==========

speak("Welcome... to The Hidden Number 🎮.")
speak("A mysterious number hides between 1 and 100.")
speak("Your mission... is to find it.")

# Fast countdown
for i in range(3, 0, -1):
    speak(f"{i}...")
    time.sleep(0.4)
speak("Go! 💥")

# ========== GAME LOOP ==========

def play_game():
    secret_number = random.randint(1, 100)
    guess_count = 0

    while True:
        try:
            guess = int(input("👉 Your guess: "))
            guess_count += 1

            if guess < secret_number:
                speak("Too low, try again.")
            elif guess > secret_number:
                speak("Too high, try again.")
            else:
                speak(f"Boom! 🎉 You got it in {guess_count} tries!")
                print("🥳 You did it! You're a guessing legend!")
                break

            # Close guess feedback
            diff = abs(secret_number - guess)
            if diff <= 5:
                speak("🔥 You're super close!")
            elif diff <= 10:
                speak("🌡️ Getting warmer...")

        except ValueError:
            speak("Please enter a valid number.")

    # Game end message
    print("\n👑 GAME OVER 👑")
    speak("Thanks for playing, legend. Made with Python magic by Ahmad!")

    # Optional: fade out music
    pygame.mixer.music.fadeout(3000)

    # Play again?
    play_again = input("🔁 Play again? (y/n): ").lower()
    if play_again == 'y':
        os.execl(sys.executable, sys.executable, *sys.argv)

# Start the game
play_game()
