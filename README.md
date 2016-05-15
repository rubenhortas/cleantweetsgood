CleanTweetsGood
==================

WHAT IS IT?

It is a program that allows an user to remove tweets from his twitter history.

Tweets can be deleted in two ways:
    - By content: tweets are removed containing one or more words
         stored on a blacklist by the user.
    - By ID: tweets are removed from their ID.

WHAT IS *NOT*?

It's not a panic button or a magic solution.

Although tweets are deleted from the timeline, the timeline changes take time to be reflected
(You can check the history downloading it again).

Tweets deleted from the timeline may be stored in sites outside the scope of this application:
Twitter servers, screenshots ... 
When users direct messages are deleted the are *NOT* deleted from the other user account.

WHY?

Because there are countries where people can go to jail for tweeting.

Because companies and media are obsessed with social networking and some tweet last out 
context can make you infamous or can cause you to lose a possible job opportunity
or a job.


SETTINGS
    
* Log in with your account twitter: https://twitter.com

* Go to https://apps.twitter.com/

* Click on "Create New App"

* Fill the form:
    Name: CleanTweetsGood
    Description: Twitter cleaner
    Website: https://github.com/rubenhortas/cleantweetsgood
    Callback URL: Leave blank

* Accept the Developer Agreement

* Go to "Access Keys and Tokens" tab
    Get the tokens: Key Consumer, Consumer secret, Access Token and Access Token Secret
    Set the tokens in the configuration.py file

* Go to "Permissions" tab
    Change permissions from "Access" to "Read, Write and Access direct messages"

* Click on "Update settings"
    
    
REQUIREMENTS

* tweepy

* Download the history of twitter from: https://twitter.com/settings/your_twitter_data

* Storing the history of twitter in the root directory of the application with the name: tweets.csv

USE:

Use: cleantweetsgood.py [-h] [-t] [-log] [-BL] [-dm] [-u USER [USER ...]]
                        [-id ID [ID ...]]

Clean your twitter account

optional arguments:
    -h, --help            show this help message and exit
    -t, --test            Run a single test showing the expected output
    -log, --log           Saves the output into a plain text file
    -bl, --blacklist      Deletes the tweets that contain blacklisted words
    -dm, --direct_messages
                          Deletes *ALL* the direct messages
    -u USER [USER ...], --unfollow USER [USER ...]
                          Users to unfollow
    -id ID [ID ...]       Tweet IDs to delete


AUTHOR

Ruben Hortas
Contact: rubenhortas at gmail.com
Website: http://www.rubenhortas.blogspot.com.es

LICENSE

CC BY-NC-SA 3.0
http://creativecommons.org/licenses/by-nc-sa/3.0/

CONTACT

If you have problems, questions, ideas or suggestions you can
contribute with this little project on github repository:

https://github.com/rubenhortas/CleanTweetsGood

WEBSITE

Visit the project site on GitHub to see the latest news and downloads:

https://github.com/rubenhortas/CleanTweetsGood
