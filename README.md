# Twitter Bot with Google Cloud Functions
A Twitter bot that automatically tweets out messages from a Google Sheets document using the Twitter API, Google Sheets API, and Google Cloud Functions.

# Features
* Automatically tweet messages stored in a Google Sheets document.
* Option to set the frequency of tweets.
* Easy-to-use interface for managing the Google Sheets document.
* Ability to add, modify, and delete messages in the Google Sheets document.
* Scalable and reliable execution of the tweeting function using Google Cloud Functions.
# Prerequisites
* A Twitter account and Twitter API key.
* A Google account with access to Google Cloud Functions and Google Sheets API key.
# Installation
* Clone the repository to your local machine.
* Run npm install to install the dependencies.
* Rename the config.template.js file to config.js and enter your Twitter API and Google Sheets API keys.
* Deploy the function to Google Cloud Functions by following the instructions in the functions directory.
* Schedule the function to run at the desired frequency using the Google Cloud Console.
# Usage
* Create a Google Sheets document and add the messages you want to tweet.
* In the config.js file, set the Google Sheets document ID.
* Deploy the function and schedule it to run at the desired frequency.
* Watch as the function automatically tweets out your messages from the Google Sheets document.
