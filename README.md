# IS211_FinalProject

README Document for IS211 Final Project 

To run flaskblog.py you will need to have installed:

						•Flask

						•flask_bootstrap

						•sqlite3

The way my flask blog works is when the program is first run, you are taken directly to the route url. Here my sqlite3 post.db data base is queried and retuned in descending (reverse chronological order) according to date time. This way if two post have the same date, they can reference the exact time they were posted and arrange them by newest first. Additionally, on this page is a a log in button.

When the login button is clicked, it re-directs the visitor to log in url. There are only 3 users with logins currently loaded into the post.db database. Their information is as follows:


		Author Name			Username		Password

	1.	Future Awad			Fawad			KidAwad
	2.	Dennis Awad			Dawad			sassmasterd
	3.	Nicole Almas			Nalmas			MrsAwad


Once a user logs in it takes them directly from the login url to their user dashboard, where only post by the user is displayed. They can choose the edit, delete, or add a new post button. This dashboard page query’s the data base for the users Id and blog post I’d in the published table. This table holds the association of the authors table to the blogpost table. It then returns the authors name and all the blog post associated with that author in a table with edit and delete buttons. Should they choose the delete button from this dashboard table, the associated post, and all its contents, are removed from the data base (from both the published table and blogpost tables. Should they choose to add a post they are re directed to the add post url, where they prompted to enter a title (in a text box), a category (in a text box), and blog post (in a text area). Once they submit the post, a datetime stamp is automatically applied to the post. This also adds the blog post to the blogpost table in the post.db database, with all this corresponding data. As this is done it is also automatically given a blog post Id number. Additionally, in the posts.db it receives this new blogpost Id number, links it to the author id and adds this association in the published table in post.db.

If Edit is selected, they are directed to the edit url. Here they are provided all the original blog post info in a table (author, title Blog ID#, Content, Date time posted and category) along with a delete button. If delete is selected on the edit post page it functions identically to that on the user dashboard making all the same changes to the database, and then redirect the user to the dashboard page. However, if the user enters new content in the text area box, and clicks on the Submit Edited Post button, then the content portion of the post is updated, in the blog post table, with the newly entered text. Additionally, the blog post table is also updated with the new current time stamp for date posted.

Every page has the same header, providing quick site navigation options. Click Flask Blog at the top of the page, and your brought back to the root url, where you can see all post by all users. Select User dashboard, and you are returned to the dashboard for the user who is currently logged in. Click Add A New Post, and your quickly redirected to the add post url, for the user who is currently logged in. Click Log In, and you are directed back to the log in url and prompted to log in (here you can log in as a different user, or you can still navigate elsewhere as the currently logged in user.)

