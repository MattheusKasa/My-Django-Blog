# [MATTHEUS BLOG](https://my-django-blog-mattheus.herokuapp.com/)

## Welcome

### Mattheus Blog is a website for viewing and commenting different blogposts.


---
## Table of Contents
1. [**UX**](#ux)
    - [**User Stories**](#user-stories)
    - [**Design**](#design)
    - [**Typography/Color Scheme**](#typographycolor-scheme)
    - [**Wireframes**](#wireframes)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features Left to Implement**](#features-not-yet-implemented)

3. [**Used Programs**](#used-programs)
    - [**Backend**](#backend)
    - [**Frontend**](#frontend)

4. [**Compatability**](#compatibility)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)
---
## UX

This is my fourth project in my journey to becoming a software developer. I have chosen to create 'Mattheus Blog", a blog where you can read interesting posts.

## User Stories

As a site user i want to be able to:

- Register as a user
- Login to the blog
- Logout of the blog
- Change my password
- View posts
- Comment posts

#### Framework

- [Django](https://www.djangoproject.com/)
    - Django is a high-level Python web framework that encourages rapid development and clean, pragmatic design.

#### Typography/Color Scheme

Font used on the site are the google font [Roboto](https://fonts.google.com/specimen/Roboto). I chose to keep the color scheme light and easy with different shades of blue for the banners and buttons. The buttons for user management i chose to style grey.

### Wireframes

[Balsamic Wireframes](https://balsamiq.com/)
    - I used this to create all the wireframes for this project

<p>&nbsp;</p>

---

## Features

### Existing Features

**Status-Dependant Navbar**

Options for the user changes depending on if user is logged in or not
- Users that are **NOT** logged in will be able to:
    - Login
    - Register
- Users that **ARE** logged in will be able to:
    - Logout
    - Change Password
    - See Posts
    - Comment Posts

<p>&nbsp;</p>

**Register**

Users are able to create their own accounts. The website makes sure that each username is unique and that the password meets all of the requirements.

**Login**

Users are able to login to their accounts. The website makes sure that the username typed in is in the database, and that the password is correct.

**Logout**

Users are able to logout of their accounts and are then redirected to a prompt to login again.

**Change Password**

Users are able to change their password. They are presented with a form asking for their old password and their new password, aswell as confirming the new one. After they are shown a prompt saying their password has been changed and a button directing them to the home page.

**Posts**

Users are able to view posts.

**Comment**

Users are able to comment on posts. They are asked to fill out a form with their name, email and comment. After they are returned to the post with a message saying that their comment is awaiting moderation.

**Pagination**

Three posts are displayed on each page to not make the page too flooded with information. Pagination has been added so that the user can easily move through all of the posts.

### Features not yet implemented

**Edit Comment**

Users should be able to edit their comments after they're posted.

**Delete Account**

Users should be able to delete their accounts.

<p>&nbsp;</p>

---

## Used Programs
- [Gitpod](https://www.gitpod.io/) - An open-source developer platform for remote development used for this project.
- [Github](https://github.com/) -  A code hosting platform also used in this project

### Backend

- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for hosting this website
- **Python**
    - [Python 3.8.11](https://www.python.org/) - Python is an interpreted, high-level, general-purpose programming language and is the language used for all backend functions of this project.
- **Django**
    - [Django 4.1.2](https://www.djangoproject.com/) - Django is a high-level Python Web framework that encourages rapid development and clean, pragmatic design.
- **Gunicorn**
    - [Gunicorn 20.1.0](https://gunicorn.org/) - Gunicorn is a Python WSGI HTTP Server for UNIX.

### Frontend

- **HTML**
    - [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - The fundamental code structure for all webpages.
- **CSS**
    - [CSS](https://sv.wikipedia.org/wiki/Cascading_Style_Sheets) - A style sheet language used for describing the presentation of a document written in a markup language such as HTML.

    <p>&nbsp;</p>

---

## Compatibility

The website was tested for full usability across the following browsers:

- Chrome
- Firefox
- Safari
- Samsung Internet Browser

<p>&nbsp;</p>

---

## Deployment

To deploy this project to Heroku you must do the following:

1. Create a **requirements.txt** file for heroku to install the requirements for the website.

2. Create a **Procfile** for Heroku to know what type of application to run and how to run it.

3. Log in to Heroku then create your new app. Click on **Deploy** then scroll down to deployment method. Select **GitHub** as deployment method, scroll down and choose branch then click on **Deploy Branch**. You can also choose to **Enable Automatic Deploys**, which will update your app on heroku everyone you update it on your github pages.

<p>&nbsp;</p>

---

## Credits 

- Countless YouTube videos for inspiration
