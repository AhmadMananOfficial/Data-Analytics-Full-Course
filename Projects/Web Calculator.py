import streamlit as st

st.set_page_config(page_title="Web Calculator", page_icon="🧮")
st.title("🧮 Python Web Calculator")
st.markdown("Use this interactive calculator to perform basic operations in real time!")

# Input fields
num1 = st.number_input("Enter first number", step=1.0, format="%f")
num2 = st.number_input("Enter second number", step=1.0, format="%f")

# Operation selection
operation = st.radio("Choose an operation:", (
    "➕ Add", "➖ Subtract", "✖ Multiply", "➗ Divide"))

# Perform calculation based on selection
def calculate(x, y, op):
    if op == "➕ Add":
        return x + y
    elif op == "➖ Subtract":
        return x - y
    elif op == "✖ Multiply":
        return x * y
    elif op == "➗ Divide":
        if y == 0:
            return "❌ Error: Cannot divide by zero!"
        return x / y

# Display result
if st.button("Calculate 💡"):
    result = calculate(num1, num2, operation)
    st.markdown(f"### ✅ Result: `{result}`")

# Cool footer
st.markdown("---")
st.markdown("🔁 Try changing values or operation above to see ral-teime results!")
