# Jirani-App

## Build by [Kolem Edwin]

## Description

This is an application that allows users in the estate to interact with other neighbours. Users can create posts details what is going on within the neighbourhood and also create posts that detail businesses located in the estate and also find the contacts for the health centres.

## Screenshot images

<img src="static../../static/img/akan%20naming.png">

<img src="static../../static/img/home2.png">

<img src="static../../static/img/home3.png">

<img src="static../../static/img/prof.png">

## Live page

https://github.com/edwinkipchumba/Jirani-watch

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
| Sign Up/Login | To create a new account,click on signup and login | Access home page on successful login |
| Add a new post | Click on the new post on navbar | Access new created post |
| Add a new business | Access created business | A new business added |
| Create a new profile | By clicking the profile tab on the navbar | A new profile for the user is created |
| To View all posts | Navigate to the home page | All posts will be displayed |
| To search for a business by title | Enter text in search bar | All business that matched the search will be displayed |
| Logout | Click on the account and select logout | You will be logged out |

## Setup | Installation Requirements

1. python3.8
2. virtualenv
3. requirements.txt
4. django3.2.8

## Cloning

* Open Terminal {Ctrl+Alt+T}

```
$git clone https://github.com/edwinkipchumba/Jirani-watch

```

```
$cd Jirani-watch
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
* Bootsrap4
* python3.8
* Heroku

## Known Bugs

If you find a bug, kindly feel free to comment an issue here and inlcude their corresponding results.

## Contact  Information

 Feel free to contact me incase of any issue or questions, ideas and concern towards the same.

* Contact Number:+254728357619
  
* E-Mail: edwinkolem5@gmail.com.

## License
https://github.com/edwinkipchumba/Jirani-watch/blob/master/LICENSE
