from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from flask import Flask, redirect, request, session
import requests
from dotenv import load_dotenv
import os
import pandas as pd
import numpy as np


load_dotenv()
app = Flask(__name__)

def fetch_information(venue_name):
    driver = webdriver.Chrome()
    driver.get('https://www.google.com/maps')

    def searchplace():
    # Locate the input field by its class or XPath
        Place = driver.find_element(By.XPATH, '//*[@id="searchboxinput"]')  # Target the input field directly
        Place.send_keys(venue_name)

    # Locate the submit button and click it
        Submit = driver.find_element(By.XPATH, '//*[@id="searchbox-searchbutton"]')
        Submit.click()

# Execute the search
    searchplace()

# Wait to ensure the page loads after the search
    time.sleep(3)

    # Extract the rating element (Google Maps ratings often have a unique class or can be found by XPath)
    try:
        rating_element = driver.find_element(By.XPATH, '//*[@id="QA0Szd"]/div/div/div[1]/div[2]/div/div[1]/div/div/div[2]/div/div[1]/div[2]/div/div/div[2]/span[1]/span[1]')
        rating = rating_element.text
    except:
        rating = "N/A"
    
    try:
        rating_numbers = driver.find_element(By.XPATH,"//div[contains(@class, 'F7nice')]//span/span/span[contains(@aria-label, 'reviews')]")
        rating_num = rating_numbers.text.replace('(','').replace(')','')
    except:
        rating_num = "N/A"


     # Close the driver
    driver.quit()

    return rating, rating_num

def get_venue(event_id):
    
    headers = {
    'Authorization': f'Bearer {session['access_token']}',}

    params = {
    'expand': 'venue',
    }

    response = requests.get(f'https://www.eventbriteapi.com/v3/events/{event_id}/', params=params, headers=headers)

    Event_row = []

    if response.status_code == 200:
        event = response.json()
        venue = event['venue']
        
        venue_name = venue['name']
        event_id = event['id']
        event_name = event['name']['text']
        venue_area = venue['address']['localized_area_display']
        
        Event_row.append(event_id)
        Event_row.append(event_name)
        Event_row.append(venue_name)
        Event_row.append(venue_area)

        rating, rating_num = fetch_information(venue_name)
        Event_row.append(rating)
        Event_row.append(rating_num)

        return Event_row
       
    else:
        return f"Error: {response.text}", response.status_code
    
event_array = [1013544838897,989096172277,1021741364927,967246519377,1003868767507,925408962117]

CLIENT_ID = os.getenv('MY_API')
CLIENT_SECRET = os.getenv('SECRET_KEY')
ACCESS_CODE = os.getenv('ACCESS_CODE')
REDIRECT_URI = f'http://localhost:5000/oauth/redirect?code={ACCESS_CODE}'
SECRET_FLASK = os.getenv('FLASK_S')

# Step 1: Redirect user to the Eventbrite authorization URL
@app.route('/login')
def login():
    eventbrite_authorization_url = (
        f"https://www.eventbrite.com/oauth/authorize"
        f"?response_type=code&client_id={CLIENT_ID}&redirect_uri={REDIRECT_URI}"
    )
    return redirect(eventbrite_authorization_url)

# Step 2: Handle the OAuth callback and exchange the code for an access token
@app.route('/oauth/redirect')
def oauth_callback():
    access_code = request.args.get('code')
    print("Callback received with code:", access_code)

    token_url = 'https://www.eventbrite.com/oauth/token'
    token_data = {
        'grant_type': 'authorization_code',
        'code': access_code,
        'client_id': CLIENT_ID,
        'client_secret': CLIENT_SECRET,
        'redirect_uri': REDIRECT_URI
    }
    token_headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    token_response = requests.post(token_url, data=token_data, headers=token_headers)

    if token_response.status_code == 200:
        session['access_token'] = token_response.json().get('access_token')
        return f"Access Token: {session['access_token']}"
    else:
        return f"Error: {token_response.text}", token_response.status_code

@app.route('/Get_venue')
def build_DF():
    df_array = []
    for ID in event_array:
        app = get_venue(ID)
        df_array.append(app)

    array = np.array(df_array)
    df = pd.DataFrame(array)
    df = pd.DataFrame(array, columns=['Event_ID', 'Event_name', 'Event venue','Venue area','venue rating','venue number of reviews'])

    df.set_index('Event_ID', inplace=True)
    df.to_csv('Event_list.csv')
    return "Dataframe build succesful"


if __name__ == '__main__':
    app.config['SECRET_KEY'] = SECRET_FLASK
    app.config['SESSION_TYPE'] = 'filesystem'
    app.run(debug=True)




