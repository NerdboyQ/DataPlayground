# NIH Webapp
_The National Institute on Minority Health & Health Disparities, or NIH, maintains historical data that can be used for Data Analysis._

_This webapp will serve as a means to practice data collection & visualization with a dynamic web based user interface._

## What is Flask?
Flask is a lightweight Web Server Gateway Interface (WSGI) web application framework. Traditionally websites are static with data & images to display, as opposed to a webapp that is interactive and has functionality to update and/or manipulate what is displayed on the screen and the data/images included. 

Basically Flask was made with the intention of quickly creating simple webapps using Python. The webapps can be used on one machine or, through a internet connection, served across a network to all connected computers. For more on Flask: [Click HERE](https://flask.palletsprojects.com/en/stable/#)

## User (Web) Interface
To simplify the User Interface (UI) design for the webapp, the Materialize Deisgn by Google is being used for web elements and 
functionality similar to what most user's today would expect while 
browsing the internet.

> NOTE: The html code pulls the Materialize resouces live from the internet, so if internet connection is loss the UI will appear different.

## HOW-TO
Currently the webapp is built to easily run on Window's computers by simply double clicking on the `run.bat` file. It is a batch script to start the webapp, and once started an IP address will be provided in the command window for users to copy and paste into a 
web browser.

### <U>run.bat flow</u>:
1. Check if python is installed on the computer
2. Get the given python version & its executable file name
3. Call the `check_requirements.py` script, in the `utils` folder, to check for all the required libraries for the webapp to run & installs them if they're not found
4. Starts the webapp 

## Web Scraper/Crawler
A Web Scraper or Web Crawler is a term used to describe automation software, or _"bots"_, that collects large amounts of data from the internet with no human interaction. A web scraper is currently in 
development for this project using `selenium` a popular library used for web automation. 

Selenium is used to mimic a human users interaction with through a web browser (Chrome in this instance); capable of mouse clicks, text entry, drop down selection, opening/closing tabs, etc. For more on selenium using python click [HERE](https://selenium-python.readthedocs.io/).

> NOTE: The web scraper is being developed to use a Chrome Browser, so Chrome must be installed on the computer running the code.