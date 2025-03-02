import streamlit as sl
import pandas as pd
import numpy as np
# Set the title for the app
sl.title("Hello World")
# Write a simple message
sl.write("Welcome to the Streamlit app!")
# Slider for selecting a number
x = sl.slider("Select a number:", 50, 100000000)
sl.write(f"The selected number is: {x}")
# Selectbox for choosing an automobile type
x = sl.selectbox("Choose automobile:", ("Mesedece", "Diesel"))
sl.write(f"The selected automobile is: {x}")
# Radio buttons for selection
x = sl.radio("Select an option:", ("aaa", "bbb", "ccc"))
sl.write(f"The selected option is: {x}")
# Multiselect for multiple selections
x = sl.multiselect("Select multiple options:", ("aaa", "bbb", "ccc"))
sl.write(f"The selected options are: {x}")
# Checkbox for a boolean option
x = sl.checkbox("Check this box")
sl.write(f"The checkbox is {'checked' if x else 'unchecked'}.")
# Metric display (updated to use correct parameters)
sl.metric(label="Example Metric", value="11", delta="1")
# Button to trigger an action
if sl.button("Click me"):
    sl.write("Button was clicked!")
# Create a random DataFrame and display line and bar charts
cd = pd.DataFrame(np.random.randint(3, 1000, size=(10, 1)), columns=["Random Numbers"])
sl.line_chart(cd)
sl.bar_chart(cd)