import streamlit as sl
import pandas as pd
import numpy as npy


sl.title("Hello world")

sl.write("T")

x = sl.slider("This is",50, 100000000)
sl.write(f"The : {x}")

x = sl.selectbox("Choose automobil", ("Mesedece", "Disel"))
sl.write(f"The : {x}")

x = sl.radio("ndfds", ("aaa, bbb, ccc"))
sl.write(f"The : {x}")

x = sl.multiselect("ddfds", ("aaa, bbb, ccc"))
sl.write(f"The : {x}")

x = sl.checkbox("bdfds")
sl.write(f"The : {x}")

'''k = sl.toggle("bdfds",)
sl.write(f"The : {k}")

x = sl.text_input("123468")
sl.write(f"The : {x}")'''

sl.metric()
sl.metric(label = "The", value = "11", "1")

x = sl.button("ff")
cd = pd.DataFrame(npy.random.randint(3, 1000))

sl.line_chart(cd)
sl.bar_chart(cd)