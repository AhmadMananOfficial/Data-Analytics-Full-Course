import tkinter as tk
from tkinter import messagebox
import string

# Strength checker function
def check_password():
    password = entry.get()
    length = len(password) >= 8
    has_upper = any(c.isupper() for c in password)
    has_lower = any(c.islower() for c in password)
    has_digit = any(c.isdigit() for c in password)
    has_special = any(c in string.punctuation for c in password)

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        result.set("✅ Strong Password 💪")
        result_label.config(fg="green")
    elif score >= 3:
        result.set("⚠️ Medium Strength Password — Add more variety!")
        result_label.config(fg="orange")
    else:
        result.set("❌ Weak Password — Improve security!")
        result_label.config(fg="red")

# Show/hide password toggle
def toggle_password():
    if entry.cget('show') == '*':
        entry.config(show='')
        show_btn.config(text="Hide Password")
    else:
        entry.config(show='*')
        show_btn.config(text="Show Password")

# Save password to file (for learning purposes)
def save_password():
    password = entry.get()
    with open("saved_passwords.txt", "a") as file:
        file.write(password + "\n")
    messagebox.showinfo("Saved", "Password saved to file!")

# GUI setup
app = tk.Tk()

app.title("Password Strength Checker")
app.geometry("400x300")

label = tk.Label(app, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

entry = tk.Entry(app, show="*", width=30)
entry.pack(pady=5)

show_btn = tk.Button(app, text="Show Password", command=toggle_password)
show_btn.pack(pady=5)

check_btn = tk.Button(app, text="Check Strength", command=check_password)
check_btn.pack(pady=5)

save_btn = tk.Button(app, text="💾 Save Password", command=save_password)
save_btn.pack(pady=5)

result = tk.StringVar()
result_label = tk.Label(app, textvariable=result, font=("Arial", 12))
result_label.pack(pady=10)

app.mainloop()


import streamlit as st
import string

st.set_page_config(page_title="Password Strength Checker", page_icon="🔐")
st.title("🔐 Password Strength Checker")
st.markdown("Enter your password below to see how strong it is!")

# Password input
password = st.text_input("Enter password:", type="password")

# Show password toggle
if st.checkbox("Show password"):
    st.text(f"🔎 Your password: {password}")

# Strength check logic
def check_strength(pw):
    length = len(pw) >= 8
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in string.punctuation for c in pw)

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return ("✅ Strong Password 💪", "green")
    elif score >= 3:
        return ("⚠️ Medium Password — Add more variety!", "orange")
    else:
        return ("❌ Weak Password — Improve it!", "red")

# Check button
if st.button("Check Strength"):
    if password:
        msg, color = check_strength(password)
        st.markdown(f"<span style='color:{color}; font-size:18px'>{msg}</span>", unsafe_allow_html=True)
    else:
        st.warning("Please enter a password first!")

# Save to file
if st.button("💾 Save Password"):
    if password:
        with open("saved_passwords.txt", "a") as f:
            f.write(password + "\n")
        st.success("Password saved successfully!")
    else:
        st.error("Please enter a password to save!")