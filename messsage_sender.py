import details as dt
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = '<Place your account_sid>'
auth_token = '<place your auth_token>'
client = Client(account_sid, auth_token)
for i in dt.getphonenumber():
    message = client.messages \
                    .create(
                         body="Tommorow is a Holiday!!!",
                         from_='<place your from number assigned by twilio>',
                         to= i
                     )

print(message.sid)
