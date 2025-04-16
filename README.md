
# Url-Shortener

An easy-to-use web-service to create short and convenient links for display in apps and chats. 

Provides both a browsable webpage and a REST API for external projects' integration.

Built with Django and Django REST Framework, PostgreSQL, designed with Bootstrap5.

## Features

  - register and login to shorten a URL and save it for future usage;
  - check the list of your previously saved URLS;
  - connect to the API with GET/POST requests to check the reqistered users, your saved URLs or to get a new shortened URL.

## Installation

This project is built using Django and DRF as the main frameworks. Please refer to the pyproject.toml file for the full list of required dependencies.

1) Download the package from GitHub:

`git clone git@github.com:Mirrasol/Url-Shortener.git`

2) Install using uv from your console:

`make install`

or set your own virtual environment using pip and other package managers.

3) Don't for get to create the .env file that contains your secret keys and database settings. 

Use .env_example for reference.

4) Run the project using the standard Django command:

`python urlshortener/manage.py runserver`

or check Makefile for the rest of the available commands.

## Demo Screens

-  Browse homepage:

![](/img/1.homepage.png)

-  Registering new user:

![](/img/2.sign_up.png.png)

-  Login afterwards:

![](/img/3.login.png)

-  Check the list of previously saved URLs:

![](/img/4.urls_index.png)

-  Or get a new short link:

![](/img/5.shorten_urls.png)

-  Get a list of registered users through an API request:

![](/img/6.api_users_index.png)

-  Get a list of your saved URLs:

![](/img/7.api_urls_index.png)