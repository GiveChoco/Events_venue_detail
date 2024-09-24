from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from flask import Flask, redirect, request, session
import requests
from dotenv import load_dotenv
import os

driver = webdriver.Chrome()
driver.get('https://www.google.com/maps')

def searchplace():
    # Locate the input field by its class or XPath
    Place = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')  # Target the input field directly
    Place.send_keys("Carlyle Court")

    # Locate the submit button and click it
    Submit = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
    Submit.click()

# Execute the search
searchplace()

# Wait to ensure the page loads after the search
time.sleep(3)

# Navigate to the Google Maps URL
#url = "https://www.google.com/maps/place/The+Home+Depot/@43.0443207,-89.480609,13z/data=!4m14!1m7!3m6!1s0x8807adb38d960edd:0xa05b4f6e654c0175!2sMadison+Public+Library+-+Sequoya!8m2!3d43.05394!4d-89.4504112!16s%2Fg%2F1td9r2q1!3m5!1s0x8807adeaeb86497f:0x517067add9ddecca!8m2!3d43.0363524!4d-89.457314!16s%2Fg%2F1tdftqk5?entry=ttu&g_ep=EgoyMDI0MDkxOC4xIKXMDSoASAFQAw%3D%3D"
#driver.get(url)

# Extract the rating element (Google Maps ratings often have a unique class or can be found by XPath)
rating_element = driver.find_element(By.XPATH, "//div[contains(@class,'F7nice')]")
rating_numbers = driver.find_element(By.XPATH,"//div[contains(@class, 'F7nice')]//span/span/span[contains(@aria-label, 'reviews')]")

# Get the rating text
rating = rating_element.text
rating_num = rating_numbers.text.replace('(','').replace(')','')


# Print the extracted rating
print(f"Rating: {rating}")
print(f"Number of reviews: {rating_num}")


# Close the driver
driver.quit()

