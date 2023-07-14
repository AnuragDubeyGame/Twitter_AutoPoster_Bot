import os
import json
import time
import random
import datetime
import requests
from dotenv import load_dotenv


load_dotenv()
EmailAdd = os.environ.get("Email")
PassWord = os.environ.get("Pass")
DBurl = "https://ap-south-1.aws.data.mongodb-api.com/app/data-uchvr/endpoint/data/v1/action/findOne"


def Post():
    # FETCH FACTS

    payload = json.dumps({
    "collection": "factsCollection",
    "database": "FactsDB",
    "dataSource": "FACTSDATABASECLUSTER",
    "projection": {
        "_id": 0
    }})
    headers = {
    'Content-Type': 'application/json',
    'Access-Control-Request-Headers': '*',
    'api-key': os.environ.get("DBAPI"),
    }
    response = requests.request("POST", DBurl, headers=headers, data=payload)
    print("\t\t RESPONSE : ",response.text)

    print("\t\t\t !!! Posting a Tweet !!!")

def main():
    # Set the start and end time for posting
    start_time = datetime.time(8, 0, 0)  # 8:00 AM
    end_time = datetime.time(23, 59, 0)  # 11:00 PM

    # Set the minimum and maximum duration between each post
    min_duration = 1 * 60 # Minimum duration in mins
    max_duration = 2 * 60 # Maximum duration in mins

    # Set the number of times to post in a day
    min_posts = 10  # Minimum number of posts
    max_posts = 15  # Maximum number of posts

    # Get the current time
    current_time = datetime.datetime.now().time()

    # Check if the current time is within the posting time range
    while start_time <= current_time <= end_time:
        # Generate a random number of posts for the day
        num_posts = random.randint(min_posts, max_posts)
        print("\t\t WE WILL BE TWEETING ",num_posts," TWEETS TODAY!")

        # Generate random post times within the posting time range
        for _ in range(num_posts):
            Post()
            duration = random.randint(min_duration, max_duration)
            print("\t\t WE WILL WAIT FOR ",duration / 60," MINUTES BEFORE NEXT TWEET!")
            time.sleep(duration)


        current_time = datetime.datetime.now().time()

        print("\t\t TIME OVER! WE WILL START TOMORROW AGAIN!")
        sleep_time = datetime.datetime.combine(datetime.date.today() + datetime.timedelta(days=1), start_time) - datetime.datetime.now()
        time.sleep(sleep_time.total_seconds())

main()
