
# spotiFollowers

A Python program which detects and alerts you of people following/unfollowing your Spotify account. Useful for if you notice a difference in your follower count, but can't figure out who caused it.

## Installation

1. Clone the repo to your computer & open the project directory in your IDE of choice.
2. Obtain your Spotify user ID. This can be found by navigating to your Spotify profile page on the desktop app, click ••• and 'Copy link to profile'. Paste this somewhere and copy the part AFTER user/, and before the question mark if there is one. 
For example, my generated profile link is
```
https://open.spotify.com/user/fz8360fhwzmnpp9zc3jyjfw2n?si=748c8d9e17364e79
```
The part you want is just:

```
fz8360fhwzmnpp9zc3jyjfw2n
```
If you are still confused, using the link you have navigate to your profile in a browser, click on 'Followers', and the user ID will be between 'user' and 'followers' in the URL. E.g:
```
https://open.spotify.com/user/EXAMPLE ID HERE/followers
```
3. Install libraries from the requirements.txt. You can do this with 
```
pip install -r requirements.txt
``` 
If you don't have pip installed, do that first. You can find a tutorial online if you need help with this step.

4. Run the script.py python file to initialise your follower count on your local machine.
5. The program should work now! So now whenever you notice a change in your follower count, you can run it, and the cause of the change will be displayed as output, as well as written to the log.txt file within the directory of the project.
## Notes

- This program uses Selenium, with geckodriver. You will need firefox installed on your computer for it to work.
- Follower change can only be detected after the program has been run once to initialise it.
