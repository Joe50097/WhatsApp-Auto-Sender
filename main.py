# Important Note: Make sure you are logged into WhatsApp Web on your default browser before running this script.
import pywhatkit as pwk
from dotenv import load_dotenv
import os

# load environment variables from the .env file
load_dotenv()

# get the phone number and message from environment variables
phone_number = os.getenv("PHONE_NUMBER")
message = os.getenv("MESSAGE")

# send the message instantly via WhatsApp Web and wait for 10 seconds before closing the tab
pwk.sendwhatmsg_instantly(phone_number, message, wait_time=10, tab_close=True)

# send a confirmation message to the console
print("message sent successfully!")