# GrandPy Bot, some locations, many stories
----------------
GrandPy Bot is a web application managed by Master Roshi, from the famous Dragon Ball manga. Since he retired from the martial arts,
he has no choice but to listen his grandsons and grandaughters ask him about all the places he went. To enjoy his retirement, Master Roshi
invented GrandPy Bot, a web robot who does all the work for him.
Ask him politely and GrandPy Bot will find you locations and all the stories about them... Or not.

# What does GrandPy Bot really do ?
----------------
Once you arrive on the [GrandPy Bot web page](https://gp-bot-app.herokuapp.com/) :\
	- you can chat with GrandPy Bot (careful, he has bad temper) \
	- you can ask him to find a location and its historical background \
	- a map will be displayed each time you request a location

GrandPy Bot is hosted by [Heroku](https://www.heroku.com/), and for now is only available in french language.	

# For developpers, how to install and work on the app :
--------------
Clone with https : https://github.com/Nastyflav/GrandPapyBot_OC.git \
or clone with SSH : git@github.com:Nastyflav/GrandPapyBot_OC.git \
into a repo on your local machine \
Documentation about pull --> https://help.github.com/en/articles/cloning-a-repository 

Set your virtual environment under python3.8.x `pip install virtualenv`\
Create an new virtual environment `virtualenv -p python env`\
Activate it `source env/Scripts/activate.bat`\
Install requirements `pip install -r requirements.txt`\
Open the config.py file and place your Google Maps API key into the Google Maps presets\
Write `run_program.py` in your terminal 

## Dependancies :

Python 3.8.2 \
download : https://www.python.org/downloads/ \
install : https://realpython.com/installing-python/ 

Depending of your python's install, you might need PIP\
install pip : https://packaging.python.org/tutorials/installing-packages/

## Modules :

run_program.py\
config.py\
gpb_app/models/ contains all the different classes and the app functions\
gpb_app/templates/ manages the frontend structure with an html file \
gpb_app/static/ contains the images, fonts, js script and css files\
gpb_app/views.py manages the Flask module\
gpb_app/tests/ all the test files, with mocks\

## Built with :

Visual Studio Code (IDE)\
Python 3.8.2\
UTF-8

## Author :

Flavien Murail : https://github.com/Nastyflav