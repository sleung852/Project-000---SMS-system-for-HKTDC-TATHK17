from twilio.rest import Client
import csv
import datetime
import time

def parse_time(time):
        time=datetime.datetime.strptime(time, "%m/%d/%y %H:%M")
        return time

# put your own credentials here
account_sid = "ACe33417c9ba1a29f8ff2e00f982163279"
auth_token = "6616ea79c6f9abbd825fa9ccbe6f80d5"

# need to define: number & message
client = Client(account_sid, auth_token)

done_list = []
count = 0
error = 0
roundnum = 0

while len(done_list) != 3:
        with open('contact.csv') as csvfile:
            participants = csv.DictReader(csvfile)
            for participant in participants:
                        print(datetime.datetime.now())
                        print(parse_time(participant['start_time']))
                        if participant['name'] not in done_list:                                          
                            if datetime.datetime.now() > parse_time(participant['start_time']):
                                if participant['country']=='HK':
                                        message = "**Think Asia Think Hong Kong** Hello %s ! We are excited to see you tomorrow! Please remember to bring your confirmation email tomorrow. Thanks! HKTDC - See **auto-message. please do not reply to this text message**" %participant['name']
                                        call_action = client.messages.create(
                                                to="+" + participant['telephone'],
                                                from_="+85264522974",
                                                body=message)
                                        count += 1
                                        print(participant['name'])
                                        done_list.append(participant['name'])

                                elif participant['country']=='UK':
                                        message = "**Think Asia Think Hong Kong** Hello %s ! We are excited to see you tomorrow! Please remember to bring your confirmation email tomorrow. Thanks! HKTDC - See **auto-message. please do not reply to this text message**" %participant['name']
                                        call_action = client.messages.create(
                                                to="+" + participant['telephone'],
                                                from_="+442825022527",
                                                body=message)
                                        count += 1
                                        print(participant['name'])
                                        done_list.append(participant['name'])

                                
        roundnum += 1                               
        print("round " + str(roundnum) + " : " + "done: " + str(count) + "left: " + str(3 - count))
        time.sleep(15)

print("Mission Accomplished!")
