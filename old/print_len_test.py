import csv

with open('contact.csv') as csvfile:
    participants = csv.DictReader(csvfile)
    print(participants)
