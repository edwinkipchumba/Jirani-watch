# Jirani-App

## Build by [Kolem Edwin]

## Description

This is an application like Awwards where users can signup, login and post a project to be reviewed and rated.

## Screenshot images

<img src="static../../static/img/akan%20naming.png">

<img src="static../../static/img/home2.png">

<img src="static../../static/img/home3.png">

<img src="static../../static/img/prof.png">

## Live page

<https://github.com/edwinkipchumba/Awwards-app>

## User stories

Users would like to:

1. Sign in with the application to start using.
2. Set up a profile and general loaction of neighbourhood name.
3. Find a list of different businesses in the neighborhood.
4. Find contact information for Health department and Police authorities near neighbourhood.
5. Create posts that will be visible to everyone in neighbourhood.
6. Change neighbourhood when decide to move out.
7. Only view details of a single neighbourhood.

## Behaviour Driven Development (BDD)

| Behaviour | Input | Output |
| :-----------------| :-----------------: | ------------------: |
| Admin Authentication | On demand | Access Admin dashboard |
| Admin Authentication | On demand,Verify emails before proceeding | Access Admin dashboard |
| Display all projects | Home page | Clickable links to open live projects in different sites |
| To add a project | Through Admin dashboard and homepage | Click on add and upload respectively |
| To edit project | Through Admin dashboard | Redirected to the project form details and editing happens |
| To delete the project | Through Admin dashboard | click on project object and confirm by delete button |
| To search projects by title | Enter text in search bar | Users can search by project title |
| Comment on projects | Add comments below respectively project | Users can add comments on any project |
| Vote on projects | Vote | Users can review projects they like and comment |

## Setup | Installation Requirements

1. python3.8
2. virtualenv
3. requirements.txt
4. django3.2.8

## Cloning

* Open Terminal {Ctrl+Alt+T}

```
$git clone https://github.com/edwinkipchumba/Awwards-app

```

```
$cd awwards-app
```

* open based on the text editor you have.

## Running the Application

* Creating the virtual environment

 ```
pip install virtualenv 
```

```
virtualenv venv
```

$ source venv/bin/activate

* Install Django Dependencies

```
pip install -r requirements.txt
```

## Setup Database

* setup your database User,Password, Host then make migrations

```
python manage.py makemigrations
```

## Now migrate

```
$python manage.py migrate
```

* To run the application, in your terminal:

$ python3 manage.py runserver

## Technology used

* django3.2.8 and postgresql
* HTML5
* CSS3
* Bootsrap3
* python3.8

## Known Bugs

If you find a bug, kindly feel free to comment an issue here and inlcude their corresponding results.

## Contact  Information

 Feel free to contact me incase of any issue or questions, ideas and concern towards the same.

* Contact Number:+254728357619
  
* E-Mail: edwinkolem5@gmail.com.

## License

<https://github.com/edwinkipchumba/Awwards-app/blob/master/LICENSE>










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