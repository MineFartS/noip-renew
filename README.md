
# Automatically confirm noip.com free hosts

[noip.com](https://www.noip.com/) free hosts expire every month.
This script uses [Selenium](https://www.selenium.dev/) and [GAS](https://script.google.com/home) to automatically renew hosts

 - [Selenium](https://www.selenium.dev/) is used to automatically navigate No-IP.com to renew the hosts.
 - [GAS](https://script.google.com/home) is used to grab the OPTs from your gmail inbox. 
.

Part 1 - Google Apps Script API:
-
 - Make a Copy of [this](https://script.google.com/d/1bi5-ZaJqsU68AG7DPTyPQV273J9mjMmGYzeDZlIo1aXqyoF-sWq2TUKg/edit?usp=sharing) Google Apps Script
	 - Open Overview
	 - Click Make a Copy
 - Publish as a web app
	 - Click 'Deploy' in the top right
	 - Click 'New Deployment'
	 - Click on the gear icon next to 'Select Type'
	 - Check 'Web App'
	 - Set 'Execute as' to 'Me (Your email)'
	 - Set 'Who has access to 'Anyone'
	 - Click 'Deploy'
	 - Click 'Authorize access'
	 - Click on your email
	 - Click 'Advanced'
	 - Click 'Go To [Script Name]'
	 - Click 'Allow'
	 - Copy the Web App URL
	  
Part 2 - Execution
-
- To run the script, `cd` into the directory with the script files and run  `python run.py`
- The script will ask you for the following during the initial execution:
    1. Apps Script URL
    2. NoIP Email
    3. NoIP Password
