from twilio.rest import Client
import csv

# put your own credentials here
account_sid = "ACe33417c9ba1a29f8ff2e00f982163279"
auth_token = "6616ea79c6f9abbd825fa9ccbe6f80d5"

# need to define: number & message
client = Client(account_sid, auth_token)

error_list = []

#total number of participants
count = 0
total = 1200

with open('contact.csv') as csvfile:
        participants = csv.DictReader(csvfile)
        for participant in participants:
                try:
                        message = "*Greetings from Think Asia Think Hong Kong* Hi %s! We look forward to seeing you at 8:30am in the QEII Centre. Thank you. HKTDC - Andrew" %participant['name']
                        call_action = client.messages.create(
                                to="+" + participant['telephone'],
                                from_="TATHK",
                                body=message)
                        count += 1
                        print("Percentage Done: " + (count + error)*100/total + "%")
                except ValueError:
                        error += 1
                        error_list.append(participant["name"])
                    
print("Total Attempt= " + count + error)
print("Total Success = " + count)
print("Total Error = " + error)

