# IS211_FinalProject

README Document for IS211 Final Project 

To run flaskblog.py you will need to have installed:

						•Flask

						•flask_bootstrap

						•sqlite3

The way my flask blog works is on the route url all blog post from all users are displayed in reverse chronological order. 

When the login button is clicked on it re-directs the visitor to log in. There are only 3 users with logins currently:


		Author Name			Username		Password

	1.	Future Awad			Fawad			KidAwad
	2.	Dennis Awad			Dawad			sassmasterd
	3.	Nicole Almas			Nalmas			MrsAwad


Once a user logs in it takes them to their user dashboard where only post by the user is displayed. They can choose to edit or delete a post or add a new post. 

Should they choose to add a post they are prompted to enter a title category and blog post once they submit the post a datetime stamp is automatically applied to the post.

Should they choose the delete button the post and all its contents are removed from the data base.

If Edit is selected, they are directed to the edit url. Here the author, title Blog ID#, Content, Date time posted and category for the original post is displayed under each header along with a delete button. If delete is selected the post is only deleted and returned to the user dashboard url. However, if the user enters new content and clicks Submit Edited Post button, then the content portion of the post is updated with the entered text in the text area and a new current time stamp is reflecting the time the submit button was clicked.

Every page has the same header providing options to click the Flask Blog and your brought back to the root url. Select User dashboard and you are returned to the dashboard for the user who is currently logged in. click ad a new post will take you directly to the add post url for the user who is currently logged in. click log in and you are directed back to the log in url and prompted to log in (here you can log in as a different user, or you can still navigate elsewhere as the currently logged in user.)



