import requests
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://www.selenium.dev/selenium/web/web-form.html")

# Navigate to the Google Maps URL
url = "https://www.google.com/maps/place/The+Home+Depot/@43.0443207,-89.480609,13z/data=!4m14!1m7!3m6!1s0x8807adb38d960edd:0xa05b4f6e654c0175!2sMadison+Public+Library+-+Sequoya!8m2!3d43.05394!4d-89.4504112!16s%2Fg%2F1td9r2q1!3m5!1s0x8807adeaeb86497f:0x517067add9ddecca!8m2!3d43.0363524!4d-89.457314!16s%2Fg%2F1tdftqk5?entry=ttu&g_ep=EgoyMDI0MDkxOC4xIKXMDSoASAFQAw%3D%3D"
driver.get(url)

# Extract the rating element (Google Maps ratings often have a unique class or can be found by XPath)
rating_element = driver.find_element(By.XPATH, "//div[contains(@class,'F7nice')]")

# Get the rating text
rating = rating_element.text

# Print the extracted rating
print(f"Rating: {rating}")

# Close the driver
driver.quit()

