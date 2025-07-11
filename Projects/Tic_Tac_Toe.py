# ======================================================
# 💡 Features:
# 🎶 Background music (looped)
# 🗣️ Voice feedback (emoji-free)
# 🎮 Play vs Player or Smart AI (Minimax)
# 🌈 Colorful terminal using colorama
# ======================================================

import os
import pygame
import pyttsx3
import time
import sys
import re
from colorama import init, Fore, Style
init(autoreset=True)

# ========== SETUP ==========

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
    print(Fore.YELLOW + f"🗣️ {text}")
    clean = strip_emojis(text)
    engine.say(clean)
    engine.runAndWait()

# ========== BOARD FUNCTIONS ==========

def print_board(board):
    create_map = {
        "X": Fore.RED + "X" + Style.RESET_ALL,
        "O": Fore.BLUE + "O" + Style.RESET_ALL,
        " ": " "
    }

    print() # Add spacing before board to just crating a clan look
    for i, row in enumerate(board):
        row_str = " | ".join(create_map[cell] for cell in row)
        print(row_str)
        if i < 2:
            print("--+---+--")
    print()

def check_win(board, player):
    win_conditions = [
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

def board_full(board):
    return all(cell != " " for row in board for cell in row)

def get_winner(board):
    for player in ["X", "O"]:
        if check_win(board, player):
            return player
    return None

# ========== SMART AI (Minimax) ==========

def minimax(board, is_maximizing):
    winner = get_winner(board)
    if winner == "O": return 1
    elif winner == "X": return -1
    elif board_full(board): return 0

    if is_maximizing:
        best_score = -float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    score = minimax(board, False)
                    board[i][j] = " "
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    score = minimax(board, True)
                    board[i][j] = " "
                    best_score = min(score, best_score)
        return best_score

def best_ai_move(board):
    best_score = -float("inf")
    move = None
    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "O"
                score = minimax(board, False)
                board[i][j] = " "
                if score > best_score:
                    best_score = score
                    move = (i, j)
    return move

# ========== GAME LOGIC ==========

def play_game(vs_ai=False):
    board = [[" "]*3 for _ in range(3)]
    current = "X"

    speak("Game starts now!")
    print_board(board)

    while True:
        if vs_ai and current == "O":
            time.sleep(0.5)
            i, j = best_ai_move(board)
            speak("AI has made its move.")
        else:
            while True:
                try:
                    print(Fore.YELLOW + f"👉 Player {current}, enter position (1-9): " + Style.RESET_ALL)
                    move = input()
                    pos = int(move) - 1
                    i, j = divmod(pos, 3)
                    if board[i][j] == " ":
                        break
                    else:
                        speak("That spot is taken!")
                except:
                    speak("Enter a number between 1 and 9.")

        board[i][j] = current
        print_board(board)

        if check_win(board, current):
            speak(f"Player {current} wins!")
            color = Fore.GREEN if current == "X" else Fore.CYAN
            print(color + f"🏆 Player {current} is the champion!\n" + Style.RESET_ALL)
            break
        elif board_full(board):
            speak("It's a tie!")
            print(Fore.LIGHTRED_EX + "😅 No winner this time.\n" + Style.RESET_ALL)
            break

        current = "O" if current == "X" else "X"

# ========== MENU ==========

def menu():
    speak("Welcome to Tic Tac Toe")
    print(Fore.YELLOW + "🎮 Choose Game Mode:\n1. Player vs Player\n2. Player vs AI" + Style.RESET_ALL)
    while True:
        choice = input("👉 Your choice (1 or 2): ")
        if choice == "1":
            play_game(vs_ai=False)
            break
        elif choice == "2":
            play_game(vs_ai=True)
            break
        else:
            speak("Please choose 1 or 2.")

    pygame.mixer.music.fadeout(3000)
    again = input("🔁 Play again? (y/n): ").lower()
    if again == "y":
        os.execl(sys.executable, sys.executable, *sys.argv)
    else:
        speak("Thanks for playing with me, legend!")

# ========== LET’S GOOOO ==========

menu()