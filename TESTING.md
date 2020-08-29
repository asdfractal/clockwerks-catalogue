# Testing & Bugs

## Contents:
* Testing
    * Feature Tests
        * Authentication
    * Responsiveness
    * Browser Compatibility
    * Forward and Back button navigation
    * Code Verification
        * W3 HTML
        * W3 CSS
        * JavaScript
        * Python
    * Chrome devtools Lighthouse
* Bugs

## Testing
The whole project was testing thorougly throughout the development process using Chrome Dev Tools and personally using the features. I have ensured that I cover all requirements and expectations of the user stories, as well as adding additional functionality and user experience through testing initial implementation and improving on the experience.

### Feature Tests
---
### Authentication

#### Expectation
Users can login to store their favourites and update profile, and the website doesn't break if they try to access these pages anonymously
#### Implementation
Using Jinja template varaibles to remove certain options to anonymous users and checks in the route to ensure that even if a page is accesed by the address bar the user will be redirected with a toast message informing them
#### Test
* While not logged in -
    * Confirm the navbar is displaying a link to login and not to favourites and profile
    * In the address bar enter '/favourites/' and confirm redirect to the login page with a toast notification
    * In the address bar enter '/user/username' and confirm redirect to the login page with a toast notification
#### Result
Unregistered users are not provided with options to access areas intended for registered users, and if they access it via address bar there are systems to deal with it
#### Verdict
This test has passed


### Encrypted passwords

#### Expectation
Users passwords are stored securely to ensure the safety of their sensitive data
#### Implementation
Using Werkzeug Security `generate_password_hash` and `check_password_hash` modules, create two functions to handle passwords. When a user creates a new account, they enter the password twice, if it matches it is passed into a function to encrypt the password and store it in the database. When a user logs in their password is passed into a function to decrypt the stored password
#### Test
* Create a new user and sign up with matching passwords
* Confirm the password has been stored in the database as a binary hashed string
* Logout and login to the account with the password
* Confirm login and therefore decryption of passsword
#### Result
Passwords are securely stored and users data is not exposed
#### Verdict
This test has passed

### Hero Display and Info Card

#### Expectation
There is a display of all heroes for a user to select from, and a way to view more information
#### Implementation
A page with thumbnails of all heroes, with each thumbnail having a modal attached to it that shows a hero card with in game information, such as their roles
#### Test
* Navigate to heroes page
* Confirm all thumbnails are loaded
* Click on every thumbnail to bring up the modal
* Confirm the hero details are displayed
#### Result
Users can view a display with all heroes as well as individual hero information
#### Verdict
This test has passed

### API & Hero Filter

#### Expectation
Users can filter heroes by primary attribute to narrow their selection
#### Implementation
An API route that queries the server with the primary attribute to be filtered. With JavaScript using fetch, wait for the response and update DOM with only the matching heroes displayed
#### Test
* Using Postman, confirm the server is sending the intended response
* On the hero page, click each of the attribute buttons and confirm the expected heroes are being displayed
* Click each button on and off very fast to ensure it doesn't break
* Confirm the filter is disabled by clicking the button again
#### Result
Heroes can be filtered by their primary attribute
#### Verdict
This test has passed

### Favourites list

#### Expectation
Users can add and remove heroes to their list, and create personal notes about each hero
#### Implementation
Using the hero modal cards, users can click the heart button to add or remove a hero to their list. On their favourites page, they can also remove the hero. They can click on the hero image to show a text area under the hero and write or update their notes about the hero
#### Test
* While logged in, navigate to hero page, open a modal and click the heart, confirm hero is on my list
* Open the same hero and click the heart, confirm hero has been removed
* With at least one hero in my list, navigate to favourites page
* Click hero's name or down chevron, enter a note and click save
* Expand that hero's notes and confirm note is saved
* Change the note to something else and click save, confirm note is updated
* Expand that hero's notes and click delete, confirm note has been deleted
* Click the heart next to hero and confirm it is removed from list
#### Result
Users can add and remove heroes, and save, update, and delete personal notes
#### Verdict
This test has passed

### Profile

#### Expectation
Users can save personal info about themselves relevant to the game
#### Implementation
A profile page that users can update with stats to do with the game, such as their highest rank and primary in-game role, as well as a biography
#### Test
* While logged it, navigate to the profile page
* Click Edit, fill in the biography and make some selections from the menus, click Update
* Confirm all data is saved
* Click edit, delete biography, click Update and confirm nothing is displayed
* Click edit, enter whitespace only as biography, click Update and confirm handling of empty string because nothing is displayed
#### Result
Users can create a personal profile
#### Verdict
This test has passed

### Toast Messages

#### Expectation
Users are notified of actions or errors via a popup message
#### Implementation
Using Bootstrap Toast system and the Flask flask module, users are notified of different actions or errors across the website
#### Test
* Add a hero to list, a toast is displayed confirming
* Renove a hero from list, a toast is displayed confirming
* Try to access profile page when not logged in, a toast is displayed asking user to login or register
#### Result
Toast messages are displayed for actions and errors across the site, ensuring users have confirmation of actions and are informed about errors
#### Verdict
This test has passed

### Responsiveness

##### Expectation
The website is accessable on the majority of different screen sizes and devices
##### Implementation
Using the Bootstrap framework to develop the website means I had access to their grid system, which greatly aids in implementating responsive design. Combining this with sass mixins I was able to ensure responsiveness on all elements. I used 320px as the base size and a custom variable for 'xs' of 400px, because the gap between 320 and 'sm' of 576 is too much
##### Test
Using Chrome dev tools with iPhone 5 as the base size of 320px, and using various different screen sizes as well as responsive mode. I made sure the content was accessable and readable at all different sizes. Additionally I tested on my personal phone - Samsung Galaxy S10E
##### Result
The website is responsive and accessable on a large majority of available devices and screen sizes
##### Verdict
This test has passed

### Browser Compatibility

##### Expectation
The website displays and functions on major browsers
##### Implementation
Using modern code that is widely supported
##### Test
Aside from the development in Chrome, I tested on Firefox, Edge and Safari. I checked the usage share of browsers and found this to an acceptable coverage of approximately 93%. I repeated all the tests outlined in the other sections of this documents and there was no obvious broken functionality
##### Result
The website functions as intended on major browsers
##### Verdict
This test has passed

### Forward and Back button navigation

##### Expectation
The website is navigable using the forward and back buttons and does not break or have unintended actions
##### Implementation
Through checks in the views to redirect, prevent resubmissions, and defensive programming
##### Test
* Navigate to every page via clicking, and then navigate back and forward through all selections with back and forward buttons
* Add a hero to the list and press back, confirm hero is still on list
* Submit a hero note form and press back and forward, confirm note is there and form doesn't resubmit
##### Result
The whole website is navigable with forward and back buttons
##### Verdict
This test has passed

### Code Verification

#### [W3 HTML Validator](https://validator.w3.org/)
Using this validator I tested every page and dealt with any issues that came up. After fixing the errors the whole website validates without errors

#### [W3 CSS Validator](https://jigsaw.w3.org/css-validator/)
Using this validator I tested all the css, the only errors are from third party libraries

#### JavaScript
Using the VSCode extensions JShint and Error Lens I am notified in real time of any errors and use this system to validate the code

#### Python
Using the python packages Black, Pylint and Pylint-Django in conjunction with VScode extension Error Lens I am notified in real time of any errors and use this system to validate the code

### Chrome Dev Tools Lighthouse
I tested every page using Lighthouse and fixed any issues to do with accessibility and best practice. After fixing issues every page is receiving 95+ in accessibility. For best practices the score is lower on some pages due to the images from Valve CDN not using https.


## Bugs

### Displaying correct information on the front end

##### Bug
When a user was logged the expected data was not being correctly passed to the front end
##### Fix
In the app route functions adding checks for if a session exists and handling the data based on the result
##### Verdict
This bug was fixed and expected information is displayed

### Flashing messages with account forms

##### Bug
When a user entered an incorrect input the flashed message displayed was not the correct one for the error
##### Fix
This was fixed by making sure the code was correctly indented and line spaced for Python, and implementing an else statement
##### Verdict
This bug was fixed and the user is informed of the issue

### Displaying a border around the hero thumbnails

##### Bug
A border is displayed around the hero thumbnails on the hero page if it is on the favouritesd list, but as the images can take some time to load the border will display as a white dot on the page before the image has loaded
##### Fix
After trying a few different options and redesigning the website scheme, the border was no longer very visible on the page due to low contrast, so this was removed in favour of something more practical
##### Verdict
This bug was fixed by way of removing the feature
