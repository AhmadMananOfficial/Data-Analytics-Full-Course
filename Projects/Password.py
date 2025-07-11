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

# Strength check logic with hints
def check_strength(pw):
    hints = []
    length = len(pw) >= 8
    has_upper = any(c.isupper() for c in pw)
    has_lower = any(c.islower() for c in pw)
    has_digit = any(c.isdigit() for c in pw)
    has_special = any(c in string.punctuation for c in pw)

    if not length:
        hints.append("📏 Add at least 8 characters")
    if not has_upper:
        hints.append("🔠 Include at least one uppercase letter")
    if not has_lower:
        hints.append("🔡 Include at least one lowercase letter")
    if not has_digit:
        hints.append("🔢 Add at least one number")
    if not has_special:
        hints.append("❗ Include at least one special character (e.g., !, @, #)")

    score = sum([length, has_upper, has_lower, has_digit, has_special])

    if score == 5:
        return ("✅ Strong Password 💪", "green", hints)
    elif score >= 3:
        return ("⚠️ Medium Password — Add more variety!", "orange", hints)
    else:
        return ("❌ Weak Password — Improve it!", "red", hints)

# Check strength and display hints
if st.button("Check Strength"):
    if password.strip():
        msg, color, hints = check_strength(password)
        st.markdown(f"<h4 style='color:{color}'>{msg}</h4>", unsafe_allow_html=True)

        if hints:
            st.markdown("### 🔧 Suggestions to Improve:")
            for hint in hints:
                st.markdown(f"- {hint}")
    else:
        st.warning("⚠️ Please enter a password before checking!")

# Save to file
if st.button("💾 Save Password"):
    if password.strip():
        with open("saved_passwords.txt", "a") as f:
            f.write(password + "\n")
        st.success("Password saved successfully!")
    else:
        st.error("Please enter a password to save!")

# cd D:/Projects/Password
# streamlit run Password.py