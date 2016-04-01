# Sudoku
Sock Monkey Sudoku Web App

- MVC Framework:
	- /views : HTML/TWIG front layer
		- /css : CSS Descriptors
	- /src
		- /Controllers : Python Controller middle layer
		- /Model : Python Model back layer
- Installation:
	- Create a Bottle (Python 3.4) web app, with bottle application located at: /your-PA-username/Sudoku/Development/index.py
	- Open up a console, go to the main Sudoku directory, and remove the Development directory (trust us)
		- cd Sudoku/
		- rm -r Development
	- Clone the master branch:
		- git clone https://github.com/sockmonkeysoftware/Development.git
		- This should re-create the Development branch, but now with the application located within.
	- Add the Javascript and CSS directories to your app's URL hooks:
		- Go to the Web tab of PA
		- scroll down to the section "Static files:"
		- Add records:
			- URL: '/css/', Directory: '/home/pa-username/Sudoku/Development/static/css/'
			- URL: '/js/', Directory: '/home/pa-username/Sudoku/Development/static/js/'
			- (Note: replace _pa-username_ with your own)
	- Install necessary modules:
		- pip3 install --user beaker
	- Enjoy!
