from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.firefox import GeckoDriverManager
import time
from datetime import datetime
import csv


# NOTE Paste your Spotify User ID here as a string. It will be in the URL of your Spotify account after open.spotify.com/user/
user_id = "" # <- paste it in here! (between the quotations)
 
    
def is_empty_csv(name: str) -> bool:
    with open(name, encoding="utf-8") as csvfile:
        reader = csv.reader(csvfile)
        for i, _ in enumerate(reader):
            if i:
                return False
    return True

def write_to_csv(name: str, list_data: list) -> None:
     with open(name, "r+", encoding="utf-8", newline='') as file:
        writer = csv.writer(file, delimiter='␟')
        for user in list_data:
            writer.writerow([extract_true_user_id(user.get_attribute('href')), user.text])
        
def extract_true_user_id(user_url:str) -> str:
    return user_url.removeprefix('https://open.spotify.com/user/')

def read_in_csv(name: str) -> list:
    with open(name, 'r', encoding='utf-8', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter='␟')
        new_list = []
        for row in reader:
            new_list.append((row[0], row[1])) #append each {spotify...../user/example, Example69} to list
        return new_list

def retrieve_current_followers() -> list[tuple]:
    new_list = []
    for user in follower_list:
        new_list.append((extract_true_user_id(user.get_attribute('href')), user.text))
    return new_list

def write_to_log(message: str) -> None:
    with open("log.txt", "a") as f:
        f.write(f"\n{datetime.now().strftime("%d/%m/%Y %H:%M:%S")} {message}")

url = "https://open.spotify.com/user/" + user_id + "/followers"
driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()))
driver.get(url)
time.sleep(5) # gives page some time to load data. Increase this if you have errors

follower_list = driver.find_elements(By.CLASS_NAME, "Nqa6Cw3RkDMV8QnYreTr")    

if not is_empty_csv("followers.csv"): 

    print("Checking if followers have changed...")
    old_followers = read_in_csv("followers.csv")
    current_followers = retrieve_current_followers()
    
    set_old_followers = set()
    set_current_followers = set()
    for user in old_followers:
        set_old_followers.add(user[0])
    for user in current_followers:
        set_current_followers.add(user[0])

    if set_old_followers != set_current_followers: #check if any differences
        print("Follower change detected - checking for cause...") 
        gained_followers_ids = list(set_current_followers - set_old_followers)
        lost_followers_ids = list(set_old_followers - set_current_followers)
        

        for user in gained_followers_ids:
            for user_tuple in current_followers:
                if user in user_tuple:
                    log_message = f"+ {user_tuple[1]} ({user_tuple[0]}) followed you!" 
                    print(log_message)
                    write_to_log(log_message)
        
        for user in lost_followers_ids:
            for user_tuple in old_followers:
                if user in user_tuple:
                    log_message = f"- {user_tuple[1]} ({user_tuple[0]}) unfollowed you!"
                    print(log_message)
                    write_to_log(log_message)
                            
        
        f = open("followers.csv", "w") #once done, update csv accordingly
        f.truncate()
        f.close() 
        write_to_csv("followers.csv", follower_list) #follower list is just the list retrieved from spotify, so most recent data
    
    else:
        print("Followers are the same.")
    

else: #file is empty, so do first time setup (insert current followers to text file)
    write_to_csv("followers.csv", follower_list)
    print("Initial setup complete!")
    if is_empty_csv("followers.csv"):
        print("\nEither you currently have 0 followers, or you incorrectly entered your user ID. Please check that it is correct if not.")

driver.quit() 


    


    