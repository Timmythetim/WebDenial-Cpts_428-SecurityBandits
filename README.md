# WebDenial

## Setup
**1. Download source code and open up a terminal** <br>
**2. Setup an environment for the project** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. "python -m venv project-name" will create a folder project name with environment info <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(myvenv or venv suggested they are already in the git ignore)  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Activate the environment go to project-name/Scripts and run activate or activate.bat  for example-> source (project_name)/bin/activate<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. You should see (project-name) on the far left of your terminal  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;4. Make sure you run activate every time you open a new terminal to work inside your env <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;(You can run into version control issues if not)   <br> <br>
**3. Install the python reqs**<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Make sure you are in the same dir as requirements.txt<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Run "pip install -r requirements.txt"<br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. This gives you all the packages used for the project (Just Django for now)<br>
## Django Server
**To run the Django Server on localhost:8000 by default** <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Make sure you're in the same directory as manage.py (WebDenial) <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Run "python manage.py runserver" <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Ctrl-C in terminal will quit the server  <br>

## Description
A Simple Blog app for testing Denial of Service attacks against. (Educational Purposes WSU CPTS 428 Project).
## Scenario
A user either creates an account or logs in, posts a blog, looks at other posts or their own posts. Our goal is to deny some of those services through methods learned in class.<br>
