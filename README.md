# Clockwerk's Catalogue

A small web app designed to allow users to create a list of their favourite heroes from the game 'DOTA 2'.

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

### User Requirements and Expectations
#### Requirements
* Easy to use and navigate the website
* Create an account and view list
* Create a list of heroes
#### Expectations
* User information is protected
* Website load times are sufficient

## Design Choices
The design of the website is influenced by the target audience as well as the official DOTA 2 website and in game UI. To achieve this I have chosen the [Slate](https://bootswatch.com/slate/) theme from Bootswatch, which I will use as a base and build upon with my own accents.

### Colours

#### Additional Colours
I used the 'DOTA 2 Red' colour in a complimentary colour tool to find the 'Harvest Gold' colour. Then using [coolers.co](https://coolors.co/) I entered the two colours and generated the rest
* #9E2F19 Dota 2 Red - This is the colour used in the DOTA 2 logo. It is used as the primary accent colour on the website
* #D7920A Harvest Gold - A complimentary gold colour, used to signify a hero is on the user's favourites list
* #9E829C Mountbatten Pink - A pleasant colour that stands out against the background, used for the sign up button to draw attention
#F0EFF4 Ghost White - Slightly off white used in place of white

### Fonts
* Display Font 'Audiowide' - I found  this modern looking display font on [Google Fonts](https://fonts.google.com/), which I think looks very good for the purpose of this website
* Body Font 'Lato' - Using the popular pairings section of Google Fonts I chose Lato, an easy to read san serif font

### Images
The background image on the home page is a hero from the game - Clockwerk - which the website is named after. The image thumbnails and full size portraits on the modals are official DOTA 2 images from the Valve CDN. The logo is an image I made by combining an icon of Clockwerk and two of the letter C.

### CSS
* I have chosen to use the [BEM](http://getbem.com/) naming convention for my CSS classes. I like the way this reads and allows for descriptive naming for ease of use

Note on CSS: I have chosen to use vw/vh on padding and margins in a lot of cases as I believe this allows for an even more responsive experience than using solely rem. My decision was influenced by my own experimentation as well as researching, particularly [this](https://www.elegantthemes.com/blog/divi-resources/better-mobile-website-design-how-to-use-vw-vh-and-rem-to-create-fluid-divi-pages) article.

## Wireframes
I created the wireframes using Balsamiq Wireframes. I made both desktop and mobile/tablet wireframes to have a blueprint for different devices users might access the website on. This helped to build a working website in a short time, and then adjust based on further testing to reach the final product.

View the wireframes for this project [here](./wireframes).

### Information Architechture

I created data schemas for the following collections in the database for this project. View them [here](./data/schemas).

**Users Collection**
**Title**|**Key in Collection**|**Data Type**
:-----:|:-----:|:-----:
User ID|_id|ObjectId
Name|name|String
Password|password|Binary
Favourites|favourites|Object

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

The hero id property corresponds to the in game id of the hero and is used for administrative purposes.

## Features
### Implemented Features
* Create account, login and logout
* Dynamically changing user interaction options based on if they are logged in or not
* Displaying a list of heroes with a additional information on a popup modal
* A favourite heroes list, which the user can modify from the hero page or a separate page displaying their list
* If the hero is on the user's list, a white border will display on the heroes page

### Planned Features
* Account deletion option
* Flash/popup messages to confirm list has been modified

## Technologies Used
### Languages
* [HTML](https://www.w3schools.com/html/)
* [CSS](https://www.w3schools.com/css/)
* [JavaScript](https://www.w3schools.com/js/)
* [JSON](https://www.json.org/json-en.html)
* [Python](https://www.python.org/)

### Tools and Libraries
* [Bootstrap](https://getbootstrap.com)
* [Bootswatch](https://bootswatch.com/)
* [JQuery](https://jquery.com)
* [Popper.JS](https://popper.js.org/)
* [Font Awesome](https://fontawesome.com/)
* [Google Fonts](https://fonts.google.com)
* [Git](https://git-scm.com/)
* [Flask](https://flask.palletsprojects.com/en/1.1.x/)
* [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
* [Flask PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
* [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)
* [Werkzeug](https://werkzeug.palletsprojects.com/en/1.0.x/)
* [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/)

### Resources
* [Stack Overflow](https://stackoverflow.com)
* [MDN](https://developer.mozilla.org/en-US/)
* [w3 Schools](https://www.w3schools.com/)
* [Favicon Generator](https://www.favicon-generator.org/)
* [Python Programming](https://pythonprogramming.net/)
* [Miguel Grinberg's blog](https://blog.miguelgrinberg.com/)

## Testing

#### Design -
* <strong>Plan:</strong> Taking inspiration from the DOTA 2 user interface to create a website that is familiar for users
* <strong>Implementation:</strong> The Bootswatch theme 'Slate' has a very similar look, with the shades of gunmetal grey, and the other chosen colours stand out very well
* <strong>Test:</strong> To test this I compared it to the DOTA 2 website and in game UI
* <strong>Result:</strong> After implementing this theme and using the coolers.co tool to create complimentary colours, a DOTA 2 inspired page is the clear end result
* <strong>Verdict:</strong> This test has passed and the theme of the website fits the purpose

#### Navigation -
* <strong>Plan:</strong> A website that is easy to navigate to the desired page and interact with intuitively
* <strong>Implementation:</strong> A navbar with relevant links is always present on the header, with dynamically changing options if a user is signed in. The same on the index page buttons, with the right one changing from a sign in to a favourites button upon sign in
* <strong>Test:</strong> To test this I navigated around the website and used all the different functionality
* <strong>Result:</strong> The interace is simple and easy to use, it is clear how to get to where you want to go
* <strong>Verdict:</strong> This test has passed and the website is easy to navigate

#### Create and login to an account -
* <strong>Plan:</strong> Functionality for users to create an account and login to it
* <strong>Implementation:</strong> Originally checked documentation on flask-login, but found it not to be what I wanted. I opted for using the session module of Flask and writing the funcitonality into the app route function of the code. This code checks if the user exists and if the password is correct and then moves on. If there is an error it flashes a message on the form component informing the user, if everything is fine it will create an account or login to an existing one
* <strong>Test:</strong> To test this I tried many combinations. I created test accounts, tried to create an account with duplicate name, tried to create an account with passwords that didn't match, tried to login with an account that didn't exist, logged in with an incorrect password. I implemented message flashing based on the action taken
* <strong>Result:</strong> The user can create and login to an account easily
* <strong>Verdict:</strong> This test has passed and users can create and login to an account

#### Encrypt the user password -
* <strong>Plan:</strong> To store users sensitive information in a secure way
* <strong>Implementation:</strong> Using Werkzeug which comes with flask, I imported the security module and used the encrypting and decrypting functionality
* <strong>Test:</strong> I created test accounts and using the print function in python output the resulting hashed string to check it was working, and also using mongodb checked my database for the password entry to confirm it had saved the correct information
* <strong>Result:</strong> The users password is encrypted upon account creation and stored in the database only as the hashed version, not storing the original password
* <strong>Verdict:</strong> This test has passed and the users password is encrypted

#### Adding and removing from favourites list
* <strong>Plan:</strong> To allow users to add and remove a hero from their personal list
* <strong>Implementation:</strong> As there are many heroes in DOTA 2, I wanted a way to show the information in a concise yet easy to access way. The hero page has thumbnails of all the heroes, and when you click one it will bring up a modal with more information. This modal allows a user to add or remove a hero from their list. They can also remove a hero from their list in the list view
* <strong>Test:</strong> To test this I used the test accounts and tried adding and deleting from the places it is possible
* <strong>Result:</strong> The buttons to add and delete from list work and display the result
* <strong>Verdict:</strong> This test has passed and the user can add and remove heroes from their list

## Bugs

#### Displaying correct information on the front end
* <strong>Bug:</strong> When a user was logged the expected data was not being correctly passed to the front end
* <strong>Fix:</strong> In the app route functions adding checks for if a session exists and handling the data based on the result
* <strong>Verdict:</strong> This bug was fixed and expected information is displayed

#### Flashing messages with account forms
* <strong>Bug:</strong> When a user entered an incorrect input the flashed message would not display correctly
* <strong>Fix:</strong> This was fixed by making sure the code was correctly indented and line spaced for Python, and implementing an else statement
* <strong>Verdict:</strong> This bug was fixed and the user is informed of the issue

#### Displaying a border around the hero thumbnails
* <strong>Bug:</strong> A border is displayed around the hero thumbnails on the hero page if it is on the favouritesd list, but as the images can take some time to load the border will display as a white dot on the page before the image has loaded
* <strong>Fix:</strong>
* <strong>Verdict:</strong>

## Deployment
I developed this project using Visual Studio Code, using git for version control and GitHub to host the repository. The live version of the website is hosted on Heroku. I use a tool called [Pipenv](https://pipenv-fork.readthedocs.io/en/latest/) for the handling of the virtual environment and requirements. This essentially functions like npm and replaces the requirements.txt file. The following steps assume VSCode and Pipenv, however a requirements.txt file is present should you need that option.

A <a href="https://www.mongodb.com/">MongoDB</a> account is necessary to create the database.

### Steps to deploy
#### Cloning the repository
* Clone the repository by either downloading from [here](https://github.com/asdfractal/clockwerks-catalogue) or in the terminal by typing:
```
git clone https://github.com/asdfractal/clockwerks-catalogue.git
```
* Navigate to this folder in the terminal and type:
```
pipenv install
```


#### Deploying on Heroku


## Credits

