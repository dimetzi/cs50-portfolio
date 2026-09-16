# IMDB
#### Video Demo:  <URL https://www.youtube.com/watch?v=aFJuAS5_I8k>
#### Description:
Starting with app.py , we have the register route which makes sure a user can register in my web-app and the user needs to co-operate when entering password.The password needs to be at least 8 chars long , contain 1 number and 1 symbol to be accepted. If the password is accepted, the username and password are saved in a database with SQL, and I genarate hash for password so it's cryptic. If the user goes to /register via GET he will see the register.html template which is the input boxes and the button for the register.

Then there is the login and logout routes respectively. The login route clears the session at the start to make sure we get a fresh id with the next login, and after some checking on the users' inputs it will search on the database for the users' username and password. If the username and password are valid and there is a user with those, then it will log the user in my web-app. If the user goes in login route via GET he will see the login.html template which is the input boxes and the button for the login. Then we have the logout route, which makes sure to clear the session and forget the user, after the user logs out.

On helpers.py there is the login_required function, which allows me to limit some route to be accessed only if you are logged in. Also on helpers.py we have the lookup(title) function , which takes an argument (title) and when called from the quote function it sends an API request to get the API's data through response.json(). And lastly we have the apology function, which helps to hit the user with some errors, returning on the apology.html template.

Then we have the quote route. If the user gets there via GET he will see an input and a button for search. The user needs to type the title of the movie on the input searchbar and then click the quote button. After the search is done , the user will see the quoted.html which are the movies, relevant to the user's search, getting them with an API request. The user will see in quoted.html every movie (image_poster, title, actors) relevant to the search (max 8 movies, cause of the API limit), and then there is some javascript implemented to create a button which allows the user to add a movie to his favorites. This is being done by fetching to the /add-to-favorites route and by requesting json and also inserting the data to my SQL database. Then the user can go to /favorites route and see all the favorite movies he has stored through the favorites.html template, which is a table with information of the movies.

On index.html the user gets 4 random movies from the already favorited movies, and they change on each refresh. If he has less than 4 movies favorited he will get that number of movies. I initially wanted random movies from the API to show up on index, so they would be totally random, but after a bit of search I realized that the API does not have that feature, so I adjusted and made 4 random movies from the users' favorites to show up, namely from the SQL database.

Then we have the layout.html which is the default layout for all the templates, and we add the rest of the templates with the {% block main %} {% endblock %} so all templates are on a different file and can be worked seperately.

We also have the /static file and there we have some images and some css on the /static/styless.css.

Then there is the flask_session file which stores the sessions of the flask runs.

Lastly we have the project.db file which is the SQL database, which has 2 tables , 1 for users and 1 for movies. So we are able to store each user and then store each user's favorite movie in the database.