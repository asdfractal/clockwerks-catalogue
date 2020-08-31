# Clockwerk's Catalogue

A small web app designed to allow users to create a list of their favourite heroes from the game 'DOTA 2'. Users can also create a small profile with a biography and information related to the game, as well as attach personal notes to their favourite heroes.

This is a website developed for Code Institute milestone project 3.

## Contents:
* User Experience
    * Project Goals
    * Target Audience Goals
    * Site Owner Goals
    * User Stories
    * Requirements
    * Expectations
* Design Choices
    * Colours
    * Fonts
    * Icons
    * CSS
    * Images
    * Wireframes
    * Code Styling
* Information Architecture
* Features
    * Implemented Features
    * Planned Features
* Technologies Used
    * Languages
    * Tools & Libraries
* Testing & Bugs
* Development & Deployment
    * Local Development and Set-Up
    * Heroku Deployment
* Credits
    * Images
* Acknowledgements
* Disclaimer

## User Experience

### Project Goals
The goal of this project is to provide a complete list of all heroes in the computer game 'DOTA 2' for players of the game. The users of the website will be able to create a favourite heroes list for their future reference. The target audience is players of the game.

### Target Audience Goals
* To view a complete list of DOTA 2 Heroes
* Create an account and add to a favourite heroes list
* A visual design that appeals to gamers and fans of DOTA 2
* To view and interact with the website on mobile, tablet and desktop

### Site Owner Goals
* Provide users an easy way to keep track of their favourite heroes
* Aquire a collection of data from site analytics
* Create a personal favourites list
* Promote YouTube channel and gain potential subscribers through link to hero guides

### User Stories
* As a user, I would like to be able to see a list of all the heroes so that I can pick a specific one
* As a user, I would like to be able to filter the heroes by their primary attribute so that I can narrow my selection
* As a user, I would like to be able to see detailed information about a hero to assist my selection process
* As a user, I would like to be able to add notes or a comment about a hero so that I can remember why I added it to my list

#### Requirements
* Easy to use and navigate the website
* Create an account and view list
* Create a list of heroes
* Functionality to add personal notes to hero
#### Expectations
* User information is protected
* Website load times are sufficient
* Information is stored and can be easily accessed at a later date

## Design Choices
The design of the website is a minimalist white theme with a prominent centered display box, raised from the background with a sharp box shadow and border. To achieve this I have chosen the [Spacelab](https://bootswatch.com/spacelab/) theme from Bootswatch, which I will use as a base and build upon with my own accents.

The current iteration of the design is the result of a complete overhaul of the styles after being dissatisfied with the original implementation.

### Colours
I used the 'DOTA 2 Red' colour in a complimentary colour tool to find the 'Harvest Gold' colour

![Colour Pallete](/wireframes/colour-palette.png).

* Dota 2 Red - #9E2F19 - This is the colour used in the DOTA 2 logo. It is used as the primary accent colour on the website
* Vermillion - #E12500 - Dota 2 red a few shades lighter
* Harvest Gold - #D7920A - A complimentary gold colour, used to signify a hero is on the user's favourites list
* Ghost White - #F4F4F4 - Slightly off white used in place of white

### Fonts
* Headers - 'Audiowide' - I found  this modern looking display font on [Google Fonts](https://fonts.google.com/), which I think looks very good for the purpose of this website
* Body - 'Lato' - Using the popular pairings section of Google Fonts I chose Lato, an easy to read san serif font

### Icons
I have font awesome icons across the website to aid in displaying content and navigation options instead of using only text. There are also official DOTA2 icons on the heroes page and cards.

### CSS
* I am using the [BEM](http://getbem.com/) naming convention for my CSS classes to create modular, reusable components.

Note on CSS: I have chosen to use vw/vh on padding and margins in a lot of cases as I believe this allows for an even more responsive experience than using solely rem. My decision was influenced by my own experimentation as well as researching, particularly [this](https://www.elegantthemes.com/blog/divi-resources/better-mobile-website-design-how-to-use-vw-vh-and-rem-to-create-fluid-divi-pages) article.

### Images
The background image on the home page is a hero from the game - Clockwerk - which the website is named after. The logo is an image I made by combining an icon of Clockwerk and two of the letter C from the Audiowide font. The rest of the images are from Valve and credited in the credits section of the readme.

### Wireframes
I created the wireframes using Balsamiq Wireframes. The mobile/tablet are combined because there will be minimal differences in the design. I used them as a blueprint and then adjusted based on further testing to reach the final design. The wireframes can be viewed [here](/wireframes/).

### Code styling
For consistency and readable code I am using formatters and format on save option.
* HTML - Beautify
* SCSS - Formate
* JavaScript - Prettier (options)

    ```json
    "printWidth": 88,
    "tabWidth": 4,
    "trailingComma": "all",
    "semi": false
    ```

* Python - Black

#### Rationale
I spent quite a bit of time reading about JavaScript and Python formatting conventions and settled on this configuration for a few reasons. For JS, I prefer the clean look without semicolons but I understand it can cause ASI errors. The 'semi: false' setting of Prettier covers this and will insert them where this could occur.
I decided to use Black as my Python formatter because I liked what I read about it and after using it I like the code it produces. It has a line length of 88 and solid reasoning behind this choice, I chose the same number for Prettier to be consistent across the project. Using pylint-flask and a vscode extension called Error Lens I am notified immediately of errors in my code and this has helped me to write functional code and learn about best practices.

## Information Architechture

View the data schemas for the project [here](/data/schemas).

**Users Collection**
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectId
Name|name|String
Password|password|Hashed String
Favourites|favourites|Array
Primary role|primary_role|String
Region|region|String
Best Rank|best_rank|String
Current Rank|current_rank|String
Avatar|avatar|String
Biography|biography|String

**Favourites Array (nested inside user object)**
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Hero|hero|ObjectId
Note|note|String

**Heroes Collection**
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
Object ID|_id|ObjectId
Hero ID|id|Int
Name|name|String
Primary Attribute|primary_attr|String
Hero Thumbnail|image_thumb|String
Hero Portrait|image_full|String
Hero Roles|roles|Array
Attack type|attack|String

The hero id property corresponds to the in game id of the hero and is used for administrative purposes.

## Features
### Implemented Features
* Authentication system to create account, login and logout
* Passwords are encrypted using Werkzeug security package
* Dynamically changing user interaction options based on if they are logged in or not
* Full hero list display with a additional information in a popup modal in card format
* API that handles a query from the user to filter heroes by their primary attribute
* Dyanmic updating of the DOM with the response from the API
* A favourite heroes list, which the user can modify from the hero page or a separate page displaying their list
* Additional section of the favourite list to store personal notes about each hero on the list
* Personal profile page which the user can update with in game stats and a biography
* Toast messages to inform user of actions such as adding and removing heroes

### Planned Features
* Account deletion option
* Page to display all users profiles for other users to view and connect with the community

## Technologies Used
### Languages
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
* [JSON](https://www.json.org/json-en.html)
* [Python](https://www.python.org/)

### Libraries
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Flask PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
* [dnspython](https://pypi.org/project/dnspython/)
* [Pylint](https://pypi.org/project/pylint/)
* [Pylint-Flask](https://pypi.org/project/pylint-flask/)
* [Black](https://pypi.org/project/black/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
* [Gunicorn](https://gunicorn.org/)
* [Bootstrap](https://getbootstrap.com)
* [Bootswatch](https://bootswatch.com/)
* [JQuery](https://jquery.com)
* [Popper.JS](https://popper.js.org/)

### Tools
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com)
* [Git](https://git-scm.com/)
* [Postman](https://www.postman.com/)
* [Beautify](https://marketplace.visualstudio.com/items?itemName=HookyQR.beautify)
* [Formate](https://marketplace.visualstudio.com/items?itemName=MikeBovenlander.formate)
* [JShint](https://jshint.com/)
* [Error Lens](https://marketplace.visualstudio.com/items?itemName=usernamehw.errorlens)

## Testing & Bugs
A full write up for testing and dealing with bugs is [here](/TESTING.md)

## Development & Deployment
Note: *These instructions are applicable to Windows and VSCode, and will be using the tool [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/). A requirements.txt file is also available if you are not using Pipenv. If you are not using Windows or VSCode please refer to your IDE documentation for any differences.*

### Local Development and Set-Up
Requirements to run locally:
* An IDE such as [VSCode](https://code.visualstudio.com/)

You have have installed
* [Python 3](https://www.python.org/downloads/)
* [PIP](https://pip.pypa.io/en/stable/installing/)
* [Git](https://gist.github.com/derhuerst/1b15ff4652a867391f03)
* [MongoDB Community Edition](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

You have a free account with [MongoDB Atlas](https://www.mongodb.com/) to create the database. Please refer to [their documentation](https://docs.atlas.mongodb.com/getting-started/) for instructions on how to create a new account and database

*All commands from this point should be entered in the terminal of your IDE*

Install Pipenv with this command

`pip install --user pipenv`

#### Instructions

1. Clone the repository with this command

    `git clone https://github.com/asdfractal/clockwerks-catalogue`

2. In your IDE terminal, navigate to this folder
3. Install the required packages and start your virtual environment with these commands

    `pipenv install`

    `pipenv shell`

4. Set up your environment variables
    * create a folder in project root called `.vscode`, inside this folder create a file called `settings.json` and create this json object. Remove the angle brackets `<>` and place your variables inside the quotes.

    ```json
        "terminal.integrated.env.windows": {
            "SECRET_KEY": "<your key>",
            "MONGO_URI": "<your connection address>",
            "DBNAME": "<your database name>",
            "DEBUG": "True"
        }
    ```

    * `SECRET_KEY` is a long random string and can be generated [here](https://keygen.io/).
    * To obtain `MONGO_URI` please refer to the [MongoDB documentation](https://docs.atlas.mongodb.com/tutorial/connect-to-your-cluster/) on how to connect your app to the cluster
    * `DBNAME` is your chosen database name when you made an account
    * Close your VSCode terminal session and open a fresh terminal to activate the variables, and restart your environment with `pipenv shell`
    * Create a `.gitignore` file and add `.vscode` to ensure the security of your environment variables

5. Load the data into the database

Note: *Please follow [these](https://www.computerhope.com/issues/ch000549.htm) instructions for adding a variable to your system path in Windows, and create a new variable with this path*

    C:\Program Files\MongoDB\Server\4.4\bin

* Restart VSCode to register the new system path
* Please refer to the [MongoDB documentation](https://docs.atlas.mongodb.com/command-line-tools/) on how to connect to the cluster using the CLI. Enter the following command

    `mongoimport --uri="YOUR_URI_HERE" --file=heroes.json`

6. Start your environment and run the app locally with these commands

    `pipenv shell`

    `python app.py`

    You can now view the website on your local machine at the address shown in the terminal

### Heroku Deployment

1. On the [Heroku](https://www.heroku.com/) website, create an account or login
2. Create a new app from your dashboard by clicking **New** and then **Create new app**
3. Enter a name, select a region and then click **Create app**
4. Navigate to the **Settings** page, click on **Reveal Config Vars** in the Convig Vars section
5. Set the following Config Vars

    | Key | Value |
    --- | ---
    `SECRET_KEY` | `your key`
    `IP` | 0.0.0.0
    `MONGO_URI` | `your connection address`
    `DBNAME` | `your database name`

6. Before proceeding further you must create a new repo on github by following these steps
    * On the [GitHub](https://github.com/) website, sign in or create an account
    * Click on the *green* **New** button and give your repo a name, then click **Create repository**
    * From the **Quick setup** section copy the github url to your repo
    * In the terminal in your IDE, make sure you are in the project folder, change the remote and push with these commands

    `git remote set-url origin YOUR_REPO_URL`

    `git push`

7. In Heroku, click on **Deploy** in the navigation bar
8. In the **Deployment** section, select **GitHub** as the deployment method
9. Search for your repository and click **Connect**
10. Click Deploy Branch
    * Optionally enable automatic deploys to deploy every time a the repository is updated
11. Click on **Activity** tab to see the build log
12. When build has succeeded, click on **Open App** to view the deployed site

## Credits
* [Index Background](https://7wallpapers.net/dota2-clockwerk/)
* Hero images and icons are from [Valve](https://www.valvesoftware.com/en/)
* The loading spinner is taken from [loading.io](https://loading.io/css/)
* I referred to [this](https://dev.to/techparida/how-to-deploy-a-flask-app-on-heroku-heb) on setting up Gunicorn to serve the website securely and without the 'development server' warning
* During development I constantly referred to and used code from [Flask](https://flask.palletsprojects.com/en/1.1.x/api/) and [Python](https://docs.python.org/3/) documentation

## Acknowledgements

Huge thanks to [Simen Daehlin](https://github.com/Eventyret) for being an incredible mentor and teacher, and for helping me stay on top of everything when I was struggling.

Thanks to fellow student [Stephen Seagrave](https://github.com/nemixu) for testing the deployed website and offering feedback.

[Code Institute](https://codeinstitute.net/) for this great course and network that I am grateful to be a part of.

### Disclaimer
This site is part of a course project and is intended for educational purposes only
