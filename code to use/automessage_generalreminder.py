from twilio.rest import Client
import csv

# login details
account_sid = "" #enter ID here
auth_token = "" #enter PW here

# need to define: number & message
client = Client(account_sid, auth_token)

#total number of participants
count = 0

with open('contact.csv') as csvfile:
        participants = csv.DictReader(csvfile)
        for participant in participants:
                try:
                        if participant['country']=='HK':
                                message = "**Think Asia Think Hong Kong** Hello %s ! We are excited to see you tomorrow! Please remember to bring your confirmation email tomorrow. Thanks! HKTDC - See **auto-message. please do not reply to this text message**" %participant['name']
                                call_action = client.messages.create(
                                        to="+" + participant['telephone'],
                                        from_="+85264522974", #from your purchased phone number
                                        body=message)
                                count += 1
                        elif participant['country']=='UK':
                                message = "**Think Asia Think Hong Kong** Hello %s ! We are excited to see you tomorrow! Please remember to bring your confirmation email tomorrow. Thanks! HKTDC - See **auto-message. please do not reply to this text message**" %participant['name']
                                call_action = client.messages.create(
                                        to="+" + participant['telephone'],
                                        from_="+442825022527", #from your purchased phone number
                                        body=message)
                                count += 1
                except ValueError:
                        error += 1
                    
print("Total SMS sent = " + count)

