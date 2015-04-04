__author__ = 'adam.mulroy'

from twilio import rest


account = 'twilioaccount'
token = 'twiliotoken'

client = rest.TwilioRestClient(account, token)

call = client.calls.create(from_='Number',
                           to='Number',
                           url="http://twimlets.com/message?Message")