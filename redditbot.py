import praw
import time

def RedditLogin(Username, Password):
    '''This function takes in the user's Reddit login details and accesses their account feed. Note
    both username and password are to be entered as strings.
    '''
    reddit = praw.Reddit(client_id= "pjihl0QRm3_VZ-wPyPkX6A", client_secret = "QloyNJ1PI-GW1Mcd7KQD9HrfZi0D1Q", password= Password, user_agent= "IvanPetertheTerrible", username= Username)
    
    return reddit

def RedditPost(reddit,Subreddit, post_text):
    '''This function takes the reddit login, name of a subreddit and a text of a post as strings 
    to submit the text to a the chosen subreddit as a post.
    '''
    reddit.subreddit(Subreddit).submit(post_text, url="https://reddit.com")
    return("Posting Successful! Please check your profile to confirm the same")

def RedditComment(reddit, post_url):
    '''This function takes the url of a post as a string and prompts the user to enter a comment
    this comment will then be posted to the submission link provided
    '''
    comment = str(input("Enter comment"))
    submission = reddit.submission(url = post_url)
    submission.reply(comment)
    return("Comment submitted Successfully")

def RedditPostFind(reddit, subreddit, recency, keyword):
    '''This function takes the name of a subreddit, the recency of a post and a keyword from a user
    and browses the given subreddit for post titles including the key word. THe name and permalink
    of these posts will be returned by the function.
    '''
    for submission in reddit.subreddit(subreddit).new(limit = recency):
        title = submission.title
        if keyword in title:
            return(submission.title, submission.permalink)
