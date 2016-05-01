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
			- URL: '/img/', Directory: '/home/pa-username/Sudoku/Development/static/img/'
			- (Note: replace _pa-username_ with your own)
	- Install necessary modules:
		- pip3 install --user beaker
	- Enjoy!

- Keeping Up-To-Date:
	- Pull the latest Master branch changes using:
		- git pull origin master
	
	- When working on your stuff, please do NOT use the master branch.
	- To create your own branch:
		- git checkout -b my_branch_name
			- use our naming structure: dev_[part]_[task] e.g: dev_controller_status
	- To switch to a branch which is already made:
		- git checkout my_branch_name
	- To switch back to master to grab the latest Sprint work (to be able to use the pull from above)
		- git checkout master

- Adding Your Changes:
	- To add your own branch work to the repo:
		- git add [file list to be added]
		- git commit -m "some message explaining what you added/did"
		- git push -u origin my_branch_name

