from twilio.rest import Client

account_sid = 'ACa45fdd1b344065a1bb62f32bc7c54b27'
auth_token = '125cc2187c41ee0ba87c23a17c29d286'
client = Client(account_sid, auth_token)

message = client.messages \
    .create(
        body='This is the ship that made the Kessel Run in fourteen parsecs?',
        from_='+13175264595',
        to='+13176206586'
    )

print(message.sid)
