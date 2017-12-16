from twilio.rest import Client
import csv
import datetime
import time

# put your own credentials here
account_sid = "ACe33417c9ba1a29f8ff2e00f982163279"
auth_token = "pw"

# need to define: number & message
client = Client(account_sid, auth_token)


#time data
def parse_time(time):
        time=datetime.datetime.strptime(time, "%H:%M:%S")
        return time
        
#some count variable
count = 0
done_list = []

with open('contact.csv') as csvfile:
        participants = csv.DictReader(csvfile)
        while len(done_list) != 6:
                for participant in participants:
                        try:
                                if participant['name'] not in done_list:                                          
                                        if datetime.datetime.now() > parse_time(participant['start_time']):
                                                if participant['country']=='HK':
                                                        message = "**Think Asia Think Hong Kong** Hello %s ! Testing! HKTDC - See **auto-message. please do not reply to this text message**" %participant['name']
                                                        call_action = client.messages.create(
                                                                to="+" + participant['telephone'],
                                                                from_="+85264522974",
                                                                body=message)
                                                        done_list.append(participant['name'])
                                                        count += 1
                                                        
                        except ValueError:
                                error += 1
                print("round " + str(count))
                time.sleep(60)
                    
print("Total SMS sent = " + str(len(done_list)))

