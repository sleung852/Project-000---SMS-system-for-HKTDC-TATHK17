from twilio.rest import Client
import csv

# put your own credentials here
account_sid = "ACe33417c9ba1a29f8ff2e00f982163279"
auth_token = "6616ea79c6f9abbd825fa9ccbe6f80d5"

# need to define: number & message
client = Client(account_sid, auth_token)

message = "**Think Asia Think Hong Kong** Hello."
call_action = client.messages.create(
        to="+85256141474",
        from_="TATHK",
        body=message)
