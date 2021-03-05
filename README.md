# Desktop Lackey

**Lackey** is a desktop application built on top of [Neuron](https://github.com/Andrew-Shay/Neuron) (a Python project that allows an application's GUI to be built with HTML and Javascript). 

I chose ```Neuron``` over popular Python GUI libararies because I found the project very interesting and I also wanted to have a frontend that I felt only ```React``` could  properly deliver.

The goal of this project was an desktop application that I could customize and quickly reference without having to open a browser and go to bookmarks or tabs to obtain the information I am looking for.

Right now the application has the following features:
  - Calendar 
  - Notepad(s)
  - Weather Forecast
  - Stock Portfolio Tracker
  - Sports Schedule/Stats Tracker
    - NBA
    - EPL
    - NFL

The ```master``` branch of this repository will serve as a base version of the application or template for others to build or customize their own desktop applications using the work I have already done. I will continue developing lackey in my ```personal``` branch as a personalized version.

The two features that requires an API key are ```finance```, go [here](https://www.alphavantage.co/support/#api-key) and ```soccer```, go [here](https://www.football-data.org/client/registery) add your key to ```lackey/__info__.py``` in the ```API_KEYS``` dictionary.

## How To

### Try it out

 **1.** clone this repo
 
 **2.** ```cd``` into the repo
 
 **3.** ```pip install -r requirements```
 
 **4.** ```python -m lackey```
 
 **5.** the application should now be open and running
 
## Create an EXE and Install (Windows only)

**1.** install [NSIS](http://nsis.sourceforge.net/Download) (3rd party program that creates the installer)

**2.** follow above 1-3

**3.** ```cd``` into the build directory

**4.** ```python build.py```

**5.** navigate to the ```build/dist``` folder

**6.**  click ```Install-Lackey-v1.00``` and follow the GUI instructions

**7.** you should now have an EXE you can launch at any time on your machine

## Demo

![Alt Text](demo.gif)


## References

[Neuron](https://github.com/Andrew-Shay/Neuron) - Build a Python GUI using HTMl and  CSS

[CEFPython](https://github.com/cztomczak/cefpython) - Python bindings for the Chromium Embedded Framework  

[Flask](http://flask.pocoo.org/) - Python web framework  

[Flask-SQLAlchemy](https://github.com/pallets/flask-sqlalchemy) - Extension for Flask that adds support for SQLAlchemy

[Flask-Restful](https://github.com/flask-restful/flask-restful) - REST api for Flask

[Create-React-App](https://github.com/facebook/create-react-app) - Web Front-End Framework  

[PyInstaller](http://www.pyinstaller.org/) - Turn Python projects into executables  

[NSIS](http://nsis.sourceforge.net/Main%5FPage) - Creates installer  

## API References

[Alphavantage](https://www.alphavantage.co/documentation/) - Stock API

[Metaweather](https://www.metaweather.com/api/) - Weather API

[nba_api](https://github.com/swar/nba_api)  - Unofficial API client for NBA stats and information

[Football-Data.org](https://www.football-data.org/documentation/quickstart) - Soccer API

[Hidden ESPN API](https://gist.github.com/akeaswaran/b48b02f1c94f873c6655e7129910fc3b) - For NFL schedule info

