from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import streamlit as st

st.title("ChatStream Ollama")

st.write("Calling Ollama")

# --- Create an instance of Chrome WebDriver ---
'''driver = webdriver.Chrome()  # --- or webdriver.Firefox() for Firefox ---

# --- Open a website ---
driver.get("https://share.streamlit.io")

# --- Wait for the page to load ---
time.sleep(2)  # --- You can use WebDriverWait instead ---

# --- Find an element and interact with it ---
search_box = driver.find_element(By.NAME, "q")  # --- Change the element name based on the website ---
search_box.send_keys("Hello World!" + Keys.RETURN)

# --- Wait for the results to load ---
time.sleep(2)

# --- Close the browser ---
driver.quit()'''