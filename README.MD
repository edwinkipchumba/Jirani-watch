### NEIGHBOURHOOD
This is an application that allows users in an area to interact with other people who also live in the same area. The users can look up businesses in that area and also create posts that let the other jirani know of the happenings in the nieghbourhood.

### By Emmanuel Muchiri

### Description
This is an application that allows users in an area to interact with other people who also live in the same area. Users an create posts that details what is going on within the neighbourhood and also create posts that detail businesses located in that area. Users can also find the contacts for the local police authorities and health centres.
 

|        User Requirements                 |           Input                           |           Output                         |
|------------------------------------------|-------------------------------------------|------------------------------------------|
| Sign Up/Login                            | To create a new account, click on the sign| If login is successful, the user is      |
|                                          | up link and fill in the form details. To  | redirected to the home page              |
|                                          | login, fill in the details                |                                          |
| Add a New Post                           | Click on the New Post tab on the navbar   | A new Post is created                    |
|                                          | and fill out the form                     |                                          |
| Add a New Business                       | Click on the New Business tab on the      | A new Business is added                  |
|                                          | navbar and fill out the form              |                                          |
| Create a New Profile                     | Click on the Profile tab on the navbar    | A new Profile for the user is created    |
|                                          | then click on the Edit Profile button     |                                          |
| To view All Posts                        | Navigate to the home page                 | All posts will be displayed              |
| Search For a Business                    | Enter the business name into the search   | All businesses that match the searched   |
|                                          | bar in the navbar                         | term will be displayed                   |
| Log Out                                  | Click on the Account button and select    | You will be logged out                   |
|                                          | log out                                   |                                          |


### Setup/Installation Requirements
- Ensure you have Python3.6 installed.
- Clone the Neighbourhoods directory.
- Create your own virtual environment and activate it using these respective commands `python3.6 -m venv --without-pip virtual` and  `source virtual/bin/activate`
- Install all the necessary dependencies necessary for running the application using this command `pip install -r requirements.txt`
- Open the terminal and run this command `psql` You can then create a database by running this command
`CREATE DATABASE hood`
- Run migrations using these respective commmands `python3.6 manage.py makemigrations projects` then `python3.6 manage.py migrate`
- Run the app using this command `python3.6 manage.py runserver` on the terminal.You can then open the app on your browser.


### Technologies Used
<ul>
<li>Python 3.6</li>
<li>Django</li>
<li>Heroku</li>
<li>Bootstrap</li>
<li>HTML</li>
</ul>

### Support and Contact Details
For more information, questions, or feedback, get in touch with me on email: Emmanuel.Muchiri@outlook.com

### Licence
Copyright(c) 2019 Emmanuel Muchiri