import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "ACCOUNT"
auth_token = "AUTHORIZATION"

client = Client(account_sid, auth_token)
csv_file = 'example.csv'

df = pd.read_csv(csv_file, encoding='utf-8', delimiter=';')

for index, row in df.iterrows():
    to = row['CELLPHONE']
    message = client.messages.create(
        to=to,
        from_="+16199999999",
        body="Example message."
    )
    print(f"Message sent to {to}: {message.sid}")
