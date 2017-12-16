import csv
import datetime
import time

def parse_time(time):
        time=datetime.datetime.strptime(time, "%m/%d/%y %H:%M")
        return time

done_list = []
count = 0
error = 0
roundnum = 0

with open('contact.csv') as csvfile:
        participants = csv.DictReader(csvfile)
        total = len(participants['name'])
            
while len(done_list) != total:
        with open('contact.csv') as csvfile:
            participants = csv.DictReader(csvfile)
            for participant in participants:
                        print(datetime.datetime.now())
                        print(parse_time(participant['start_time']))
                        if participant['name'] not in done_list:                                          
                            if datetime.datetime.now() > parse_time(participant['start_time']):
                                print(participant['name'])
                                done_list.append(participant['name'])
                                count += 1
                                
        roundnum += 1                               
        print("round " + str(roundnum) + " : " + "done: " + str(count))
        time.sleep(15)

