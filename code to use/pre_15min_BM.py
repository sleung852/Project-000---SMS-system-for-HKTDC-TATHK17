from twilio.rest import Client
import csv
import datetime
import time

def parse_time(time):
        time=datetime.datetime.strptime(time, "%m/%d/%y %H:%M")
        return time

total_number = input('What is the total number of contacts: ')
total_number = float(total_number)

# put your own credentials here
account_sid = "ACe33417c9ba1a29f8ff2e00f982163279"
auth_token = "6616ea79c6f9abbd825fa9ccbe6f80d5"

# need to define: number & message
client = Client(account_sid, auth_token)

done_list = []
count = 0
error = 0
roundnum = 0

while len(done_list) != total_number:
        with open('pre15contact.csv') as csvfile:
            participants = csv.DictReader(csvfile)
            for participant in participants:
                        print(datetime.datetime.now())
                        print(parse_time(participant['start_time']))
                        if participant['name'] not in done_list:                                          
                            if datetime.datetime.now() > parse_time(participant['start_time']):
                                        message = "*TATHK BM* Hello %s ! A gentle reminder about your business matching meeting with %s which will be starting in 15 minutes in the %s" %participant['name'] %participant['target'] %participant['location']
                                        call_action = client.messages.create(
                                                to="+" + participant['number'],
                                                from_="TATHK BM",
                                                body=message)
                                        count += 1
                                        print(participant['name'])
                                        done_list.append(participant['name'])
                                
        roundnum += 1                               
        print("round " + str(roundnum) + " : " + "done: " + str(count) + "left: " + str(3 - count))
        time.sleep(15)

print("Mission Accomplished!")
