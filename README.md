### What does this repository do? 

This repository uses Eventbrite API ([link](https://www.eventbrite.com/platform/docs/introduction)) and selenium web scraper to search venues on google maps. I gather information about the event (Name, venue name, …) and use the venue name to search its rating and number of reviews on google maps. I use this information to create a dataframe to compare the venue selection of the events and possibly its logistical power (ex. Reserving a well-known venue).

I chose eventbrite because it has hundreds of public events listed with great JSON response formatting. Google maps is easily navigated through Selenium, and near all venues are registered on their database. 

### Why is it valuable?

There are several datasets with event detail. But I go more in depth and analyze the venue in detail and its reviews. It will also provide insight into where the organizers prefer. 

This dataset is unique, as it has most recent/on-going events with secondary information beyond Eventbrite's API capabilities. 


### How to run this repository 

#### Setting up 

1. Clone the repository

git clone https://github.com/GiveChoco/Events\_venue\_detail

2. (if necessary) Set up a virtual environment

python \-m venv .venv

* On Windows:

.venv\\Scripts\\activate

* On macOS and Linux:

source .venv/bin/activate

3. Install package

pip install \-r requirements.txt

#### Running the file

1. Run main.py   
2. Navigate to localhost:5000/login   
3. Make sure you receive the token   
4. Navigate to localhost:5000/Get\_venue  
5. Find ‘Event\_list.csv” in your repository 

#### Optional 
Due to restrictions of Evenbrite's web scraping policy, I implemented a hard-coded array of events to call API on. Please feel free to modify the event array to gather more or diverse events that you prefer. 

