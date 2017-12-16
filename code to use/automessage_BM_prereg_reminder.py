from twilio.rest import Client
import csv
import datetime

# put your own credentials here
account_sid = "ACe33417c9ba1a29f8ff2e00f982163279"
auth_token = "6616ea79c6f9abbd825fa9ccbe6f80d5"

# need to define: number & message
client = Client(account_sid, auth_token)

#total number of participants
count = 0

with open('number.csv') as csvfile:
    participants = csv.DictReader(csvfile)
    for participant in participants:
        message = "Thank you for registering our Think Asia Think Hong Kong symposium, with the impressive line-up of speakers, and more than 1000 guests attending the Main Symposium. Please be reminded that our afternoon thematic sessions will start from 2pm today! Thank you."
        call_action = client.messages.create(
            to="+" + participant['number'],
                from_="TATHK",
                body=message)
        count = count + 1
        print("send")
print("Total SMS sent = " + count)

