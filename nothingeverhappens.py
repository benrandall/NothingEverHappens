# Copyright 2017, Benjamin Randall

#   This program is free software: you can redistribute it and/or modify
#   it under the terms of the GNU General Public License as published by
#   the Free Software Foundation, either version 3 of the License, or
#   (at your option) any later version.

#   This program is distributed in the hope that it will be useful,
#   but WITHOUT ANY WARRANTY; without even the implied warranty of
#   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#   GNU General Public License for more details.

#   You should have received a copy of the GNU General Public License
#   along with this program.  If not, see <http://www.gnu.org/licenses/>.

import praw            # For reddit API
import time            # For sleep function
import sys             # For stderr message output
import configparser    # For reading ini file for authentication

# Read the config file
config = configparser.ConfigParser()
config.read('authentication.ini')
USERNAME = config.get('nothingeverhappensbot', 'username')
PASSWORD = config.get('nothingeverhappensbot', 'password')
CLIENTID = config.get('nothingeverhappensbot', 'client_id')
SECRET = config.get('nothingeverhappensbot', 'client_secret')
USER_AGENT = config.get('nothingeverhappensbot', 'user_agent')

def main():

	# Initialize Reddit instance
    bot = praw.Reddit(user_agent=USER_AGENT,
                      client_id=CLIENTID,
                      client_secret=SECRET,
                      username=USERNAME,
                      password=PASSWORD)
    print("Logged in.", file=sys.stderr)

    subreddit = bot.subreddit('all')
    comments = subreddit.stream.comments()

    message = "/r/nothingeverhappens"
    key_phrases = ("r/thathappened", "/r/thathappened")

    # Infinitely loop through new comments
    for comment in comments:
        text = comment.body # Fetch body
        for phrase in key_phrases:
            if phrase == text.lower():
                print("Found key phrase.", file=sys.stderr)
                comment.reply(message) # Post message
                print("Posted comment.", file=sys.stderr)
                time.sleep(5) # Sleep for 5 seconds

main()