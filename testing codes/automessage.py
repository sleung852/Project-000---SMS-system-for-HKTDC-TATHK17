from twilio.rest import Client


# put your own credentials here
account_sid = "ACe781be1700eeb534f6799df54ad61a35"
auth_token = "pw"



# need to define: number & message
client = Client(account_sid, auth_token)

result = client.messages.create(
        to='+447805112708',
        from_="+442380000397",
        body="##HKTDC Business Matching Service## We have received your on-site business matching form. However, due to the overwhelming demand, the companies that you are interested to meet are unable to meet you. However, we will pass your information and your contact to those parties.")

print(result.sid)
