import os
from dotenv import load_dotenv


load_dotenv()
Email = os.environ.get("Email")
Pass = os.environ.get("Pass")


# Pick the Data Make a post and then delete that row from the databse. Do this Periodically.