Install latest python from their website
Make sure to select "ADD TO PATH" during installation

Install git from their website

Open this project to VS Code
open cmd from VS Code with this shortcut: ctrl + `

commands:
cd project
//to change the directory from root folder to project

pip install -r requirements.txt
//to install all necessary dependencies for this project

python manage.py runserver
//to run the server
//open your browser and go to localhost:8000
//go to project/app/urls.py to see all urls available



All HTML files are located inside project/templates/
ALL CSS files are location inside project/static/css

To make the HTML viewable, go to project/app/views.py and create a function. Check other functions for reference
Add that function in project/app/urls.py. Check other urls for reference

