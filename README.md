# Mattheus Travels

## Welcome to Mattheus Travels!

### Here you can join me on my adventures around the world, as I share my experiences through stunning images and short snippets of my travels.

Here's a link to the live website: https://my-django-blog-mattheus.herokuapp.com/

---
## Table of Contents
1. [**UX**](#user-experience)
    - [**User Stories**](#user-stories)
    - [**Typography/Color Scheme**](#typographycolor-scheme)
    - [**Wireframe**](#wireframe)

2. [**Features**](#features)
    - [**Existing Features**](#existing-features)
    - [**Features not yet implemented**](#features-not-yet-implemented)

3. [**Used Programs**](#used-programs)

4. [**Testing**](#testing)

5. [**Deployment**](#deployment)

6. [**Credits**](#credits)

------

## User Experience, UX

Those visiting Mattheus Travels are people who enjoy traveling or are interested in learning about new places and cultures.

-----

## User Stories

## As a site user i want to be able to:

## Account

- As a Site User I can register an account
- As a registered Site User I can login to my account
- As a registered Site User I can logout of my account
- As a registered Site User I can change my password
- As a registered Site User I can delete my account

## Interaction
- As a non registered Site User I can view a list of posts
- As a Site User I can view a paginated list of posts
- As a registered Site User I can click on a post so that i can read the full text
- As a registered Site User I can view comments on posts
- As a registered Site User I can leave comments on a post
- As a registered Site User I can edit my comments
- As a registered Site User I can delete my comments
- As a registered Site user I can like a post
- As a registered Site User I can unlike a post

## As a site admin i want to be able to:
- As a Site Admin I can leave comments on a posts through the admin page.
- As a Site Admin I can create, read, update and delete posts so that I can manage my blog content
- As a site Admin i can create drafts posts so that i can finish writing the content later
- As a site Admin I can edit everyones comments through the admin page.
- As a site Admin I can delete everyones comments through the admin page.


<p>&nbsp;</p>


#### Typography/Color Scheme

Fonts used on the site are the google fonts [Roboto](https://fonts.google.com/specimen/Roboto) and [Alkatra](https://fonts.google.com/specimen/Alkatra?query=Alkatra). I choose to keep the color scheme light and easy with a mix of white, lightgrey, black and peach.

<p>&nbsp;</p>

### Wireframe

- I used [Balsamic-Wireframes](https://balsamiq.com/) to plan out my project, designing the style that I aimed for.
- This is what the initial mockup design looked like:

    ![Wireframe](assets/images/wireframe.png)


<p>&nbsp;</p>

---

# Features

<p>&nbsp;</p>

## Existing Features

<p>&nbsp;</p>


- ### Users that are **NOT** logged in will be able to:
    - Register
    - Login
- ### Users that **ARE** logged in will be able to:
    - View Posts
    - Like Posts
    - Create Comments
    - Delete Comments
    - Edit Comments
    - Change Password
    - Logout
    - Delete Account
- ### Admins are able to:
    - View Posts
    - Create Posts
    - Delete Posts
    - Edit Posts
    - Create Comments
    - Delete Comments
    - Edit Comments
    - Create Users
    - Delete Users
    - Edit Users Info

<p>&nbsp;</p>

- **Status-Dependant Navbar**

    - Navbar changes depending on if the user is logged in or not.

- **Register**

    - Users are able to create their own accounts. The website makes sure that each username is unique and that the password meets all of the requirements.

- **Login**

    - Users are able to login to their accounts. The website makes sure that the username typed in is in the database, and that the password is correct.

- **Logout**

    - Users are able to logout of their accounts and are then redirected to a prompt to login again.

- **Change Password**

    - Users are able to change their password. They are presented with a form asking for their old password and their new password, aswell as confirming the new one. After they are shown a prompt saying their password has been changed and a button directing them to the home page.

- **Posts**

    - Users are able to view posts.

- **Comment**

    - Users are able to comment on posts. They are also able to edit their comments and delete them.

- **Like**

    - Users are able to like/unlike posts.


- **Pagination**

    - Three posts are displayed on each page to not make the page too flooded with information. Pagination has been added so that the user can easily move through all of the posts.

<p>&nbsp;</p>

## Features not yet implemented

<p>&nbsp;</p>

- **Search Function**

    - Users will be able to search for specific posts.

- **Dark Mode**

    - Users will be able to toggle between light and dark mode.

<p>&nbsp;</p>

---

## Used Programs
- [Gitpod](https://www.gitpod.io/) - An open-source developer platform for remote development used for this project.
- [Github](https://github.com/) -  A code hosting platform also used in this project
- [Git](https://git-scm.com/) - For version control.
- [Django](https://www.djangoproject.com/) - I utilized Django to develop this project, a framework based on Python.
- [Bootstrap](https://getbootstrap.com/) - For HTML design templates.
- [Balsamiq](https://balsamiq.com/) - For Wireframes.
- [Heroku](https://www.heroku.com) - Used for hosting this website
- [Python](https://www.python.org/) - The language used for all backend functions of this project.
- [Gunicorn 20.1.0](https://gunicorn.org/) - Web Server Gateway Interface used in this project.
- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - The fundamental code structure for all webpages.
- [CSS](https://sv.wikipedia.org/wiki/Cascading_Style_Sheets) - A language for describing document presentation in markup languages like HTML.
- [W3C](https://www.w3.org/) - For HTML and CSS validation
- [Pep8CI](https://pep8ci.herokuapp.com/) - For Python validation

    <p>&nbsp;</p>

---

## Testing

- Testing and results can be found [here](TESTING.md)

---

## Create Repository

The project was deployed using both Heroku and GitHub. The following steps were taken to create the project with GitHub:

1. Logged into GitHub.
2. Navigated to the 'repositories' section.
3. Clicked the 'new' button to create a new repository page.
4. Selected the CodeInstitute template from the dropdown menu.
5. Assigned a title to my project and clicked 'create repository'.
6. Once the repository was created, I opened it and clicked the green 'GitPod' button to set up my workspace.


---

## Deployment

### To deploy the project with Heroku, follow these steps:

1. Log in to Heroku.
2. From the main Heroku dashboard, select 'new' and 'create new app'.
3. Choose a unique name for your project and select a suitable region. Click 'create app' to create the app in Heroku.
4. From the 'deploy' tab, navigate to the 'resources' tab in the menu at the top.
5. Add the Heroku Postgres database to your app by going to the add-ons section and searching for 'Heroku Postgres'. Select the package that appears and add it to the database.
6. In the settings, under 'config vars', add the DATABASE_URL to the clipboard for the Django config.
7. Create a new file called env.py in GitPod, set your environment table for the DATABASE_URL, and paste in the copied address from Heroku.
8. Add 'KEY - DISABLE_COLLECTSTATIC' with the value of 1 to the config vars in Heroku. This line must be removed before final deployment of the project.
9. Add the STATIC files to your settings.py file, including the url, storage path, directory path, root path, media url, and the default file storage path.
10. Link this to the templates directory in Heroku with 'TEMPLATES_DIR = os.path.join(BASE_DIR, 'templates')'.
11. Add new folders in GitPod for media, static, and templates, and create a file at the top level named Procfile (note the capital P).
12. In the Procfile, add the following line: web: guincorn "NAME OF YOUR PROJECT".wsgi.
13. Commit and push these changes to GitHub.
14. In Heroku, go to the deployment tab and manually deploy this branch. Heroku will build the app, and you will be able to follow the build process in the window.
15. When the deployment is successful, you will see the message "Your app was successfully deployed".

<p>&nbsp;</p>

---

## Credits 

- Font awesome for fonts.
- Code with Stein on Youtube.
- Code institute Slack Channel
- Countless other YouTube videos for inspiration