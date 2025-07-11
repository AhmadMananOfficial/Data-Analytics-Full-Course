"""
🎮 Rock, Paper, Scissors — Showdown Edition
By Ahmad Manan Akram

💡 Features:
🎉 Fun emojis and smart messages
🗣️ Voice announcements
🧠 User vs Computer logic
🎯 Best of 3 match system
"""

import random
import pyttsx3
import time
import pygame

# Initialize voice engine
engine = pyttsx3.init()
engine.setProperty('rate', 150)

pygame.mixer.init()
pygame.mixer.music.load("music.mp3")
pygame.mixer.music.play(-1)


def speak(text):
    #print(f"🗣️ {text}")
    engine.say(text)
    engine.runAndWait()


print("\n========== Welcome to Rock, Paper, Scissors — Showdown Edition! ==========")
speak("Welcome to Rock Paper Scissors — Showdown Edition!")

# Choices
choices = ['rock', 'paper', 'scissors']
emojis = {
    'rock': '🪨',
    'paper': '📄',
    'scissors': '✂️'
}

user_score = 0
comp_score = 0
rounds = 3

# Game loop
for round in range(1, rounds + 1):
    print(f"\n📣 Round {round} — Fight!")
    speak(f"Round {round}. Choose your move.")
    
    user = input("🤔 Type Rock, Paper, or Scissors: ").lower().strip()
    while user not in choices:
        print("❌ Invalid choice. Try again.")
        user = input("🤔 Rock, Paper, or Scissors: ").lower().strip()

    comp = random.choice(choices)
    print(f"\n👤 You: {user.capitalize()} {emojis[user]}  | 💻 Computer: {comp.capitalize()} {emojis[comp]}")
    #print(f"💻 Computer: {comp.capitalize()} {emojis[comp]}")

    # Decide winner
    if user == comp:
        print("⚖️ It's a tie!")
        speak("It's a tie!")
    elif (user == 'rock' and comp == 'scissors') or \
         (user == 'paper' and comp == 'rock') or \
         (user == 'scissors' and comp == 'paper'):
        print("✅ You win this round!")
        speak("You win this round!")
        user_score += 1
    else:
        print("❌ Computer wins this round.")
        speak("Computer wins this round.")
        comp_score += 1

    print(f"📊 Score — You: {user_score} | Computer: {comp_score}")
    speak(f"You: {user_score} | Computer {comp_score}")
    speak(f"")

# Final Result
print("\n🏁 Game Over!")
if user_score > comp_score:
    print("🎉 YOU WON THE MATCH!")
    speak("Congratulations! You won the match.")
elif comp_score > user_score:
    print("💀 COMPUTER WINS THE MATCH.")
    speak("Game over! Computer wins the match.")
else:
    print("🤝 IT'S A DRAW!")
    speak("The game ends in a draw.")

print("Thanks for playing! 🙌")
