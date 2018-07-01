# INSTALL PROJECT: python3.6, kivy1.11
# --------------------------------------------

git clone ....

	cd configurator

### imstall virtualenv and dependencies for projects 

	sudo pip install --upgrade pip virtualenv setuptools
	virtualenv --no-site-packages -p python3.6 venv
	. venv/bin/activate
	pip install -r requirements.txt

### commands for running project

- firts console window:
	python server/server.py

- second console window:
	python main.py

# ---------
# - END - #
# ------------------------------------------------------
