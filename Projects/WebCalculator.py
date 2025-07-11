import streamlit as st
import math
import streamlit.components.v1 as components

st.set_page_config(page_title="Web Calculator", page_icon="🧮")
st.title("🧮 Python Web Calculator")
st.markdown("Use this interactive calculator to perform basic operations in real time!")

# Session state for history
if "history" not in st.session_state:
    st.session_state.history = []

# JS keyboard shortcuts script
keyboard_shortcuts_js = """
<script>
document.addEventListener("keydown", function(event) {
    const key = event.key.toLowerCase();

    if (key === "enter") {
        let btn = window.parent.document.querySelector('button[kind="primary"]');
        if (btn) { btn.click(); }
    }
    if (event.altKey && key === "a") {
        selectRadio("➕ Add");
    }
    if (event.altKey && key === "s") {
        selectRadio("➖ Subtract");
    }
    if (event.altKey && key === "m") {
        selectRadio("✖ Multiply");
    }
    if (event.altKey && key === "d") {
        selectRadio("➗ Divide");
    }
    if (event.altKey && key === "p") {
        selectRadio("xʸ Power");
    }
    if (event.altKey && key === "r") {
        selectRadio("√ Square Root (1st number)");
    }
});

function selectRadio(labelText) {
    const labels = window.parent.document.querySelectorAll('label');
    labels.forEach(label => {
        if (label.innerText.trim() === labelText) {
            label.click();
        }
    });
}
</script>
"""
components.html(keyboard_shortcuts_js)

# Input fields
num1 = st.number_input("Enter first number", step=1.0, format="%f")
num2 = st.number_input("Enter second number", step=1.0, format="%f")

# Operation selection
operation = st.radio("Choose an operation:", (
    "➕ Add", "➖ Subtract", "✖ Multiply", "➗ Divide", "xʸ Power", "√ Square Root (1st number)"
))

# Perform calculation based on selection
def calculate(x, y, op):
    if op == "➕ Add":
        return round(x + y, 2)
    elif op == "➖ Subtract":
        return round(x - y, 2)
    elif op == "✖ Multiply":
        return round(x * y, 2)
    elif op == "➗ Divide":
        if y == 0:
            return "❌ Error: Cannot divide by zero!"
        return round(x / y, 2)
    elif op == "xʸ Power":
        return round(math.pow(x, y), 2)
    elif op == "√ Square Root (1st number)":
        if x < 0:
            return "❌ Error: Cannot take square root of a negative number!"
        return round(math.sqrt(x), 2)

# Display result
if st.button("Calculate 💡"):
    result = calculate(num1, num2, operation)
    if isinstance(result, str):
        display = result
    else:
        display = f"{operation} ➜ {result}"
        st.session_state.history.append(display)
    st.markdown(f"### ✅ Result: `{display}`")

# Show history
if st.session_state.history:
    st.markdown("---")
    st.markdown("### 🧾 History:")
    for entry in reversed(st.session_state.history[-5:]):  # show last 5 entries
        st.markdown(f"- {entry}")

# Cool footer
st.markdown("---")
st.markdown("🔁 Press **Enter** to calculate or use these shortcuts:")
st.markdown("- ⌨️ `Alt + A` ➕ Add")
st.markdown("- ⌨️ `Alt + S` ➖ Subtract")
st.markdown("- ⌨️ `Alt + M` ✖ Multiply")
st.markdown("- ⌨️ `Alt + D` ➗ Divide")
st.markdown("- ⌨️ `Alt + P` xʸ Power")
st.markdown("- ⌨️ `Alt + R` √ Root")
